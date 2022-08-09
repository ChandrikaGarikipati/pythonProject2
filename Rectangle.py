class Rectangle:
    def __init__(self,l,b):
        self.l=l
        self.b=b

    def area(self):
        return (self.l * self.b)


    def Perimeter(self):
        return 2*self.l*self.b
    def carea(r):

        return(3.14*r*r)
    def traingle(l,b,h):
        return(1/2*l*b*h)

obj1 = Rectangle(3, 4)
print("area is:",obj1.area())
print("Perimeter:",obj1.Perimeter())
print("area of circle",Rectangle.carea(4))
print("traingle",Rectangle.traingle(1,2,3))






