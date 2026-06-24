# class aand object 
# Python constructor is an instance method in a class, that is automatically called whenever a new object of the class is created. The constructor's role is to assign value to instance variables as soon as the object is declared.

class students:
    # print("Hello this is students class")
    # def __init__(self,n,r):
    #     # print("this is constructor")
    #     self.naam=n 
    #     self.roll=r
    #     # naam=n 
    #     # roll=r
    #     # print(f"name is {self.naam} and roll is {self.roll} ")
    def __init__(self):
        pass
    def getValues(self):
        self.name= input("Enter your name ")
        self.rollno= input("Enter your rollnumber ")
    def printVal(self):
        print(f"name is {self.name} and roll is {self.rollno}")
        
        
        
# stu1= students()
# stu1= students('Jaskaran',12)
# # print(stu1)
# stu2= students('Mohit',34)

# stu1.printVal()


stu1= students()
stu1.getValues()

stu2= students()
# stu2.getValues()


# stu2.printVal()