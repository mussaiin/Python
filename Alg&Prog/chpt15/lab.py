class Square:
    def __init__(self, h=0):
        self.h=h
    def __str__(self):
        return "%d" % (self.h)
    def __add__(self, a):
        self.h+=a
    def __radd__(self, a):
        return Square.__add__(self, a)
    def __sub__(self, a):
        self.h-=a
    def __mul__(self, a):
        self.h*=a
    def __div__(self, a):
        self.h/=a
    def __lt__(self, other):
        return self.h<other.h
    def __eq__(self, other):
        return self.h==other.h
    def __le__(self, other):
        return self.h<=other.h
    def area(self):
        return self.h**2
    def perimeter(self):
        return self.h*4

class Cube(Square):
    def area(self):
        return (self.h**2)*6
    def perimeter(self, a):
        return self.h*12
    def volume(self):
        return self.h**3
    
s=Square(10)
s2=Square(10)
s*2
print(s)
print(s.perimeter())
print(s.area())

class A:
    def __init__(self, a, b, c):
        self.a=a
        self.b=b
        self.c=c
    def __str__(self):
        return "%s %d %d" % (self.a, self.b, self.c)
a=A('asd', 34, 45)
print(a)

class B(A):
    def __init__(self, a, b, c, d):
        self.d=d
        A.__init__(self, a, b, c)
    def __str__(self):
        return "%s %d %d %s" % (self.a, self.b, self.c, self.d)

print("%s %d %g %.5f" % ('abc', 5, 2.4, 2.4))
