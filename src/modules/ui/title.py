import os
import TermTk as ttk
from modules.config import Config

class Title:
    def __init__(self, root: ttk.TTk) -> None:
        self.root = root

    def create(self):
        self.title = ttk.TTkLabel(parent=self.root, pos=(0, 0), size=(Config.Size.columns, 2), border=True, text=f"{Config.APP_NAME} v{Config.APP_VERSION} ({Config.APP_RELEASE_DATE})", titleColor=ttk.TTkColor.BOLD) 
        self.title.setAlignment(ttk.TTkK.Alignment.CENTER_ALIGN)
        self.title.setColor(ttk.TTkColor.fg('#FFFAFA') | ttk.TTkColor.bg('#0000FF'))