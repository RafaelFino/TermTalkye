import os
import TermTk as ttk
from modules.config import Config
from modules.ui.viewer import MessageViewer
from datetime import datetime

class Receiver:
    def __init__(self, root: ttk.TTk) -> None:
        self.root = root

    def create(self):
        self.pnl = ttk.TTkContainer(parent=self.root, pos=(Config.SIDEBAR_WIDTH, 1), size=(Config.Size.columns - Config.SIDEBAR_WIDTH, Config.RECEIVER_HEIGHT), border=True)  

        self.chat = ttk.TTkLabel(parent=self.pnl, pos=(0, 0), size=(Config.Size.columns - Config.SIDEBAR_WIDTH, 2), border=True, text="", titleColor=ttk.TTkColor.BOLD) 
        self.chat.setColor(ttk.TTkColor.fg('#FFFF00') | ttk.TTkColor.bg('#2222AA'))

        #self.rcv = ttk.TTkTextEdit(parent=self.pnl, lineNumber=False, pos=(0,2), size=(Config.Size.columns - Config.SIDEBAR_WIDTH, Config.RECEIVER_HEIGHT), multiline=True)
        self.rcv = MessageViewer(parent=self.pnl, pos=(0,2), size=(Config.Size.columns - Config.SIDEBAR_WIDTH, Config.RECEIVER_HEIGHT-2), follow=True)
        
        self.pnl.addWidget(self.rcv)

    def append(self, user: str, text: str):
        self.rcv.append(user, text)
        
    def setChatText(self, text: str):
        self.chat.setText(text)          