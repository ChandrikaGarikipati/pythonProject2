
class Inheritance:
    def __init__(self,first,last):
        self.first=first
        self.last=last

    def display(self):
        print("First name",self.first)
        print("Last name",self.last)

obj=Inheritance("Chandrika","G")
obj.display()