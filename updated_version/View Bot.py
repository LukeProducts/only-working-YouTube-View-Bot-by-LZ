import os, threading
from selenium import webdriver
from selenium.webdriver.chrome.options import Options  as ChromeOptions
import time
from selenium.webdriver.common.keys import Keys
os.system("color 1")
print("                                                                                                 bbbbbbbb                                \n"
"YYYYYYY       YYYYYYY                                   TTTTTTTTTTTTTTTTTTTTTTT                  b::::::b                                \n"
"Y:::::Y       Y:::::Y                                   T:::::::::::::::::::::T                  b::::::b                                \n"
"Y:::::Y       Y:::::Y                                   T:::::::::::::::::::::T                  b::::::b                                \n"
"Y::::::Y     Y::::::Y                                   T:::::TT:::::::TT:::::T                   b:::::b                                \n"
"YYY:::::Y   Y:::::YYY   ooooooooooo   uuuuuu    uuuuuu  TTTTTT  T:::::T  TTTTTTuuuuuu    uuuuuu   b:::::bbbbbbbbb        eeeeeeeeeeee    \n"
"   Y:::::Y Y:::::Y    oo:::::::::::oo u::::u    u::::u          T:::::T        u::::u    u::::u   b::::::::::::::bb    ee::::::::::::ee  \n"
"    Y:::::Y:::::Y    o:::::::::::::::ou::::u    u::::u          T:::::T        u::::u    u::::u   b::::::::::::::::b  e::::::eeeee:::::ee\n"
"     Y:::::::::Y     o:::::ooooo:::::ou::::u    u::::u          T:::::T        u::::u    u::::u   b:::::bbbbb:::::::be::::::e     e:::::e\n"
"      Y:::::::Y      o::::o     o::::ou::::u    u::::u          T:::::T        u::::u    u::::u   b:::::b    b::::::be:::::::eeeee::::::e \n"
"       Y:::::Y       o::::o     o::::ou::::u    u::::u          T:::::T        u::::u    u::::u   b:::::b     b:::::be:::::::::::::::::e  \n"
"       Y:::::Y       o::::o     o::::ou::::u    u::::u          T:::::T        u::::u    u::::u   b:::::b     b:::::be::::::eeeeeeeeeee   \n"
"       Y:::::Y       o::::o     o::::ou:::::uuuu:::::u          T:::::T        u:::::uuuu:::::u   b:::::b     b:::::be:::::::e            \n"
"       Y:::::Y       o:::::ooooo:::::ou:::::::::::::::uu      TT:::::::TT      u:::::::::::::::uu b:::::bbbbbb::::::be::::::::e           \n"
"    YYYY:::::YYYY    o:::::::::::::::o u:::::::::::::::u      T:::::::::T       u:::::::::::::::u b::::::::::::::::b  e::::::::eeeeeeee   \n"
"    Y:::::::::::Y     oo:::::::::::oo   uu::::::::uu:::u      T:::::::::T        uu::::::::uu:::u b:::::::::::::::b    ee:::::::::::::e  \n"
"    YYYYYYYYYYYYY       ooooooooooo       uuuuuuuu  uuuu      TTTTTTTTTTT          uuuuuuuu  uuuu bbbbbbbbbbbbbbbb       eeeeeeeeeeeeee     ")


print(" .______   ____    ____     __       __    __   __  ___      ___           _______.    ________  \n"
      " |   _  \  \   \  /   /    |  |     |  |  |  | |  |/  /     /   \         /       |   |       /  \n"
      " |  |_)  |  \   \/   /     |  |     |  |  |  | |  '  /     /  ^  \       |   (----`   `---/  /   \n"
      " |   _  <    \_    _/      |  |     |  |  |  | |    <     /  /_\  \       \   \          /  /    \n"
      " |  |_)  |     |  |        |  `----.|  `--´  | |  .  \   /  _____  \  .----)   |        /  /----.\n"
      " |______/      |__|        |_______| \______/  |__|\__\ /__/     \__\ |_______/        /________| ")







num = 1
def start():
    chrome_options = ChromeOptions()
    chrome_options.add_extension('vpn.crx')
    driver = webdriver.Chrome('chromedriver.exe', options=chrome_options)
    time.sleep(30)
    print("Sleeping for 30 secs, now go to the proxy extension, select a country you prefere and click on connect")
    driver.get(url)
    global num
    while True:
        time.sleep(sleeptime)
        driver.refresh()
        time.sleep(sleeptime)
        print("Status:", num, "done")
        num = num + 1
        if num == exittime + 1:
            driver.quit()
            print("Process finsíshed - bye!")
            time.sleep(1)
            break
url = input("put in URL [ENTER = default for YouTube LukeProducts]:\n>> ")
if url == '':
    url = 'https://www.youtube.com/watch?v=AvR4FbzzhJk'
os.system('color 7')

sleeptime = 1
while True:
    sleeptime = input("enter sleeptime [ENTER = default = 0,01 sec.]:\n>> ")
    if sleeptime == '':
        sleeptime = 0.01

    try:
        sleeptime = float(sleeptime)
        break
    except ValueError:
        print("#FALSE ENTRY#")

while True:
    exittime = input("how many tries? [ENTER = default = 1000 tries] :\n>> ")
    if exittime == '':
        exittime = 1000

    try:
        exittime = int(exittime)
        break
    except ValueError:
        print("#FALSE ENTRY#")
while True:
    try:
        threads = int(input("Threads: [be careful, too many threads could trigger thread errors, because of overloaded PCs -> recommended: < 10]\n>> "))
        if threads > 0:
            break
        else:
            print("Thread must be at least 1")
            continue
    except:
        print("No Integer given")
        continue


os.system('color B')
print("NOW PLEASE WAIT [COULD TAKE 1 MINUTE NOW BEFORE STARTING]")



for thread in range(threads):
    threading.Thread(target=start).start()













