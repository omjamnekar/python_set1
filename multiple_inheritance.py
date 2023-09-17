class Basic:
    n=0
    def value1(self):
        self.n =int(input('Enter a number1:'))

class Aclass:
    m = 0
    def value2(self):
        self.m =int(input('Enter a number2:'))

        
class Bclass(Aclass,Basic):
    num = 0
    def sumup(self):
        num =self.n+self.m
        return num

    
n = Bclass()

n.value1()
n.value2()
print(n.sumup())
