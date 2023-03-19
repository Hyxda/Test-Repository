class Fractions:
    def __init__(self, num = 1, den = 2):
        self.numerator = num
        self.denominator = den

    def __add__(self, other):
        return self.numerator + other.denominator

    def __str__(self):
        return str(f1.numerator) + "/" + str(self.denominator)
    
    def invert(self, other):
        return str(other.denominator) + "/" + str(self.numerator)
    
    def getNumerator(self):
        return self.numerator
    
    def getDenominator(self):
        return self.denominator
    
    def setNumerator(self, num):
        self.numerator = num
    
    def setDenominator(self, den):
        self.denominator = den

f1 = Fractions()
f2 = Fractions()

f1.setNumerator(12)
f2.setDenominator(9)

print(f1.getNumerator())
print(f2.getDenominator())