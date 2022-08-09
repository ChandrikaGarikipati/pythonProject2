class Ticket:
    def __init__(self,people,name, doj,gender,age):
        self.people=people
        self.name = name
        self.doj = doj
        self.gender=gender
        self.age = age

    def display(self):
         self.people=int(input("Enter Number Of People: "))
         for i in range(1, self.people + 1):
          self.name=input("Enter Name Of The Passenger: ")
          self.doj =input("Enter The Date Of Journey: ")
          self.gender=input("Male OR Female: ")
          self.age=int(input("Enter The Age Of Passenger: "))
          if (self.age)<4:
            print("Ticket not required")
          print(" No.of people      : ",self.people,"\n","Name Of Passenger : ",self.name,"\n","Date Of Journey   : ",self.doj,"\n","Male OR Female    : ",self.gender,"\n","Age Of Passenger  : ",self.age)
obj=Ticket(" "," "," "," "," ")
obj.display()
print("Tickets Booked")


