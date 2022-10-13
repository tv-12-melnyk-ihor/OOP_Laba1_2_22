class BinaryTree:

    def __init__(self):
        self.root = None

    def createnode(self, code, price):
        if (self.root == None):
            self.root = Node(code, price)
        else:
            newnode = Node(code, price)
            self.addnode(self.root, newnode)

    def addnode(self, parentnode, thisnode):
        thisnode.parent = parentnode
        #Якщо буде задано код що належить уже існуючому продукту - тоді просто оновлюємо ціну цього продукту
        if (thisnode.code == parentnode.code):
            parentnode.price = thisnode.price
            return
        #Перевіряємо чи батьківський вузол має дочірні вузли
        if (parentnode.leftbranch == None and parentnode.rightbranch == None):
            #Якщо не має - наш новий вузол стає для нього лівим або правим дочірнім (в залежності від коду продукту)
            if (thisnode.code < parentnode.code):
                parentnode.leftbranch = thisnode
            elif (thisnode.code > parentnode.code):
                parentnode.rightbranch = thisnode
        #Якщо у батьківського вузла вже існують дочірні - шукаємо останній вузол відповідних гілок
        else:
            if (thisnode.code < parentnode.code):
                if (parentnode.leftbranch != None):
                    self.addnode(parentnode.leftbranch, thisnode)
                else:
                    parentnode.leftbranch = thisnode
            elif (thisnode.code > parentnode.code):
                if (parentnode.rightbranch != None):
                    self.addnode(parentnode.rightbranch, thisnode)
                else:
                    parentnode.rightbranch = thisnode

    def displaytree(self, thisnode, level):
        if (thisnode != None):
            self.displaytree(thisnode.leftbranch, level + 1)
            print(' ' * 5 * level + '-> ' + str(thisnode.code) + ' ( ' + str(thisnode.price) + ' $)')
            self.displaytree(thisnode.rightbranch, level + 1)

    def cost(self, thisnode, product, amount):
        if (amount <= 0):
            return 0
        if (thisnode == None):
            return
        elif (thisnode.code != product):
            if (self.cost(thisnode.leftbranch, product, amount) != None):
                return self.cost(thisnode.leftbranch, product, amount)
            if (self.cost(thisnode.rightbranch, product, amount) != None):
                return self.cost(thisnode.rightbranch, product, amount)
        else:
            return thisnode.price * amount


class Node:

    def __init__(self, code, price):
        self.parent = None
        self.leftbranch = None
        self.rightbranch = None
        self.code = code
        self.price = price


mytree = BinaryTree()
mytree.createnode(100, 25)
mytree.createnode(104, 7)
mytree.createnode(184, 8)
mytree.createnode(97, 12)
mytree.createnode(34, 3)
mytree.createnode(56, 50)
mytree.createnode(132, 1)
mytree.createnode(34, 22) #Той самий випадок коли буде задано вже існуючий код - ціна зміниться з 3$ о 22$
mytree.createnode(133, 18)
mytree.createnode(14, 32)
mytree.createnode(101, 11)
mytree.displaytree(mytree.root, 0)
print("\n")
product = int(input("Which product do you want to purchase? "))
amount = int(input("How many of it do you want to purchase? "))
total = mytree.cost(mytree.root, product, amount)
if (total != None):
    print("Your order is", total, "$")
else:
    print("Sorry, we don't have any products with the code", product)




