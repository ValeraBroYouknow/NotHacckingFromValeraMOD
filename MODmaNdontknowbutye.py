import requests
from Core import fornicks
from Core import decor
import os, sys
from Core import ts
from requests import get
from bs4 import BeautifulSoup
from colorama import Fore, init
from prettytable import PrettyTable
import urllib, json, os
import requests, os, urllib.request, json, random, time


print(decor.chsystem)
global system
system = int(input(f"{decor.lye}[MODmaNdontknowbutye/chooseSystem] >> "))

if system == 1:
    os.system('cls')

elif system == 2:
    os.system('clear')

else:
    print(decor.lye + "UNKNOWN VALUE")


print(decor.banner)
while True:
    print(decor.menu)
    ans = int(input(f"{decor.lye}[MODmaNdontknowbutye/main] >> {decor.res}"))
    if ans == 1 and system == 1:
        os.system('cls')
        nick = input(f"{decor.lye}Enter Nickname >> ")
        print(f"{decor.lye} Messeagers and Soical Networks:")
        fornicks.osint(fornicks.snm, nick)
        print(f"{decor.lye} Videohostings:")
        fornicks.osint(fornicks.vh, nick)
        print(f"{decor.lye} Games:")
        fornicks.osint(fornicks.games, nick)
        print(f"{decor.lye} Forums:")
        fornicks.osint(fornicks.forums, nick)
        print(f"{decor.lye} Wallets:")
        fornicks.osint(fornicks.money, nick)
        print(f"{decor.lye} Other:")
        fornicks.osint(fornicks.other, nick)
        continue
    elif ans == 1 and system == 2:
        os.system('clear')
        nick = input(f"{decor.lye}Enter Nickname >> ")
        print(f"{decor.lye} Messeagers and Soical Networks:")
        fornicks.osint(fornicks.snm, nick)
        print(f"{decor.lye} Videohostings:")
        fornicks.osint(fornicks.vh, nick)
        print(f"{decor.lye} Games:")
        fornicks.osint(fornicks.games, nick)
        print(f"{decor.lye} Forums:")
        fornicks.osint(fornicks.forums, nick)
        print(f"{decor.lye} Wallets:")
        fornicks.osint(fornicks.money, nick)
        print(f"{decor.lye} Other:")
        fornicks.osint(fornicks.other, nick)
        continue
    elif ans == 4:
        break
    elif ans == 2 and system == 1:
        os.system('cls')
        ip = input(f"{decor.lye}Enter IP >> ")
        url = "https://ipinfo.io/" + ip + "/json"
        info = urllib.request.urlopen(url)
        ls = json.load(info)
        res  = rf'''{Fore.LIGHTGREEN_EX}
        Ciry -> {ls['city']}
        Region -> {ls["region"]}
        Location -> {ls["loc"]}
        Operator -> {ls["org"]}
        '''
        print(res)
        page = get("https://iknowwhatyoudownload.com/en/peer/?ip=" + ip,
                   headers=ts.headers)
        soup = BeautifulSoup(page.content, "html.parser")
        table = soup.find(class_="table").find("tbody")
        
        output = PrettyTable(["Name", "Category", "Size", "First seen", "Last seen"])
        for torrent in torrents:
            first, last = torrent.find_all(class_="date-column")
            first, last = first.text, last.text
            category = torrent.find(class_="category-column").text
            name = torrent.find(class_="name-column").text.replace("\n", '')
            size = torrent.find(class_="size-column").text
            output.add_row([name, category, size, first, last])

        print(f" {Fore.YELLOW}Found {len(torrents)} torrents... \n{Fore.LIGHTGREEN_EX}{output}{Fore.RESET}")
        continue
    elif ans == 2 and system == 2:
        os.system('clear')
        ip = input(f"{decor.lye}Enter IP >> ")
        url = "https://ipinfo.io/" + ip + "/json"
        info = urllib.request.urlopen(url)
        ls = json.load(info)
        res  = rf'''{Fore.LIGHTGREEN_EX}
        Ciry -> {ls['city']}
        Region -> {ls["region"]}
        Location -> {ls["loc"]}
        Operator -> {ls["org"]}
        '''
        print(res)
        page = get("https://iknowwhatyoudownload.com/en/peer/?ip=" + ip,
                   headers=ts.headers)
        soup = BeautifulSoup(page.content, "html.parser")
        table = soup.find(class_="table").find("tbody")
        torrents = table.find_all("tr")
        output = PrettyTable(["Name", "Category", "Size", "First seen", "Last seen"])
        for torrent in torrents:
            first, last = torrent.find_all(class_="date-column")
            first, last = first.text, last.text
            category = torrent.find(class_="category-column").text
            name = torrent.find(class_="name-column").text.replace("\n", '')
            size = torrent.find(class_="size-column").text
            output.add_row([name, category, size, first, last])

        print(f" {Fore.YELLOW}Found {len(torrents)} torrents... \n{Fore.LIGHTGREEN_EX}{output}{Fore.RESET}")
        continue
    elif ans == 3 and system == 1:
        os.system('cls')
        print(decor.sher_menu)
        vari = input(f"{decor.lye}[MODmaNdontknowbutye/main/lolahahahaah/category] >> {decor.res}")
            try:
                print(decor.lye)
                print(u"Country >>", infoPhone["country"]["name"])
                print(u"Region >>", infoPhone["region"]["name"])
                print(u"Operator >>", infoPhone["0"]["oper"])
                print(u"City >>", infoPhone["0"]["name"])
                print(decor.res)
            except:
                print(f"{decor.lre}On TOR to continue working")

    elif ans == 3 and system == 2:
        os.system('clear')
        print(decor.sher_menu)
        vari = input(f"{decor.lye}[MODmaNdontknowbutye/main/carNphone/category] >> {decor.res}")
        elif vari == "1":
            phone = input(f"{decor.lye}Enter Phone Number >> ")
            getInfo = "https://htmlweb.ru/geo/api.php?json&telcod=" + phone
            try:
                infoPhones = urllib.request.urlopen( getInfo )
            except:
                print(f"{decor.red}[no result]")
            infoPhone = json.load( infoPhones )

            try:
                print(decor.lye)
                print(u"Country >>", infoPhone["country"]["name"])
                print(u"Region >>", infoPhone["region"]["name"])
                print(u"Operator >>", infoPhone["0"]["oper"])
                print(u"City >>", infoPhone["0"]["name"])
                print(decor.res)
            except:
                print(f"{decor.lre}On TOR to continue working")
