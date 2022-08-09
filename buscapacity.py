class Vehicle:
    def __init__(self,type,company):
        self.type=type
        self.company=company
    def display(self):
        print("type :",self.type)
        print("company :",self.company)
class Bus(Vehicle):
    def seatingcapacity(s):
        return s
print("Seating capacity",Bus.seatingcapacity(50))
obj=Vehicle("Bus","Mahindra")
obj.display()