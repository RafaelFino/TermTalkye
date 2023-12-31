import os
import TermTk as ttk
from modules.config import Config

class Title:
    def __init__(self, root: ttk.TTk) -> None:
        self.root = root

    def create(self):
        title = ttk.TTkLabel(parent=self.root, pos=(0, 0), size=(Config.Size.columns, 2), border=True, text=f"{Config.APP_NAME} v{Config.APP_VERSION} ({Config.APP_RELEASE_DATE})", titleColor=ttk.TTkColor.BOLD) 
        title.setAlignment(ttk.TTkK.Alignment.CENTER_ALIGN)
        title.setColor(ttk.TTkColor.fg('#FFFAFA'))
        title.setColor(ttk.TTkColor.bg('#0000FF'))

    def setText(self, text: str):
        self.title.setText(text)