import requests
import csv
from bs4 import BeautifulSoup
from arbfunc import quotes,iswordnum

def getData():
    marketname = []
    link = 'https://coinmarketcap.com/exchanges/'
    with open('data/markets', 'r') as marketfold:
        reader = marketfold.readlines()
        for line in reader:
            marketname.append(line)
    for i in range(len(marketname)):
        marketname[i] = marketname[i][:-1]
    ############################################
    print(marketname)
    for i in range(len(marketname)):

        r = requests.get(link + marketname[i])

        asoup = BeautifulSoup(r.content, "lxml")
        table = asoup.find("tbody")
        names = table.find_all("a", {"class": "market-name"})
        pairs = table.find_all("a", {"target": "_blank"})
        price = table.find_all("span", {"class": "price"})

        volume = table.find_all("span",{"class":"volume"})
        #print("ok")
        with open('data/' + marketname[i] + '.csv', 'w', newline='') as file:
            thewriter = csv.writer(file)
            for i in range(len(names)):
               #
               #  print(iswordnum(names[i].text), iswordnum(pairs[i].text), iswordnum(price[i].text),iswordnum(volume[i].text))
                thewriter.writerow([iswordnum(names[i].text), iswordnum(pairs[i].text), iswordnum(price[i].text),iswordnum(volume[i].text)])

    print("Got the data.")
