from pyfiglet import figlet_format
from termcolor import colored

def banner():
    print(colored(figlet_format("lightsec-xploit", font="slant"), "red"))
    print(colored("By Neok1ra | For Labs. Not Chaos.", "white"))
