import requests
import os
import colorama
from os import system, name
import time
from colorama import Fore
colorama.init()

os.system("cls")

print(f'''
{Fore.RED} ▌ ▐·▪   ▐ ▄ .▄▄ · ▄▄▄▄▄▄▄▄▄   ▄▄▄·  ▄▄· ▄ •▄ ▄▄▄ .▄▄▄  
{Fore.YELLOW}▪█·█▌██ •█▌▐█▐█ ▀. ▀•██ ▀▀▄ █·▐█ ▀█ ▐█ ▌▪█▌▄▌▪▀▄.▀·▀▄ █·
{Fore.YELLOW}▐█▐█•▐█·▐█▐▐▌▄▀▀▀█▄  ▐█.▪▐▀▀▄ ▄█▀▀█ ██ ▄▄▐▀▀▄·▐▀▀▪▄▐▀▀▄ 
{Fore.RED} ███ ▐█▌██▐█▌▐█▄▪▐█  ▐█▌·▐█•█▌▐█▪ ▐▌▐███▌▐█.█▌▐█▄▄▌▐█•█▌
{Fore.RED}. ▀  ▀▀▀▀▀ █▪ ▀▀▀▀   ▀▀▀ .▀  ▀ ▀  ▀ ·▀▀▀ ·▀  ▀ ▀▀▀ .▀  ▀
''')

time.sleep(1)

print(f"{Fore.WHITE}_" * 50)
time.sleep(1)
print(" ")
print(" ")
host = input(f"{Fore.GREEN}>> {Fore.BLUE}Introduce el host a escanear:{Fore.WHITE} ")
api = f"https://ipapi.co/{host}/json/"
print(" ")
print(f"{Fore.WHITE}_" * 50)
time.sleep(1)
print(" ")
print(" ")

req = requests.get(api)
print(req.json())