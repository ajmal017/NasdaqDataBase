import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import ssl
import time

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

equity=list()
symbol=list()
for letter in ["A","B","C","D","E","F","G",'H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',"0"]:#filling from equity and symbol
    url="https://www.advfn.com/nasdaq/nasdaq.asp?companies="
    url1=url+letter
    req = Request(url1, headers={'User-Agent': 'Mozilla/5.0'})
    html = urlopen(req).read()
    soup = BeautifulSoup(html, "html.parser")

    ctr=0
    tags= soup('a')
    for tag in tags:
        ctr+=1
        if ctr<=34:
            continue
        y=tag.text
        x="Terms & Conditions"
        if y==x:
            break
        if(len(y)==0):
            continue
        if ctr%2==0:
            symbol.append(y)
        else:
            equity.append(y)

#f =open("nasdaq.txt","w")
#print(range(len(equity)))
#for i in range(len(equity)):
#    f.write(equity[i])
#    f.write("\n")
#f.close()

f =open("nasdaqsymbol.txt","w")
print(range(len(equity)))
for i in range(len(equity)):
    f.write(symbol[i]+" ")
    f.write("\n")
f.close()
