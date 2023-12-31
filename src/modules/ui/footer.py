import os
import TermTk as ttk
from modules.config import Config

class Footer:
    def __init__(self, root: ttk.TTk) -> None:
        self.root = root

    def create(self):
        self.footer = ttk.TTkLabel(parent=self.root, pos=(0, Config.Size.lines-1), size=(Config.Size.columns, 2), border=True, text="", titleColor=ttk.TTkColor.BOLD) 
        self.footer.setAlignment(ttk.TTkK.Alignment.CENTER_ALIGN)
        self.footer.setColor(ttk.TTkColor.fg('#000000') | ttk.TTkColor.bg('#AAAAAA'))

    def setText(self, text: str):
        self.footer.setText(text)        