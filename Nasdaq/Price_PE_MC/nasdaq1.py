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
i=0
ctr=0
while i<=30:
#for i in range(len(symbol)):
    flag=0
    flag_span=0
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
#Skipping ACTS********************************************************************
    if symbol[i]=="ACTS":
        price.append("NA")
        PEratio.append("NA")
        cap.append("NA")
        i+=1
        ctr+=1
        continue
#*******************************************************************************
#Getting price for stock*************************************************************
    tags= soup('span',{"class":"Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)"})
    for tag in tags:
        y=tag.text
        print("PRICE:"+y)
        if len(y)==0:
            price.append("NA")
        else:
            price.append(y)
        flag=1#check if enters loop
#*********************************************************************************
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
    print("CTR:"+str(ctr))
#Getting P/E ratio***************************************************************
    if price[ctr]=="NA":
        PEratio.append("NA")
    else:
        tags= soup('span',{"data-reactid":"147"})
        for tag in tags:
            print("Y")
            y=tag.text
            print("PE:"+y)
            #contains_digit=re.search('[a-zA-Z]', y)
            contains_digit=y.isalnum()#Ensure number is picked up
            #print(contains_digit)
            #s="," in y
            #print(s)
            #if s=='True':
            #    PEratio.append("NA")
            #else:
            #    print("B")
            #    PEratio.append(y)
            #contains_digit=any(c.isalpha() for c in y)
            print(contains_digit)
            if contains_digit=="True":
                PEratio.append("NA")
            else:
                print("B")
                PEratio.append(y)
            flag_span=1#flag to check if enters this loop

        if flag_span==0:
            tags= soup('tr',{"data-reactid":"147"})#if P/E ratio is stored in another class
            for tag in tags:
                y=tag.text
                split=y.split()
                PEratio.append(split[4])
#*********************************************************************************
    print("PE:"+PEratio[ctr])
    print(PEratio)
#Getting Market Cap***************************************************************
    if price[ctr]=="NA":
        cap.append("NA")
    else:
        tags= soup('span',{"data-reactid":"137"})
        for tag in tags:
            y=tag.text
            cap.append(y)
#*******************************************************************************
    print("CAP:"+cap[ctr])
    i+=1
    ctr+=1
    time.sleep(2)
#f =open("nasdaq3.txt","w")
#statement=equity[i]+" "+symbol[i]+" "+price[i]
#f.write(statement)
#f.write("\n")
#f.close()
print(price)
print(cap)
print(PEratio)
print(range(len(price)))
i=0
ctr=0
f=open("nasdaq4.txt","a")
while i<=30:
#for i in range(len(symbol)):
    print(symbol[i])
    print(price[ctr])
    print(PEratio[ctr])
    print(cap[ctr])
    statement=symbol[i]+" "+price[ctr]+" "+PEratio[ctr]+" "+cap[ctr]
    f.write(statement)
    f.write("\n")
    i+=1
    ctr+=1
f.close()
