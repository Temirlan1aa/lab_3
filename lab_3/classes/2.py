class Shape():

    def area(self):
        return 0
    

class Square(Shape):

    def __init__(self,length):
        self.length=length

    def area(self):
        return self.length ** 2
    
a = float(input("a:"))

mysquare=Square(a)
print("Area of Sqare:",mysquare.area())

myshape=Shape()
print("drugoe:",myshape.area())