import sqlite3

equity=list()
symbol=list()
price=list()
peratio=list()
marketcap=list()
div=list()
ceo=list()
ceosalary=list()
phone=list()
domain=list()
address=list()
fte=list()
sector=list()
industry=list()
# f=open("nasdaqaddress1.txt","w")

# f=open("nasdaq1.txt")
f=open("C:/Users/siddc/OneDrive/Desktop/py4e/nasdaq1.txt")
for line in f:
    eq=line.split()
    statement=' '.join(eq[:-1])
    equity.append(statement)
f.close()
print(equity)
print(len(equity))

f=open("C:/Users/siddc/OneDrive/Desktop/py4e/nasdaq1.txt")
for line in f:
    sy=line.split()
    statement=sy[-1]
    symbol.append(statement)
f.close()
print(symbol)
print(len(symbol))

f=open("C:/Users/siddc/OneDrive/Desktop/py4e/P_PE_MC.txt")
for line in f:
    p=line.split()
    statement=p[1]
    price.append(statement)
    statement=p[2]
    peratio.append(statement)
    statement=p[3]
    marketcap.append(statement)
f.close()
print(len(price))
print(len(peratio))
print(len(marketcap))

f=open("C:/Users/siddc/OneDrive/Desktop/py4e/nasdaqDIV.txt")
for line in f:
    d=line.split()
    statement=d[-1]
    div.append(statement)
f.close()
print(div)
print(len(div))

f=open("C:/Users/siddc/OneDrive/Desktop/py4e/nasdaqceo.txt")
for line in f:
    d=line.split()
    statement=' '.join(d[1:-1])
    ceo.append(statement)
    statement=d[-1]
    ceosalary.append(statement)
f.close()
print(ceo)
print(ceosalary)
print(len(ceo))
print(len(ceosalary))

f=open("C:/Users/siddc/OneDrive/Desktop/py4e/nasdaqnumber.txt")
for line in f:
    d=line.split()
    statement=' '.join(d)
    phone.append(statement)
f.close()
print(phone)
print(len(phone))

f=open("C:/Users/siddc/OneDrive/Desktop/py4e/nasdaqmail.txt")
for line in f:
    d=line.split()
    statement=' '.join(d)
    domain.append(statement)
f.close()
print(domain)
print(len(phone))

f=open("C:/Users/siddc/OneDrive/Desktop/py4e/nasdaqaddress1.txt")
for line in f:
    d=line.split()
    statement=' '.join(d)
    address.append(statement)
f.close()
print(address)
print(len(address))

f=open("C:/Users/siddc/OneDrive/Desktop/py4e/nasdaqfte.txt")
for line in f:
    d=line.split()
    statement=d[1]
    fte.append(statement)
f.close()
print(len(fte))

f=open("C:/Users/siddc/OneDrive/Desktop/py4e/nasdaqsector.txt")
for line in f:
    d=line.split()
    statement=' '.join(d[1:])
    sector.append(statement)
f.close()
print(sector)
print(len(sector))

f=open("C:/Users/siddc/OneDrive/Desktop/py4e/nasdaqindustry.txt")
for line in f:
    d=line.split()
    statement=' '.join(d[1:])
    industry.append(statement)
f.close()
print(industry)
print(len(industry))

conn = sqlite3.connect('nasdaqDB.sqlite')
cur = conn.cursor()
# cur.execute('DROP TABLE IF EXISTS Company')

cur.executescript('''
DROP TABLE IF EXISTS Company;

CREATE TABLE Company (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    Equity TEXT,
    Symbol TEXT,
    Price  BLOB,
    PE  BLOB,
    Market_Cap BLOB,
    Dividend_Yield BLOB,
    CEO BLOB,
    CEO_Salary BLOB,
    Phone BLOB,
    Domain BLOB,
    Address BLOB,
    FTE BLOB,
    Sector BLOB,
    Industry BLOB
);
''')

i=0
while i<=2829:
    eq=equity[i]
    sy=symbol[i]
    p=price[i]
    pe=peratio[i]
    mc=marketcap[i]
    dividend=div[i]
    ceo_name=ceo[i]
    ceo_sal=ceosalary[i]
    number=phone[i]
    domain_name=domain[i]
    add=address[i]
    ftemployee=fte[i]
    sec=sector[i]
    ind=industry[i]
    print("A")
    print(sy)
    i+=1
    print(i)
    cur.execute('''INSERT OR IGNORE INTO Company
        (Equity, Symbol, Price, PE, Market_Cap,Dividend_Yield,CEO,CEO_Salary,Phone,Domain,Address,FTE,Sector,Industry)
        VALUES ( ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
        ( eq, sy, p, pe, mc, dividend, ceo_name, ceo_sal, number, domain_name, add, ftemployee, sec, ind) )

conn.commit()
