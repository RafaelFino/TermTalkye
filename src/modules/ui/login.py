import TermTk as ttk

class Login:
    def __init__(self, root: ttk.TTk):
        self.root = root

    def show(self):       
        login = ttk.TTkWindow(parent=self.root, pos = (10,10), size=(40,8), title="Login", border=True, layout=ttk.TTkLayout())
        layout = login.layout()
        
        ttk.TTkLabel(parent=login, pos=(0,0), size=(6,1), border=True, text="&User:")
        ttk.TTkLineEdit(parent=login, pos=(6,0), size=(32,1), border=True, text="")
        ttk.TTkLabel(parent=login, pos=(0,1), size=(6,1), border=True, text="&Pass:")
        ttk.TTkLineEdit(parent=login, pos=(6,1), size=(32,1), border=True, text="")        
        ttk.TTkButton(parent=login, pos=(0,3), size=(18,1), border=True, text="&Login", command=lambda: login.close())
        ttk.TTkButton(parent=login, pos=(20,3), size=(18,1), border=True, text="&Quit", command=lambda: login.close())

        self.root.mainloop()
