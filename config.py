from utils.dbconfig import db_connect, Secrets
from utils.pipelines import MasterPassPipeline
import hashlib
import random
import string
from getpass import getpass

from rich import print as printc
from rich.console import Console

console = Console()

def generateDeviceSecret(length=10):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length)).encode(encoding='UTF-8',errors='strict')

def config():
    while True:
        mp = getpass("Choose a MASTER PASSWORD: ")
        if mp==getpass("Re-type: ") and mp!="":
            break
        printc("[yellow][-] Please try again.[/yellow]")

    #Hash the MASTER PASSWORD
    hashed_mp = hashlib.sha256(mp.encode()).hexdigest()
    printc("[green][+][/green] Generated hash of MASTER PASSWORD")

    ds = generateDeviceSecret()
    printc("[green][+][/green] Device Secret generated")
    
    ob = MasterPassPipeline()
    ob.process_item(hashed_mp,ds)

config()