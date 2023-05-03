
import re
import requests
import threading
import argparse
import sys

def logo():
    print("\n")
    print("\033[5;34;46mKFC-CRAZY-THURSDAY-VME50！\033[0m")
    print("\033[32m"+r"""
___ _ ___ ___ _ _____ _ ____
\ \/// ___\/ ___\/ \ /|/ __// \ / __/\
 \ / | \| \| |_||| \ | | | \/|
 / \ \___ |\___ || | ||| /_ | |_/\| __/
/__/\\\____/\____/\_/ \|\____\\____/\_/                                    
    """+"\033[0m")
    print("\033[5;34;46mKFC-CRAZY-THURSDAY-VME50！\033[0m")





def ddd(url,urlage,semaphore):
    with semaphore:
        at = ""
        at = url+"?"+urlage+"=wa1ki0gwa1ki0gwa1ki0gwa1ki0gwa1ki0gwa1ki0ghhh"
        try:
            text1 = requests.get(at).text
            if "wa1ki0gwa1ki0gwa1ki0gwa1ki0gwa1ki0gwa1ki0ghhh" in text1:
                print("\033[31m [+] \033[0m \033[32m"+str(urlage)+" 参数值被输出在页面   \033[32m",end="")
                print("\033[32m"+url+"?"+urlage+"=xxxxxx"+ "\033[32m")
        except requests.exceptions.RequestException as e:
            print(e)

def att(url,max_threads):
    response = requests.get(url)
    html = response.text
    pattern = r"var\s+(\w+)\s*="
    matches = set(re.findall(pattern, html))
    print("")
    print("\033[32m该页面中共有 %d 个 JavaScript 变量名\033[32m" % len(matches))
    print("")
    semaphore = threading.BoundedSemaphore(max_threads)
    for urlage in matches: 
        t = threading.Thread(target=ddd, args=(url,urlage, semaphore))
        t.start()


if __name__=='__main__':
    logo()
    parser = argparse.ArgumentParser(description='some help')
    parser.add_argument('-u', type=str,help='The target url')
    parser.add_argument('-t', type=int,help='The thread number')
    args = parser.parse_args()
    u = args.u
    t = args.t
    if u==None and t==None:
        print("")
        print("please input url: -u url")
        print("please input thread: -t number")
        sys.exit()
    if u==None:
        print("")
        print("please input url: -u url")
        sys.exit()
    if t==None:
        print("")
        print("please input thread: -t number")
        sys.exit()
    att(u,t)