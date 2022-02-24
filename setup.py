#!/bin/env python3
# code by : Termux Professor

"""

you can re run setup.py 
if you have added some wrong value

"""
import os, sys
import configparser
re="\033[0;31m"
gr="\033[1;32m"
cy="\033[1;36m"
bl="\033[0;30m"
wh="\033[0;37m"
def banner():
	os.system('clear')
	print(f"""
	{wh}╔═╗{re}┌─┐┌┬┐┬ ┬┌─┐
	{re}╚═╗{wh}├┤  │ │ │├─┘
	{wh}╚═╝{re}└─┘ ┴ └─┘┴
	
	           Version : 2.0
	{wh}Follow my repo on Github
	{re}github.com/ixmazecoX
	""")
banner()
print(re+"[+] Request API ID & HASH at : ") 
print(wh+"[+] my telegram.org") 
print(gr+"[+] Installing requierments ...")
os.system('python3 -m pip install telethon')
os.system('pip3 install telethon')
banner()
os.system("touch config.data")
cpass = configparser.RawConfigParser()
cpass.add_section('cred')
xid = input(gr+"[+] masukkan API ID : "+re)
cpass.set('cred', 'id', xid)
xhash = input(gr+"[+] masukkan HASH ID : "+cy)
cpass.set('cred', 'hash', xhash)
xphone = input(gr+"[+] masukkan nombor fon : "+wh)
cpass.set('cred', 'phone', xphone)
setup = open('config.data', 'w')
cpass.write(setup)
setup.close()
print(gr+"[+] setup complete !")
print(gr+"[+] now you can run any tool !")
print(gr+"[+] RabbitX")
print(gr+"[+] https://github.com/ixmazecoX")
