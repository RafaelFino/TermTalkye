import os
import TermTk as ttk
from modules.config import Config

class Sidebar:
    def __init__(self, root: ttk.TTk) -> None:
        self.root = root

    def create(self):
        self.sidebar = ttk.TTkFrame(parent=self.root, pos=(0, 2), size=(Config.SIDEBAR_WIDTH-1, Config.RECEIVER_HEIGHT-1), border=True, title="Login")  
    
        self.login = ttk.TTkContainer(parent=self.sidebar, pos=(0, 0), size=(Config.SIDEBAR_WIDTH-1, Config.RECEIVER_HEIGHT-1), border=True, title="Login")  
        ttk.TTkLabel(parent=self.login, pos=(0,1), size=(6,1), border=True, text="User:")
        self.txtUser = ttk.TTkLineEdit(parent=self.login, pos=(0,2), size=(Config.SIDEBAR_WIDTH-1,1), border=True, text="")
        
        ttk.TTkLabel(parent=self.login, pos=(0,4), size=(6,1), border=True, text="Pass:")
        self.txtPass = ttk.TTkLineEdit(parent=self.login, pos=(0,5), size=(Config.SIDEBAR_WIDTH-1,1), border=True, text="", inputType=ttk.TTkK.Input_Text|ttk.TTkK.Input_Password)
            
        btnLogin = ttk.TTkButton(parent=self.login, pos=(0, 9), size=(Config.SIDEBAR_WIDTH-4, Config.BUTTON_HEIGHT), border=True, text="Login")
        btnCreate = ttk.TTkButton(parent=self.login, pos=(0, 11), size=(Config.SIDEBAR_WIDTH-4, Config.BUTTON_HEIGHT), border=True, text="Create")
        btnLogin.clicked.connect(lambda: self.LoginAccepeted())   

    def LoginAccepeted(self):
        self.sidebar.layout().removeWidget(self.login)
        self.createChatList()

    def createChatList(self):
        self.sidebar.setTitle("Chat list")  
        self.chatList = ttk.TTkList(parent=self.sidebar, pos=(0, 1), size=(Config.SIDEBAR_WIDTH-1, Config.RECEIVER_HEIGHT), border=True, title="Chat list")
        self.chatList.textClicked.connect(self.chatSelected)    

    def addChat(self, items: list):
        self.chatList.addItems(items)    

    def chatSelected(self, label: str):
        ttk.log.TTkLog.debug(f"Chat selected: {label}")
        
