def arbfunc(a, b):
    if a == b == 0 : return(0)
    return (max(a,b)-min(a,b))/max(a,b)*100


######################################################
def is_number(char):
    if char >= "0" and char <= "9":
        return True
    return False


def find_dot(num):
    for i in range(len(num)):
        if num[i] == ".":
            return i
    return 0

def atof(num):
    dot = find_dot(num)
    if dot == 0:
        print("Cant get the number in atof")
        return -1
    length = len(num)
    pow = 1
    number = 0
    dot = dot -1
    while (dot>=0 and is_number(num[dot])):
        number += float(num[dot])*pow
        pow = pow*10
        dot = dot -1
    dot = find_dot(num)
    pow = 10
    dot = dot + 1
    while (dot < length and is_number(num[dot])):
        number += float(num[dot])/pow
        pow = pow*10
        dot = dot + 1
    return number


def atoi(num):
    b=0
    for i in range(len(num)):
        if num[i]<="9" and num[i]>="0":
            b= b*10 + int(num[i])
    return b


###########################################################################################
import linkedlist as l
import winsound
def checkArb():
    import csv


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
    for i1 in range(len(marketname) - 1):
        pivotmarket = marketname[i1]
        pivotlist = l.linked_list()
        with open('data/' + marketname[i1] + '.csv', 'r') as pivot:
            readpivot = csv.reader(pivot)
            for pivotrow in readpivot:
                pivotlist.append(pivotmarket,pivotrow[0],pivotrow[1],atof(pivotrow[2]),atoi(pivotrow[3]))
                    #############  Compare pivot with others markets    #######################
            for i2 in range(i1 + 1, len(marketname)):
               #F print(marketname[i2])
                with open('data/' + marketname[i2] + '.csv', 'r') as changer:
                    changerreader = csv.reader(changer)
                    changemarket = marketname[i2]
                    changelist = l.linked_list()
                    for changerrow in changerreader:
                        changelist.append(changemarket,changerrow[0],changerrow[1],atof(changerrow[2]),atoi(changerrow[3]))
                        #changelist.append(changemarket,changerrow[0],changerrow[1],atof(changerrow[2]),atoi(changerrow[3]))
                    currentpivot =  pivotlist.head
                    for i in range(pivotlist.length()):
                        currentpivot = pivotlist.next(i)
                        currentchange = changelist.head
                        for j in range(changelist.length()):
                            currentchange = changelist.next(j)
                            pivotpair = currentpivot.get_coinpair()
                            changepair = currentchange.get_coinpair()
                            if (pivotpair == changepair) :
                                arb = arbfunc(currentpivot.get_price(), currentchange.get_price())
                                bigmarket = currentpivot.get_marketname()
                                smallmarket = currentchange.get_marketname()
                                if arb > 2 and arb<40 and currentchange.get_volume()>5000 and currentpivot.get_volume() > 5000 and currentchange.get_price()<1 and currentpivot.get_price()<1:

                                    if currentpivot.get_price() < currentchange.get_price():
                                        pivotmarket = bigmarket
                                        bigmarket = changemarket
                                        smallmarket = pivotmarket
                                    #if smallmarket =='kucoin':
                                     #   winsound.PlaySound('sound.wav', winsound.SND_FILENAME)
                                    print('Buying Market: ', smallmarket, '   Selling Market: ', bigmarket, '   CoinPair: ',
                                            currentpivot.get_coinpair(),  '   with profit: ', arb)





def quotes(a):
    if a[0]==a[-1]=='"': return a[1:-1]
    return a

def iswordnum(a):
    b =""
    for i in range (len(a)):
        if (a[i]<="Z" and a[i]>="A"): b += a[i]
        if(a[i]<="n" and a[i]>="a"): b += a[i]
        if (a[i]==" ") or (a[i]=="-")or (a[i]=="/")or (a[i]=="."): b += a[i]
        if (a[i]>="0" and a[i]<="9"): b += a[i]
    return b

