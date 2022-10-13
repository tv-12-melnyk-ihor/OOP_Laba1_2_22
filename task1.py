class Rectangle:
    def __init__(self, leng = 1.0, wid = 1.0):
        self.length = leng
        self.width = wid

    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, leng):
        if (isinstance(leng, float) == False):
            raise Exception("Length needs to be a float value")
        if (leng <= 0.0 or leng >= 20.0):
            raise Exception("Length needs to be greater than 0.0 but lesser than 20.0")
        self.__length = leng

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, wid):
        if (isinstance(wid, float) == False):
            raise Exception("Width needs to be a float value")
        if (wid <= 0.0 or wid >= 20.0):
            raise Exception("Width needs to be greater than 0.0 but lesser than 20.0")
        self.__width = wid

    def calc_area(self):
        return self.length * self.width

    def calc_perim(self):
        return 2 * (self.length + self.width)

if __name__ == '__main__':
    leng = float(input("Enter the length: "))
    wid = float(input("Enter the width: "))
    #Перевіримо випадок коли ширину не вказано - тоді вона за умовчуванням набуває значення 1.0
    abcd = Rectangle(leng)
    print("The perimeter of your rectangle is", abcd.calc_perim())
    print("The area of your rectangle is", abcd.calc_area())
    #Тепер вкажемо ширину і обчислимо периметр і площу
    defg = Rectangle(leng, wid)
    print("The perimeter of your rectangle is", defg.calc_perim())
    print("The area of your rectangle is", defg.calc_area())

