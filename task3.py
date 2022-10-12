class Product:

    def productInfo(self, pr, desc, dim):
        self.price = pr
        self.description = desc
        self.dimensions = dim

class Customer:

    def customerInfo(self, sur, n, pat):
        self.surname = sur
        self.name = n
        self.patronymic = pat

class Order():

    def __init__(self, someproduct, somecust):
        self.thisproduct = someproduct
        self.thiscust = somecust

    def display(self):
        print(self.thiscust.surname, self.thiscust.name, self.thiscust.patronymic, "has bought",
              self.thisproduct.dimensions, "of", self.thisproduct.description, "for", self.thisproduct.price, "$ each")

    def total(self):
        return self.thisproduct.price * self.thisproduct.dimensions

if __name__ == '__main__':
    newproduct = Product()
    newproduct.productInfo(10, "book", 25)
    newcust = Customer()
    newcust.customerInfo("Vladimirov", "Volodymyr", "Mykolaiovych")
    neworder = Order(newproduct, newcust)
    neworder.display()
    print("Total price is", neworder.total(), "$")
