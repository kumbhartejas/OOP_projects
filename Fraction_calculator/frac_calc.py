class Fraction:
    def __init__(self,n,d):
        self.num = n
        self.den = d
        self.__str__()

    def __str__(self):
        return f"{self.num}/{self.den}"


    def __add__(self,other):
        num=self.num * other.den + other.num * self.den
        den= self.den*other.den
        return Fraction(num,den)

    def __sub__(self,other):
         num=self.num * other.den - other.num * self.den
         den= self.den*other.den
         return Fraction(num,den)

    def __mul__(self,other):
        num=self.num*other.num
        den= self.den*other.den
        return Fraction(num,den)

    def __truediv__(self, other):
     temp_num = self.num * other.den
     temp_den = self.den * other.num
     return Fraction(temp_num, temp_den)

    def __eq__(self,other):
        return self.num * other.den == self.den * other.num

    def __float__(self):
         return self.num / self.den

    def __lt__(self,other):
         return self.num* other.den < self.den *other.num

    def __gt__(self,other):
        return self.num * other.den > self.den * other.num

    def __pow__(self,power):
         return Fraction(self.num ** power, self.den ** power)

     


x=Fraction(3,4)
y=Fraction(5,6)
z=Fraction(7,8)

print(x,y)
print(x + y + z)
print(x-y)
print(x*y)
print(x/y)
print(x==y)
print(float(x))
print(x<y)
print(x>y)
print(x**2)