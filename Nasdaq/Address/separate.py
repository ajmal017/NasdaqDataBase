import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import ssl
import time
import re
from re import search

# mail=list()
# #filling email from txt file***************************************************
# f=open("nasdaqaddress.txt")
# for line in f:
#     m=line.split()
#     if m[1]=='N/A':
#         mail.append("N/A")
#     else:
#         mail.append(m[-1])
# f.close()
# print(mail)
# #******************************************************************************
number=list()
address=list()
#filling address from txt file***************************************************
f=open("nasdaqaddress.txt")
for line in f:
    i=-2
    num=" "
    a=line.split()
    if a[1]=='N/A':
        number.append("N/A")
        address.append("N/A")
        continue
    while 5==5:
        if  a[i].isdigit():
            num=a[i]+num
            i-=1
        else:
            break
    number.append(num)
    i+=1
    x=a[1:i]
    address.append(x)
f.close()
#***********************************************************************************
# i=0
# f=open("nasdaqmail.txt","a")
# while i<=2829:
#     statement=mail[i]
#     f.write(statement)
#     f.write("\n")
#     i+=1
# f.close()
print("A")
i=0
f=open("nasdaqnumber.txt","w")
while i<=2829:
    statement=number[i]
    f.write(statement)
    f.write("\n")
    i+=1
f.close()

i=0
f=open("nasdaqaddress1.txt","w")
while i<=2829:
    statement=' '.join(address[i])
    f.write(statement)
    f.write("\n")
    i+=1
f.close()
