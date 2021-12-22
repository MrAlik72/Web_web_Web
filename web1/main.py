class Rect():

    total_area = 0

    def __init__(self, a, b):
        self.a = a
        self.b = b
        Rect.total_area += self.area(a, b)

    @staticmethod
    def area(a, b):
        return a * b

    @classmethod
    def all_area(cls):
        print(cls.total_area)
        

class Square(Rect):
    def __init__(self, a):
        super().__init__(a, a)
    


r1 = Rect(2, 5)
r2 = Rect(3, 2)
s1 = Square(2)
s2 = Square(5)

print(Rect.area(4, 2))
Rect.all_area()