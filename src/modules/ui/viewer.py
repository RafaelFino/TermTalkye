import os
from datetime import datetime
from TermTk.TTkCore.constant import TTkK
from TermTk.TTkCore.log import TTkLog
from TermTk.TTkCore.color import TTkColor
from TermTk.TTkCore.string import TTkString
from TermTk.TTkCore.signal import pyTTkSlot
from TermTk.TTkAbstract.abstractscrollarea import TTkAbstractScrollArea
from TermTk.TTkAbstract.abstractscrollview import TTkAbstractScrollView

class _MessageViewer(TTkAbstractScrollView):
    __slots__ = ('_color', '_text', '_messages', '_cwd', '_follow')
    def __init__(self, *args, **kwargs):
        TTkAbstractScrollView.__init__(self, *args, **kwargs)
        self._messages = [TTkString()]
        self._cwd = os.getcwd()
        self._follow = kwargs.get('follow' , False )
        self.viewChanged.connect(self._viewChangedHandler)

    @pyTTkSlot()
    def _viewChangedHandler(self):
        self.update()

    def viewFullAreaSize(self) -> (int, int):
        w = max( m.termWidth() for m in self._messages)
        h = len(self._messages)
        return w , h

    def viewDisplayedSize(self) -> (int, int):
        return self.size()

    def append(self, user:str, message:str):
        dt = datetime.now().strftime("%G/%m/%d %H:%M:%S")        
        head = TTkString(text=f"{dt} [{user}]:", color=TTkColor.fg('#FFFF00') | TTkColor.BOLD) 
        self._messages.append(head)

        msg = TTkString(text=f"> {message}", color=TTkColor.fg('#FFFFFF'))
        self._messages.append(msg)

        offx, offy = self.getViewOffsets()
        _,h = self.size()
        if self._follow or offy == len(self._messages)-h-1:
            offy = len(self._messages)-h
        self.viewMoveTo(offx, offy)
        self.viewChanged.emit()
        self.update()

    def paintEvent(self, canvas):
        ox,oy = self.getViewOffsets()
        _,h = self.size()
        for y, message in enumerate(self._messages[oy:oy+h]):
            canvas.drawTTkString(pos=(-ox,y),text=message)

class MessageViewer(TTkAbstractScrollArea):
    __slots__ = ('_messageView')
    def __init__(self, *args, **kwargs):
        TTkAbstractScrollArea.__init__(self, *args, **kwargs)
        if 'parent' in kwargs: kwargs.pop('parent')
        self._viewer = _MessageViewer(*args, **kwargs)
        self.setFocusPolicy(TTkK.ClickFocus)
        self.setViewport(self._viewer)

    def append(self, user:str, message:str):
        self._viewer.append(user,message)