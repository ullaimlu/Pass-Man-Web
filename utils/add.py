from getpass import getpass
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Hash import SHA512
from Crypto.Random import get_random_bytes
from .pipelines import *
from .aesutil import *

def computeMasterKey(mp, ds):
    password = mp.encode()
    salt = ds.encode()
    key = PBKDF2(password, salt, 32, count=1000000, hmac_hash_module=SHA512)
    return key

def addEntry(mp, ds, sitename, username, password, user_id, selenium_id):
    mk = computeMasterKey(mp, ds)

    encrypted = encrypt(key=mk, source=password, keyType="bytes")

    ob = WebsitePipeline()
    ob.process_item(sitename,username, encrypted, user_id, selenium_id)

