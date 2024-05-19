import random
import string

def generateDeviceSecret(length=10):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length)).encode(encoding='UTF-8',errors='strict')

