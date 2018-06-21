import csv
from arbfunc import arbfunc
pivotname =[]
pivotprice = []
changername =[]
changerprice = []

###########################################
marketname = []
with open('data/markets', 'r') as marketfold:
    reader = marketfold.readlines()
    i = 0
    for line in reader:
        marketname.append(line)

for i in range(len(marketname)):
    marketname[i] = marketname[i][:-1]
############################################

for i1 in range(len(marketname)-1):
    pivotmarket = marketname[i1]
    with open('data/'+marketname[i1]+'.csv','r') as pivot:
        readpivot = csv.reader(pivot)
        for pivotrow in readpivot:
            try:

                Y = float(pivotrow[2])
                pivotprice.append(Y)
                pivotname.append(pivotrow[1])
            except ValueError:
                print("Not the right format")
                pivotprice.append(0)
                pivotname.append(pivotrow[1])

    #############  Compare pivot with others markets    #######################
        for i2 in range(i1+1,len(marketname)):
            print(marketname[i2])
            with open('data/'+marketname[i2]+'.csv','r') as changer:
                changerreader = csv.reader(changer)
                changemarket = marketname[i2]
                for changerrow in changerreader:
                    try:
                        Y = float(changerrow[2])
                        changerprice.append(Y)
                        changername.append(changerrow[1])
                    except ValueError:
                        print("Not the right format")
                        changerprice.append(0)
                        changername.append(changerrow[1])

                for i in range(len(pivotprice)):
                    for j in range(len(changerprice)):
                        if (pivotname[i] == changername[j]) and ('ETH' in pivotname[i]):
                            arb = arbfunc.checkarb(pivotprice[i],changerprice[j])
                            bigmarket = pivotmarket
                            smallmarket = changemarket
                            if arb > 5 and arb != 100 :
                               if pivotprice[i]<changerprice[j]:
                                    bigmarket = changemarket
                                    smallmarket = pivotmarket
                               print('buy from ',smallmarket,' AND sell to ',bigmarket,' WHAT???: ',pivotname[i],'',changername[j],' because we have arb: ',arb)


