import os
import TermTk as ttk
from modules.config import Config

class Tabs:
    def __init__(self, root: ttk.TTk ) -> None:
        self.root = root

    def createMainTabs(self, sendCallback):
        self.sendTextCallback = sendCallback
        self.tab = ttk.TTkTabWidget(parent=self.root, pos=(0, Config.Size.lines - (Config.PNL_BORDER_HEIGHT + Config.PNL_MAIN_HEIGHT)), size=(Config.Size.columns, Config.PNL_MAIN_HEIGHT + Config.BUTTON_HEIGHT), border=True)
        
        self.__createLoginTab() 
        self.__createMessageTab()
        self.__createLogViewTab()
        
    def __createMessageTab(self):
        pnl = ttk.TTkContainer(parent=self.tab, pos=(0, 0), size=(Config.Size.columns, Config.PNL_MAIN_HEIGHT), border=True)  
       
        self.te = ttk.TTkTextEdit(parent=pnl, lineNumber=False, pos=(0,0), size=(Config.Size.columns - Config.BUTTON_WIDTH - Config.PNL_BORDER_WIDTH- Config.PNL_BORDER_WIDTH, 5), multiline=True)
        self.te.setLineWrapMode(ttk.TTkK.WidgetWidth)
        self.te.setWordWrapMode(ttk.TTkK.WordWrap)
        self.te.setReadOnly(False)
        self.te.setText("")
        self.te.setColor(ttk.TTkColor.fg('#FFFAFA'))

        pnl.addWidget(self.te)

        btnSend = ttk.TTkButton(parent=pnl, pos=(Config.Size.columns - Config.BUTTON_WIDTH - Config.PNL_BORDER_WIDTH, 0), size=(Config.BUTTON_WIDTH, 5), border=True, text="Send")
        pnl.addWidget(btnSend)        

        btnSend.clicked.connect(lambda: self.sendText())

        self.tab.addTab(pnl, "Send message")

    def __createLoginTab(self):
        pnl = ttk.TTkContainer(parent=self.tab, pos=(0, 0), size=(Config.Size.columns, Config.PNL_MAIN_HEIGHT), border=True)  
    
        ttk.TTkLabel(parent=pnl, pos=(0,1), size=(6,1), border=True, text="User:")
        txtUser = ttk.TTkLineEdit(parent=pnl, pos=(6,1), size=(64,1), border=True, text="")
        
        ttk.TTkLabel(parent=pnl, pos=(0,2), size=(6,1), border=True, text="Pass:")
        txtPass = ttk.TTkLineEdit(parent=pnl, pos=(6,2), size=(64,1), border=True, text="", inputType=ttk.TTkK.Input_Text|ttk.TTkK.Input_Password)
            
        btnLogin = ttk.TTkButton(parent=pnl, pos=(0, 4), size=Config.BUTTON_SIZE, border=True, text="Login")
        btnCreate = ttk.TTkButton(parent=pnl, pos=(Config.BUTTON_WIDTH + 2, 4), size=Config.BUTTON_SIZE, border=True, text="Create")    

        self.tab.addTab(pnl, "Login")


    def __createLogViewTab(self):        
        pnl = ttk.TTkLogViewer(parent=self.tab, pos=(Config.Size.columns - 18, 0), size=(Config.Size.columns, Config.PNL_MAIN_HEIGHT), border=True)
        self.tab.addTab(pnl, "Log Viewer")

    
    def sendText(self):
        msg = self.te.toPlainText()
        self.sendTextCallback(msg)        
        self.te.setText("")        
