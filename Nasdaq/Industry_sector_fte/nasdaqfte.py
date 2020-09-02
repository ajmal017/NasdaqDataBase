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
#******************************************************************************
i=2501
ctr=0
fte=list()
sector=list()
industry=list()
while i<=2829:
#building url***************************************************************
    url="https://finance.yahoo.com/quote/"
    url1=symbol[i]
    url2="/profile?p="
    url3=url+url1+url2+url1
    print(url3)
#***************************************************************************
#Cursor on html**************************************************************
    req = Request(url3, headers={'User-Agent': 'Mozilla/5.0'})
    html = urlopen(req).read()
    soup = BeautifulSoup(html, "html.parser")
#***********************************************************************************
#sector industry fte***************************************************************
    tags= soup('span',{"class":"Fw(600)"})
    if len(tags)==0:
        sector.append("N/A")
        industry.append("N/A")
        fte.append("N/A")

    ctr1=0
    if symbol[i]=="ADGF":
        sector.append("N/A")
        industry.append("N/A")
        fte.append("N/A")
        i+=1
        continue

    for tag in tags:
        y=tag.text
        print(y)
        if ctr1==0:
            sector.append(y)
        elif ctr1==1:
            industry.append(y)
        else:
            if y=='':
                fte.append("N/A")
            else:
                fte.append(y)
        print(ctr1)
        ctr1+=1
    i+=1
    time.sleep(2)

print(sector)
print(industry)
print(fte)
#***************************************************************************************
i=2501
ctr=0
f=open("nasdaqsector.txt","a")
while i<=2829:
    statement=symbol[i]+" "+sector[ctr]
    f.write(statement)
    f.write("\n")
    i+=1
    ctr+=1
f.close()

# i=2501
# ctr=0
# f=open("nasdaqindustry.txt","a")
# while i<=2829:
#     statement=symbol[i]+" "+industry[ctr]
#     f.write(statement)
#     f.write("\n")
#     i+=1
#     ctr+=1
# f.close()

# i=2501
# ctr=0
# f=open("nasdaqfte.txt","a")
# while i<=2829:
#     statement=symbol[i]+" "+fte[ctr]
#     f.write(statement)
#     f.write("\n")
#     i+=1
#     ctr+=1
# f.close()
