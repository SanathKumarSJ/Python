import pandas as pd
class fridge:
    def __init__(self,eggs,milk,chese):
        self.eggs=eggs
        self.milk=milk
        self.chese=chese

    def checkeggs(self):
        if(self.eggs>=2):
            print("Sufficient Quantity")
        else:
            print("Insufficient Quantity")
    def checkmilk(self):
        if(self.milk>=3):
            print("Sufficient Quantity")
        else:
            print("Insufficient Quantity")

    def checkeggs(self):
        if(self.eggs>=2):
            print("Sufficient Quantity")
        else:
            print("Insufficient Quantity")
    def checkchese(self):
        if(self.chese>=4):
            print("Sufficient Quantity")
        else:
            print("Insufficient Quantity")
    def table(self):
        hd=pd.Series(["no.","qnty"])
        print(hd)
        it=pd.Series([self.milk,self.eggs,self.chese])
        print(it)
obj=fridge(int(input("Enter no. of eggs: ")),int(input("Enter ltrs of milk: ")),int(input("Enter no. of cheese: ")))
obj.checkeggs()
obj.checkmilk()
obj.checkchese()
obj.table()