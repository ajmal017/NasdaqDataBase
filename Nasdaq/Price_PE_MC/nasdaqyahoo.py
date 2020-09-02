import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import ssl
import time
import re

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

price=list()
cap=list()
PEratio=list()
symbol=list()
#filling symbol from txt file***************************************************
f=open("nasdaqsymbol.txt")
for line in f:
    sym=line.split()
    symbol.append(sym[0])
#******************************************************************************
i=2751
ctr=0
while i<=2829:
#for i in range(len(symbol)):
    flag=0
    flagMC=0
    flagPE=0
    flag_market=0
    flag_pe=0
#building url***************************************************************
    url="https://finance.yahoo.com/quote/"
    url1=symbol[i]
    url2="?p="
    url3=url+url1+url2+url1
    print(url3)
#***************************************************************************
#Cursor on html**************************************************************
    req = Request(url3, headers={'User-Agent': 'Mozilla/5.0'})
    html = urlopen(req).read()
    soup = BeautifulSoup(html, "html.parser")
#***********************************************************************************
#Getting price for stock*************************************************************
    tags= soup('span',{"class":"Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)"})
    for tag in tags:
        y=tag.text
        print("PRICE:"+y)
        if len(y)==0:
            price.append("NA")
        else:
            price.append(y)
        flag=1
#*********************************************************************************
    print("CTR:"+str(ctr))
#if there is no information and doesnt enter loop above*****************************
    if flag==0:
        print("A")
        price.append("NA")
        PEratio.append("NA")
        cap.append("NA")
        i+=1
        ctr+=1
        continue
#********************************************************************************
    print("Price:"+price[ctr])
    if price[ctr]=="NA":
        cap.append("NA")
        flag_market=1
    else:
        tags= soup('span')
        for tag in tags:
            y=tag.text
            if flagMC==1:
                print(y)
                cap.append(y)
                flag_market=1
                print("AA")
                break
            if y=='Market Cap':
                flagMC=1
    if flag_market==0:
        print("BB")
        cap.append("NA")
#*******************************************************************************
    print("CAP:"+cap[ctr])
#Getting P/E ratio***************************************************************
    if price[ctr]=="NA":
        PEratio.append("NA")
        flag_pe=1
    else:
        tags= soup('span')
        for tag in tags:
            y=tag.text
            if flagPE==1:
                print(y)
                PEratio.append(y)
                flag_pe=1
                print("AA")
                break
            if y=='PE Ratio (TTM)':
                flagPE=1
    if flag_pe==0:
        print("BB")
        PEratio.append("NA")

    print("PE:"+PEratio[ctr])
#******************************************************************************
    i+=1
    ctr+=1
print(price)
print(cap)
print(PEratio)
i=2751
ctr=0
f=open("nasdaq4.txt","a")
while i<=2829:
    statement=symbol[i]+" "+price[ctr]+" "+PEratio[ctr]+" "+cap[ctr]
    f.write(statement)
    f.write("\n")
    i+=1
    ctr+=1
f.close()
