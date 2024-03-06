import requests
import os


class color:
    reset = '\033[0m'
    red = '\033[31m'
    yellow = '\033[33m'
    magenta = '\033[35m'
    cyan = '\033[36m'
    gray = '\033[90m'
    italic = '\033[3m'


def cls():
    if os.name == 'nt':
        os.system("cls")
    else:
        os.system("clear")


def intro():
    cls()
    print(f"{color.red}     ___           __  {color.magenta}  ____         ")
    print(f"{color.red}    / _ \___  ____/ /__{color.magenta} / __/_ _  ___ ")
    print(f"{color.red}   / // / _ `/ __/  '_/{color.magenta}_\ \/  ' \(_-< ")
    print(f"{color.red}  /____/\_,_/_/ /_/\_\{color.magenta}/___/_/_/_/___/ ")
    print(color.reset)
    print(f"{color.italic}{color.red}                         by alfanowski \n")
    print(color.reset, end="")


def control(var, a):
    if (len(var) > 4 and a) or (not (3 <= len(var) <= 15) and not a):
        return False
    if not var.isdigit():
        return False
    return True


def sure(cc, pn, ms):
    while True:
        cls()
        intro()
        print(f"{color.cyan}    Country Code:  {color.gray}{cc}{color.reset}")
        print(f"{color.cyan}    Phone Number:  {color.gray}{pn}{color.reset}")
        print(f"{color.cyan}    Message:  {color.gray}{ms}{color.reset}")
        sel = input(f"\n{color.yellow}    Are you sure (y / n)?  {color.reset}").lower()
        if sel == 'y':
            return True
        elif sel == 'n':
            return False


def sendMessage():
    while True:
        cls()
        intro()
        countryCode = input(f"{color.cyan}    Country Code:  {color.gray}+{color.reset}")
        if control(countryCode, True):
            break
    countryCode = '+' + countryCode
    while True:
        cls()
        intro()
        print(f"{color.cyan}    Country Code:  {color.gray}{countryCode}{color.reset}")
        phoneNumber = input(f"{color.cyan}    Phone Number:  {color.reset}")
        if control(phoneNumber, False):
            break
    cls()
    intro()
    print(f"{color.cyan}    Country Code:  {color.gray}{countryCode}{color.reset}")
    print(f"{color.cyan}    Phone Number:  {color.gray}{phoneNumber}{color.reset}")
    message = input(f"{color.cyan}    Message:  {color.reset}")
    if not sure(countryCode, phoneNumber, message):
        sendMessage()
    resp = requests.post('https://textbelt.com/text',{
			'phone': countryCode + phoneNumber,
			'message': message,
			'key': 'textbelt' })
    print("\n   ", resp.json())



sendMessage()
