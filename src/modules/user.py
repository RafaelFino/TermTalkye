class User:    
    def __init__(self, user, pass) -> None:
        self.user = user
        self.token = None

    def auth(self, passwd:str) -> bool:
        return False

    def create(self) -> bool:
        return False
    
    def updatePassword(self) -> bool:
        return False
