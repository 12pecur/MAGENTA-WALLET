import requests
import urllib 
import re
import cprint 
from termcolor import colored, cprint
import time

print(colored('=================================================================================================================', 'dark_grey'))
print(colored('-----------------------------------------------------------------------------------------------------------------', 'light_magenta'))

print(colored(u'\u2666'*9 + '      ' + u'\u2666'*9 +'      ' + u'\u2666' +'       ' + u'\u2666' +'      '+ '(c)2024 MAGENTA WALLET V.1.0.', 'magenta'))
print(colored(u'\u2666'+ '                  ' + u'\u2666' +'          ' + u'\u2666' + '       ' + u'\u2666'+'      '+ 'All RIGHTS RESERVED.'+ u'\u2713','magenta'))
print(colored(u'\u2666'+ '                  ' + u'\u2666' +'          ' + u'\u2666' +'       ' + u'\u2666'+'      '+ 'DONATE:0X0000FFF02034029400302', 'magenta'))
print(colored(u'\u2666'*9+ '          ' + u'\u2666' + '          ' + u'\u2666'*9 + '          ', 'magenta'))
print(colored(u'\u2666'+ '                  ' + u'\u2666' +'          ' + u'\u2666' + '       ' + u'\u2666', 'magenta'))
print(colored(u'\u2666'+ '                  ' + u'\u2666' +'          ' + u'\u2666' + '       ' + u'\u2666', 'magenta'))
print(colored(u'\u2666'*9+ '          ' + u'\u2666' + '          ' + u'\u2666' + '       ' + u'\u2666' + '        ','magenta'))

print('\n')

wallet = input(str(colored('Enter Ethereum adress: ','dark_grey')))
print('\n')
try:
   page = urllib.request.urlopen('https://api.etherscan.io/api?module=account&action=balancemulti&address='+wallet)
   contents = page.read()
   lines = str(contents)
   items = re.findall('"balance.*$',lines,re.MULTILINE)

   for x in items:
       x = x[:-4]
       x = str(x)
   items = re.findall('"account.*$',lines,re.MULTILINE)
   for y in items:
       y = y[:-40]
       y = str(y)
   page = urllib.request.urlopen('https://api.ethplorer.io/getTokenHistory/'+wallet+'?apiKey=freekey&type=transfer&limit=1')
   contents = page.read()
   lines = str(contents)
   items2 = re.findall('"from".*$',lines,re.MULTILINE)
   for z in items2:
       z = z[:-4]
       z = str(z)
   items2 = re.findall('"transfer.*$',lines,re.MULTILINE)
   for a in items2:
       a = a[:-121]
       a = str(a)
   print(colored("Network Status: " + u'\u2713', 'green'))
   print('\n')
   print(colored(u'\u2666'+'ETH: '+x, "magenta"))
   print(colored(u'\u2666'+'ETH: '+y, "magenta"))
   print(colored(u'\u2666'+'ETH: '+z, "magenta"))
   print(colored(u'\u2666'+'ETH: '+a, "magenta"))
   print('\n')
   print(colored('-----------------------------------------------------------------------------------------------------------------', 'light_magenta'))
   print(colored('=================================================================================================================', 'dark_grey'))

except:
    print(colored("Network Status: " + u'X', 'red'))
    print(colored('-----------------------------------------------------------------------------------------------------------------', 'light_magenta'))
    print(colored('=================================================================================================================', 'dark_grey'))




