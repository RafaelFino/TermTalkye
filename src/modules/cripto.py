from cryptography.fernet import Fernet
import base64
import os
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.backends import default_backend

class Crypto:
    def __init__(self, key: str) -> None:
        self.key  = base64.b64encode(str(key.ljust(32, "#")[:32]).encode('ascii'))
        self.cipher = Fernet(self.key, backend=None)
    
    def encrypt(self, message: str) -> str:
        return self.cipher.encrypt(message.encode('ascii')).decode('ascii')

    def decrypt(self, message: str) -> str:
        m = message.encode('ascii')
        return self.cipher.decrypt(m,).decode('ascii')
    
class AssimetricCryptoClient:
    def __init__(self):
        self._pu_path = f"./keys/public_key.pem" 
        if not os.path.isfile(self._pu_path):
            raise Exception(f"We need a public key on {self._pu_path} to continue")
        
        with open(self._pu_path, 'rb') as key_file:
            self._key = serialization.load_pem_public_key(
            key_file.read(),
            backend=default_backend()
        )

        self._padding = padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
            

    def Encript(self, message:str):
        encrypt = self._key.encrypt(message.encode('ascii'), self._padding)
        base64_bytes = base64.b64encode(encrypt)
        return base64_bytes.decode('ascii')

    def GetPublicKey(self):
        return self._key    