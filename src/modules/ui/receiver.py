import os
import TermTk as ttk
from modules.config import Config
from datetime import datetime

class Receiver:
    def __init__(self, root: ttk.TTk) -> None:
        self.root = root

    def create(self):
        self.pnl = ttk.TTkContainer(parent=self.root, pos=(Config.SIDEBAR_WIDTH, 1), size=(Config.Size.columns - Config.SIDEBAR_WIDTH -1, Config.RECEIVER_HEIGHT), border=True)  

        self.rcv = ttk.TTkTextEdit(parent=self.pnl, lineNumber=False, pos=(0,0), size=(Config.Size.columns - Config.SIDEBAR_WIDTH - 1, Config.RECEIVER_HEIGHT), multiline=True)
        self.rcv.setColor(ttk.TTkColor.fg('#FFFF00'))
        self.pnl.addWidget(self.rcv)
        self.rcv.setReadOnly(True)

    def append(self, user: str, text: str):
        dt = datetime.now().strftime("%G/%m/%d %H:%M:%S")        
        input = ttk.TTkString(text=f"{dt} [{user}]:", color=ttk.TTkColor.fg('#FFFF00') | ttk.TTkColor.BOLD) + ttk.TTkString(text=f"\n> {text}", color=ttk.TTkColor.fg('#FFFFFF'))
        self.rcv.append(input)        
        
        
        