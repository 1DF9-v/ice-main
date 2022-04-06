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
    print(f"""{Fore.CYAN}\n════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════
{Fore.CYAN}\n{Fore.GREEN}[1] or [del]{Fore.CYAN} Delete Webhook
{Fore.GREEN}[2]{Fore.CYAN} Webhook spammer\n\n═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════""")
    choice = input("\n ice@root~$>>> ")













    if choice == '1':
        ctypes.windll.kernel32.SetConsoleTitleW("webhook deleted ! | join : https://discord.gg/FatDtTeMpM")
        webhook = input("Webhook URL \n ice@root~$>>>  ")
        deletewebhook(webhook)

    if choice == 'del':
        ctypes.windll.kernel32.SetConsoleTitleW("webhook deleted ! | join : https://discord.gg/FatDtTeMpM")
        webhook = input("put the webhook after the *del like *del https://discord.com/api/webhooks/ \n *del ")
        deletewebhook(webhook)






    elif choice == "2":
        actual = input("Webhook URL: ")
        msg = input("Message: \n ice@root~$>>> ")
        for x in range(1000):
            ctypes.windll.kernel32.SetConsoleTitleW("sended in webhook | join : https://discord.gg/FatDtTeMpM")
            print('send in webhook >>>  ' + msg)
            sendwebhook = requests.post(actual, json={'content': msg})
        time.sleep(0)



  