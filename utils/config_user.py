from .pipelines import *
import hashlib
import random
import string

def generateDeviceSecret(length=10):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length)).encode(encoding='UTF-8',errors='strict')

def config_user(user,mp):
    hashed_mp = hashlib.sha256(mp.encode()).hexdigest()
    ds = generateDeviceSecret() 
    ob = PassManUserPipeline()
    ob.process_item(user,hashed_mp,ds)
