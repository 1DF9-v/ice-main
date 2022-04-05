import os
import requests
import time
from threading import Thread
from colorama import init, Fore, Back, Style
import os.path
import ctypes
from colorama import Fore
from time import sleep







ctypes.windll.kernel32.SetConsoleTitleW("ice tool by 475456425062301696 or 314843899736883200 | https://discord.gg/FatDtTeMpM")




def deletewebhook(url):
	return requests.delete(url)


os.system('cls')


banner = """


▪   ▄▄· ▄▄▄ .
██ ▐█ ▌▪▀▄.▀·
▐█·██ ▄▄▐▀▀▪▄
▐█▌▐███▌▐█▄▄▌
▀▀▀·▀▀▀  ▀▀▀ 

by : https://discord.gg/FatDtTeMpM\n please join for any problem and open a ticket

> https://discord.gg/FatDtTeMpM
> https://github.com/1DF9-v                                            
"""

while True:
    print(banner)
    print(f"""{Fore.CYAN}\n════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════ \n yt : ace logges - discord : notace_#0019 or acee_#0019
id : 314843899736883200 or 475456425062301696 github : 1DF9-v | discord.gg/FatDtTeMpM\n{Fore.CYAN}\n{Fore.GREEN}[1]{Fore.CYAN} Delete Webhook
{Fore.GREEN}[2]{Fore.CYAN} Webhook spammer\n ═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════""")
    choice = input("\n ice@root~$>>> ")












    if choice == '1':
        webhook = input("Webhook URL \n ice@root~$>>>  ")
        deletewebhook(webhook)




    elif choice == "2":
        actual = input("Webhook URL: ")
        msg = input("Message: \n ice@root~$>>> ")
        for x in range(1000):
            sendwebhook = requests.post(actual, json={'content': msg})


    time.sleep(0)
    actual.send(msg)
    print("Sent")

  