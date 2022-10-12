from fractions import Fraction

class Rational:

    def __init__(self, num=1, den=1):
        if (isinstance(num, int) == False):
            raise Exception("The numerator has to be an integer value")
        if (isinstance(den, int) == False):
            raise Exception("The denominator has to be an integer value")
        self.numer = Fraction(num, den).numerator
        self.denom = Fraction(num, den).denominator

    def myfrac(self):
        return Fraction(self.numer, self.denom)

    def myfloat(self):
        return self.numer/self.denom

if __name__ == '__main__':
    newfrac1 = Rational(5, 30)
    print(newfrac1.myfrac())
    print(newfrac1.myfloat(), "\n")
    newfrac2 = Rational(7)
    print(newfrac2.myfrac())
    print(newfrac2.myfloat(), "\n")
    newfrac3 = Rational(8, 12)
    print(newfrac3.myfrac())
    print(newfrac3.myfloat())