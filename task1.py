class Rectangle:
    def __init__(self):
        self.length = 1.0
        self.width = 1.0

    @property
    def mylength(self):
        return self.length

    @mylength.setter
    def mylength(self, leng):
        if (isinstance(leng, float) == False):
            raise Exception("Length needs to be a float value")
        if (leng <= 0.0 or leng >= 20.0):
            raise Exception("Length needs to be greater than 0.0 but lesser than 20.0")
        self.length = leng

    @property
    def mywidth(self):
        return self.width

    @mywidth.setter
    def mywidth(self, wid):
        if (isinstance(wid, float) == False):
            raise Exception("Width needs to be a float value")
        if (wid <= 0.0 or wid >= 20.0):
            raise Exception("Width needs to be greater than 0.0 but lesser than 20.0")
        self.width = wid

    def calc_area(self):
        return self.length * self.width

    def calc_perim(self):
        return 2 * (self.length + self.width)

if __name__ == '__main__':
    leng = float(input("Enter the length: "))
    wid = float(input("Enter the width: "))
    abcd = Rectangle()
    abcd.mylength = leng
    abcd.mywidth = wid
    print("The perimeter of your rectangle is", abcd.calc_perim())
    print("The area of your rectangle is", abcd.calc_area())