version = "1.2"
scriptURL = "https://raw.githubusercontent.com/alfanoandrea/DarkSms/main/DarkSms.py"

import requests
import re
import os


class color:
    violet = "\033[35;1m"
    red = "\u001b[31;1m"
    cyan = "\u001b[36;1m"
    green = "\u001b[32;1m"
    yellow = "\u001b[33;1m"
    magenta = "\u001b[35;1m"
    gray = "\033[90;1m"
    italic = "\033[3;1m"
    reset = "\u001b[0m"


def cls():   
    os.system("cls") if os.name == 'nt' else os.system("clear")


def internet():
    try:
        requests.head('https://www.google.com', timeout=5) 
        return True
    except requests.exceptions.RequestException:
        return False


def update():
    intro()
    try:
        response_check = requests.get(scriptURL, headers={'Range': 'bytes=0-200'}, timeout=5)
        response_check.raise_for_status()
        first_lines = response_check.text
        match = re.search(r'version\s*=\s*["\'](\d+\.\d+)["\']', first_lines)    
        if not match:
            return
        latestVersion = match.group(1)
        
    except requests.exceptions.RequestException:
        return

    if version != latestVersion:
        print(f"{color.yellow}  New version {color.green}({latestVersion}){color.yellow} avaible. Updating...{color.reset}\n")
        try:
            response_script = requests.get(scriptURL, timeout=10)
            response_script.raise_for_status()
            script_filename = os.path.basename(__file__)
            with open(script_filename, 'w') as f:
                f.write(response_script.text)
            
            print(f"{color.green}  Update completed, you can restart the script.{color.reset}")
            exit(0)
            
        except requests.exceptions.RequestException:
            print(f"{color.red}  [!] Error downloading script. Check {scriptURL}{color.reset}")
        except IOError:
             print(f"{color.red}  [!] Writing error! Check directory permissions.{color.reset}")
    else:
        pass
    

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
        intro()
        print(f"{color.cyan}  Country Code:  {color.gray}{cc}{color.reset}")
        print(f"{color.cyan}  Phone Number:  {color.gray}{pn}{color.reset}")
        print(f"{color.cyan}  Message:  {color.gray}{ms}{color.reset}")
        sel = input(f"\n{color.yellow}  Are you sure (y / n)?  {color.reset}").lower()
        if sel == 'y':
            return True
        elif sel == 'n':
            return False


def sendMessage():
    while True:
        intro()
        countryCode = input(f"{color.cyan}  Country Code:  {color.gray}+{color.reset}")
        if control(countryCode, True):
            break
    countryCode = '+' + countryCode
    while True:
        cls()
        intro()
        print(f"{color.cyan}  Country Code:  {color.gray}{countryCode}{color.reset}")
        phoneNumber = input(f"{color.cyan}  Phone Number:  {color.reset}")
        if control(phoneNumber, False):
            break
    cls()
    intro()
    print(f"{color.cyan}  Country Code:  {color.gray}{countryCode}{color.reset}")
    print(f"{color.cyan}  Phone Number:  {color.gray}{phoneNumber}{color.reset}")
    message = input(f"{color.cyan}  Message:  {color.reset}")
    if not sure(countryCode, phoneNumber, message):
        sendMessage()
    resp = requests.post('https://textbelt.com/text',{
			'phone': countryCode + phoneNumber,
			'message': message,
			'key': 'textbelt' })
    print("\n   ", resp.json())


if not internet():
    print(f"{color.red}  No internet connection!{color.reset}")
    exit()
    

update()
sendMessage()
