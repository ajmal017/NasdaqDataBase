import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import ssl
import time
import re
from re import search

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

symbol=list()

#filling symbol from txt file***************************************************
f=open("nasdaqsymbol.txt")
for line in f:
    sym=line.split()
    symbol.append(sym[0])
#******************************************************************************

i=2501
ctr=0
ceo=list()
ceosalary=list()
phone=list()
while i<=2829:
#building url***************************************************************
    url="https://finance.yahoo.com/quote/"
    url1=symbol[i]
    url2="/profile?p="
    url3=url+url1+url2+url1
    print(url3)
    print(url1)
#***************************************************************************
#Cursor on html**************************************************************
    req = Request(url3, headers={'User-Agent': 'Mozilla/5.0'})
    html = urlopen(req).read()
    soup = BeautifulSoup(html, "html.parser")
#***********************************************************************************
#ceo***************************************************************************
    tags= soup('span')
    x=""
    flagceo=0
    ctrceo=1
    for tag in tags:
        #print("a")
        y=tag.text
        substring="CEO"
        # if ctrceo==4:
        #     print("D")
        #     print(y)
        #     break
        # if ctrceo==3:
        #     print("A")
        #     print(len(y))
        #     ctrceo+=1
        if ctrceo==2:
            print("c")
            print(y)
            ceosalary.append(y)
            ctrceo+=1
            break
        if search(substring, y):
            print("b")
            flagceo=1
            ceo.append(x)
            print(x)
            print(y)
            ctrceo+=1
        # if flagceo==0:
        #     print("c")
        #     ceo.append("NA")
        x=y
    if flagceo==0:
        ceo.append("N/A")
        ceosalary.append("N/A")
    print(i)
    i+=1
    time.sleep(5)
print(ceo)
print(ceosalary)

i=2501
ctr=0
f=open("nasdaqceo.txt","a")
while i<=2829:
    statement=symbol[i]+" "+ceo[ctr]+" "+ceosalary[ctr]
    f.write(statement)
    f.write("\n")
    i+=1
    ctr+=1
f.close()
