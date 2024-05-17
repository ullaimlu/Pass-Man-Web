from getpass import getpass
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Hash import SHA512
from Crypto.Random import get_random_bytes
from utils.pipelines import *

from rich import print as printc

import utils.aesutil 

def computeMasterKey(mp, ds):
    password = mp.encode()
    salt = ds.encode()
    key = PBKDF2(password, salt, 32, count=1000000, hmac_hash_module=SHA512)
    return key

def addEntry(mp, ds, sitename, siteurl, email, username):
    # get the password
    password = getpass("Password: ")

    mk = computeMasterKey(mp, ds)

    encrypted = utils.aesutil.encrypt(key=mk, source=password, keyType="bytes")

    ob = WebsitePipeline()
    ob.process_item(sitename, siteurl, email, username, encrypted)

    printc("[green][+][/green] Added entry ")

