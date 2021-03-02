import urllib.request
import json

def getList(dict):
    list = []
    for key in dict.keys():
        list.append(key)

    return list

def price(symbol, comparison_symbols=["EUR"]):
    url = 'https://min-api.cryptocompare.com/data/price?fsym={}&tsyms={}&e=CCCAGG'\
            .format(symbol.upper(), ','.join(comparison_symbols).upper())
    r=urllib.request.urlopen(url)
    html=r.read()
    html=html.decode()
    d=json.loads(html)
    return d

file = input("Enter the file location of your portofolio:")
f = open(file,'r')
f = f.read()
f = json.loads(f)
x=getList(f)
temp={}
for i in x:
    temp1 = price(i)
    temp[i] = temp1["EUR"]*f[i]
print('Your portofolio is:')
print(f)
print('Which in Euros is: ')
print(temp)
