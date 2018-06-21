class node(object):
    def __init__(self,marketname=None,coinname=None,coinpair=None,price=None,volume=None,nextnode = None):
        self.marketname = marketname
        self.coinname = coinname
        self.coinpair = coinpair
        self.volume = volume
        self.price = price
        self.next = nextnode

    def get_next(self):
        return self.next
    def set_next(self,n):
        self.next = n

    def set_marketname(self,name):
        self.marketname = name
    def get_marketname(self):
        return self.marketname

    def set_coinname(self,name):
        self.coinname = name
    def get_coinname(self):
        return self.coinname

    def set_coinpair(self,name):
        self.coinpair = name
    def get_coinpair(self):
        return self.coinpair

    def set_volume(self,volume):
        self.volume = volume
    def get_volume(self):
        return self.volume

    def set_price(self,price):
        self.price = price
    def get_price(self):
        return self.price


class linked_list(object):
    def __init__(self):
        self.head = node()

    def append(self,market_name,cur_name,cur_pair,price,market_vol):
        new_node = node(market_name,cur_name,cur_pair,price,market_vol)

        new_node.set_next(self.head)
        self.head = new_node

    def searchpair(self,pair):
        current = self.head
        found = False
        while current.next != None:
            if current.get_coinpair()==pair:
                return current
            current = current.next

        return node()

    def next(self,n):

        current = self.head
        for i in range(n):
            current = current.next
        return current

    def length(self):
        cur = self.head
        total = 0
        while cur.next != None:
            cur = cur.next
            total = total + 1
        return total


mylist = linked_list()
mylist.append("market","hello","hello","hello","hello")
mylist.append("hell2o","hel2lo","pair","hell2o","hel2lo")
mylist.append("hell23o","hel2lo","h2ello","hell2o123","hel2lo")
nod = mylist.next(2)

print(nod.get_price())