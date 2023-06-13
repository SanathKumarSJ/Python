'''class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def dis(self):
        print("Name",self.name)
        print("Age",self.age)
c1=person(input("enter the name"),int(input('enter the age')))
c1.dis()
c2=person(input("enter the name"),int(input('enter the age')))
c2.dis()'''

'''class called bank, with account and menthod to add and remove account and to deposit and withdraw money
from lib2to3.pgen2.token import NUMBER
import numbers
import pandas as pd
from os import name


arr=[]
for i in range (0,2,1):
    class bank:
        def createacc(self):
            self.accn=int(input("enter the account number "))
            self.accnm=input("enter the account name ")
            self.add=int(input("The money added "))
            self.wd=int(input("The money withdraw "))
            self.bal=self.add-self.wd
        def balance(self):
            if self.bal<500:
                print("The balance amount is not sufficient for withdraval")
            else:
                print("Amount can be withdraw")
        def dis(self):
            print("Acc num",self.accn)
            print("Acc name",self.accnm)
            print("depositted amount",self.add)
            print("withdraw",self.wd)
            print("Balance",self.bal)
            arr.append(self.accn)
            arr.append(self.accnm)

    c1=bank()
    c1.createacc()
    c1.dis()
    c1.balance()
a=pd.series(arr)
print(a)'''
#############################################################################################################

#INHERITANCE
class A:
    def s(self):
        print("Speak")
class B(A):
    def ba(self):
        print("Bark")
d=B()
d.ba()
d.s()
