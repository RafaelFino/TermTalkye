import os
import TermTk as ttk
from modules.config import Config

class Footer:
    def __init__(self, root: ttk.TTk) -> None:
        self.root = root

    def create(self):
        footer = ttk.TTkLabel(parent=self.root, pos=(0, Config.Size.lines-1), size=(Config.Size.columns, 2), border=True, text="", titleColor=ttk.TTkColor.BOLD) 
        footer.setColor(ttk.TTkColor.fg('#FFFAFA'))
        footer.setColor(ttk.TTkColor.bg('#AAAAAA'))