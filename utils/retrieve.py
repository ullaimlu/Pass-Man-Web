from .aesutil import *

from getpass import getpass
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Hash import SHA512
from Crypto.Random import get_random_bytes
from .add import computeMasterKey

def retrieve(mp, ds, password):
    mk = computeMasterKey(mp, ds)    
    decrypted = decrypt(key=mk, source=password, keyType="bytes")
    return decrypted.decode()

