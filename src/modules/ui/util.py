import TermTk as ttk
import os

def getCenter(w:int, h: int) -> tuple:
    size = os.get_terminal_size()
    x = int((size.lines-h)/2)
    y = int((size.columns-w)/2)
    return (y,x)

def createWindow(root: ttk.TTk, w: int, h: int, title: str = "Window"):
    ret = ttk.TTkWindow(parent=root, pos=getCenter(w, h), size=(w, h), title=title, border=True)
    
    ret.setMinimumHeight(h)
    ret.setMaximumHeight(h)  
    ret.setMinimumWidth(w)    
    ret.setMaximumWidth(w)
    
    return ret