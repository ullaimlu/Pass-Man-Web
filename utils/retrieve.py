from utils.pipelines import EntriesPipeline

from rich import print as printc
from rich.console import Console
from rich.table import Table

import utils.aesutil

from getpass import getpass
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Hash import SHA512
from Crypto.Random import get_random_bytes
from utils.add import computeMasterKey
import pyperclip

def retrieveEntries(mp, ds, search, decryptPassword = False):
    ob = EntriesPipeline()
    results = ob.get_item(search)
    print(results[0][0].sitename)
    if (decryptPassword and len(results)>1) or (not decryptPassword):
        table = Table(title="Results")
        table.add_column("Site Name")
        table.add_column("URL")
        table.add_column("Email")
        table.add_column("Username")
        table.add_column("Password")

        for i in results:
            table.add_row(i[0].sitename, i[0].siteurl, i[0].email, i[0].username, "{hidden}")

        console = Console()
        console.print(table)

        return
    
    if len(results) == 1 and decryptPassword:
        mk = computeMasterKey(mp, ds)
        
        decrypted = utils.aesutil.decrypt(key=mk, source=results[0][0].passwrd, keyType="bytes")

        pyperclip.copy(decrypted.decode())
        printc("[green][+][/green] Password copied to clipboard")

