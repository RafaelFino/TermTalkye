import os
import TermTk as ttk
from modules.config import Config
from modules.ui.title import Title
from modules.ui.footer import Footer
from modules.ui.tabs import Tabs
from modules.ui.receiver import Receiver
class Manager:
    def __init__(self) -> None:
        ttk.TTkLog.use_default_file_logging()   
        
    def init(self) -> None:
        self.root = ttk.TTk(size=(Config.Size.columns, Config.Size.lines), title="Talkye", border=True, mouseTracking=True, debug=True)
           
        self.title = Title(self.root)
        self.title.create()

        self.receiver = Receiver(self.root)
        self.receiver.create()

        self.footer = Footer(self.root)
        self.footer.create() 

        self.tabs = Tabs(self.root)    
        self.tabs.createMainTabs(self.callSend)   


        self.root.mainloop()     

    def callSend(self, msg: str):
        ttk.log.TTkLog.debug(f"Sending message: {msg}")
        self.receiver.append("Me", msg)    