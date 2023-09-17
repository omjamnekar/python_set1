class Student:
    def __init__(self,n,r):
        self.name=n
        self.rno=r
    def division(self):
        if self.rno<80:
            self.div ="A"
        else:
            self.div = "B"
        print("{} is in Division {}".format(self.name,self.div))
    
s1= Student("om",98)
s1.division()

print("_____________")

n= input("Enter your name:")
r =int(input("Enter your roll no:"))
s2 = Student(n,r)

s2.division()
