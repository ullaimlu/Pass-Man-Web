import requests
import time 
import random
import string

def send_security_code(phone):
    code=generatecode()
    send_message(phone, code)
    return code

def send_message(phone, mensaje):
    url = 'http://localhost:5433/lead'
    
    data = {
        "message": f"*Your PassMan security code is:* \n \n 🔐 {mensaje}",
        "phone": phone
    }
    headers = {
        'Content-Type':'application/json'
    }
    info= requests.post(url, json=data, headers=headers)
    time.sleep(10)
    return info

def generatecode(length=6):
    return ''.join(random.choices(string.digits, k=length))
