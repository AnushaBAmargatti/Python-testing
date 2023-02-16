#dynamic binding using super keyword
class constructor:
    def __init__(self,rollno,name,m1,m2,m3):
        self.rollno=rollno
        self.name=name
        self.m1=m1
        self.m2=m2
        self.m3=m3
    def readData(self):
        self.rollno=int(input("enter the number"))
        self.name=input("enter the name")
        self.m1=int(input("enter markls 1"))
        self.m2 = int(input("enter markls 2"))
        self.m3 = int(input("enter markls 3"))
class anusha(constructor):
        def __init__(self,rollno,name,m1,m2,m3,tot,avg):
            super(anusha,self).__init__(rollno,name,m1,m2,m3)
            self.tot = tot
            self.avg=avg
        def calc(self):
            self.tot= self.m1 + self.m2 + self.m3
            self.avg=self.tot/3

        def display(self):
            print(self.rollno,self.name,self.tot,self.avg)
sm1=anusha(11,'an',10,34,23,0,0)
#sm1.readData()
sm1.calc()
sm1.display()

