from rich import print
import os
from rich.console import Console

console = Console()
from cript import *
from decript import *


def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

clear_terminal()
print("[underline cyan]You can use drag and drop to input file paths![/underline cyan]")

print("[bold white]1. Encryption mode[/bold white]")
print("[bold white]2. Decryption mode[/bold white]")
choice = console.input("[white]Write the mode number: [/white]")
choice = int(choice)
clear_terminal()

if choice == 1:
    print("[bold green]Write the path to the file:[/bold green] [italic cyan]/path/to/your/file[/italic cyan]")
    OrigFile = input()
    clear_terminal()
    Encryption(OrigFile)
    print("[bold magenta]The file is encrypted and saved as[/bold magenta] [italic yellow]encrypted.txt[/italic yellow] [bold magenta]with[/bold magenta] [italic yellow]key.bin![/italic yellow]")

if choice == 2:
    print("[bold green]Write the path to encrypted file:[/bold green] [cyan]/path/to/encrypted.txt[/cyan]")
    CryptFile = input()
    clear_terminal()
    print("[bold green]Write the path to key file:[/bold green] [cyan]/path/to/key.bin[/cyan]")
    Keyfile = input()
    clear_terminal()
    Decryption(CryptFile, Keyfile)
    print("[bold][yellow]Successfully decrypted![/yellow][/bold]")
