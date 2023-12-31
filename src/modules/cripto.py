from cryptography.fernet import Fernet
import base64

class Crypto:
    def __init__(self, key: str) -> None:
        self.key  = base64.b64encode(str(key.ljust(32, "#")[:32]).encode('ascii'))
        self.cipher = Fernet(self.key, backend=None)
    
    def encrypt(self, message: str) -> str:
        return self.cipher.encrypt(message.encode('ascii')).decode('ascii')

    def decrypt(self, message: str) -> str:
        m = message.encode('ascii')
        return self.cipher.decrypt(m,).decode('ascii')