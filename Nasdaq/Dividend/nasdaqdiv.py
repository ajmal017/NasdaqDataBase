import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import ssl
import time
import re

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


div=list()
symbol=list()
price=list()

#filling symbol from txt file***************************************************
f=open("nasdaqsymbol.txt")
for line in f:
    sym=line.split()
    symbol.append(sym[0])
#******************************************************************************
i=2501
ctr=0
while i<=2829:
    flag=0
    flagD=0
    flag_div=0

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
        div.append("NA")
        i+=1
        ctr+=1
        continue
#********************************************************************************
#Getting P/E ratio***************************************************************
    if price[ctr]=="NA":
        div.append("(N/A)")
        flag_div=1
    else:
        tags= soup('span' and 'td')
        for tag in tags:
            y=tag.text
            if flagD==1:
                print(y)
                y=y.split()
                print(y[1])
                y=y[1]
                div.append(y)
                flag_div=1
                print("AA")
                break
            if y=='Forward Dividend & Yield':
                flagD=1
    if flag_div==0:
        print("BB")
        div.append("(N/A)")
#********************************************************************************
    print("DIV:"+div[ctr])
    i+=1
    ctr+=1
    time.sleep(3)
print(div)
i=2501
ctr=0
f=open("nasdaqDIV.txt","a")
while i<=2829 :
    statement=symbol[i]+" "+div[ctr]
    f.write(statement)
    f.write("\n")
    i+=1
    ctr+=1
f.close()
