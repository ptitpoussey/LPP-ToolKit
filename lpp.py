#!/bin/python3
#!/user/bin/python
#Importations des modules
import sys  # fonctions et paramètres systèmes
from datetime import datetime as dt
import random
import os #for clear function and paths
import nmap
import ctypes
import subprocess
import requests
import re
import os.path
import urllib.request


# Make a regular expression for validating an Ip-address
regex = "^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"
 

class color:
    HEADER = '\033[95m'
    IMPORTANT = '\033[35m'
    NOTICE = '\033[33m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033|92m'
    WARNING = '\033[93m'
    RED = '\033[91m'
    END = '\033|8m'
    LOGGING = '\033[34m'

random_color =[color.HEADER,color.IMPORTANT,color.NOTICE,color.OKBLUE,color.OKGREEN,color.WARNING,color.RED,color.END,color.LOGGING]
text_menu = '''
    ╔========================================================================================================╗
    ╟                                                                                                        ╟
    ╟                                                                                                        ╟
    ╟              PPPPPPP               PPPPPPPPPPP     PPPPPPPPPPP                                         ╟
    ╟              PLLLLLP               PLLLLLLLLLLP    PLLLLLLLLLLP                                        ╟
    ╟              PLLLLLP               PLLL     LLLP   PLLL     LLLP                                       ╟
    ╟              PLLLLLP               PLLL     LLLLP  PLLL     LLLLP                                      ╟
    ╟              PLLLLLP               PLLLLLLLLLLLP   PLLLLLLLLLLLP                                       ╟
    ╟              PLLLLLP               PLLLLLPPPPPP    PLLLLLPPPPPP                                        ╟
    ╟              PLLLLLP               PLLLLLP         PLLLLLP                                             ╟
    ╟              PLLLLLP               PLLLLLP         PLLLLLP                                             ╟
    ╟              PLLLLLP               PLLLLLP         PLLLLLP                                             ╟
    ╟              PLLLLLPPPPPPPPPPPPP   PLLLLLP         PLLLLLP                                             ╟
    ╟              PLLLLLLLLLLLLLLLLLP   PLLLLLP         PLLLLLP           .....   .....   .....             ╟
    ╟              PLLLLLLLLLLLLLLLLLP   PLLLLLP         PLLLLLP           .....   .....   .....             ╟
    ╟              PPPPPPPPPPPPPPPPPPP   PPPPPPP         PPPPPPP           .....   .....   .....             ╟
    ╟                                                                                                        ╟
    ╟                                                                                                        ╟
    ╟  ©LєƤтιтƤσυcєт                                                                                         ╟
    ╚========================================================================================================╝              '''



def sudo_access():
    if os.geteuid() != 0:
        print("You need to have root privileges to continue.")
        sys.exit(0)
    
    #Add an help option like --help

def test1():
    scan=nmap.PortScanner()
    #os.system('cls' if os.name == 'nt' else 'clear')
    host=input("Enter IP | DNS : ")
    #test_up(host)
    scan.scan(host, '1-65535' ,'-v -sS -sV -sC -A -O')
    scan.command_line()
    scan.scaninfo()
    for host in scan.all_hosts():
        print('........L...........................P...................................P...........................')
        print ('Host: %s(%s)' % (host, scan[host].hostname()))
        print ('State: %s' % scan[host].state())
        for proto in scan[host].all_protocols():
            print('........')
            print ('Protocol: %s' % proto)
            lport = scan[host][proto].keys()
            sorted(lport)
            for port in lport:
                print('port: %s\tstate: %s' % (port, scan[host][proto][port]['state']))

def test_up(ip):
    
    if(re.search(regex, ip)):
        if not (os.path.exists("scan_result.txt")):
            os.system("touch scan_result.txt")
        else:
            os.system("rm scan_result.txt;touch scan_result.txt")

    else:
        print("Invalid Ip address")
        sys.exit(0)






def request(url):
        try:
            return requests.get("http://" + url)
        except requests.exceptions.ConnectionError:
            print("Error: Can't connect to website!")
            if os.path.exists('dir_result.txt'):
                os.system('rm dir_result.txt')
                sys.exit(0)
            else:
                sys.exit(0)

def test3():
    i=1
    os.system('cls' if os.name == 'nt' else 'clear')
    host=input("Enter IP | DNS <<|http://| not needed>>: ")
    check_dns=request(host)
    print("######   If you want to add your own file, put it in the folder [dir_list] ######")
    os.system('cd dir_list && ls | tr " " "\n" | tr ".txt" " "')
    dir_file =input("Choose a fuzz's file between this ones : ")
    # test if the file enter is in the folder
    dir_file=dir_file+".txt"
    os.system('touch dir_result.txt')
    #try to found a way to display the number of tests like if we have 100 words in the wordlist, it display X/100
    f = open('dir_result.txt', 'w')
    while (not(os.path.isfile("dir_list/"+dir_file))):
        print("The file entered do not exist!!")
        print("Try again... :")
        os.system('cd dir_list && ls | tr " " "\n" | tr ".txt" " "')
        dir_file =input("Choose a fuzz's file between this ones : ")
        dir_file+="txt"
        f=open("dir_list/"+dir_file, 'r')
        NumberOfLine = 0
        for line in f:
           NumberOfLine += 1
    if os.path.exists("dir_list/"+dir_file):
        file = open("dir_list/"+dir_file)
        for lines in file:
            word=lines.strip()
            url=host+"/"+word
            response=request(url)
            if response:
                i=1
                print("==============================================================================")
                print("["+ i++ +"/"+NumberOfLine+"]"+"A directory has been found here: "+url)
                f.write(str(url+"\n"))
        print("====================================================================================")
        file.close()
        f.close()
    else:
        print("/!\ The Website Is Not Up /!\ ")


os.system('cls' if os.name == 'nt' else 'clear')
ch = True
while ch:
    random.shuffle(random_color)
    text_menu = text_menu + random_color[0]
    print(text_menu)
    print("""
        1. IP Full Analyze
        2. SQL Injections Tests
        3- Find hiddens URL's
        4- Leave Program
            """)
    selection=input("Select a choice : ")
    if selection=='1':
        sudo_access()
        test1()
    elif selection=='2':
        pass
        #options2
    elif selection=='3':
        test3()
        #options3
    elif selection=='4':
        break
    else:        
        print("Unknown choice.")

