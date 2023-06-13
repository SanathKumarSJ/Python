import pandas as pd
class cart:
    def __init__(self,apple,orange):
        self.apple=apple
        self.orange=orange

    def checkapple(self):
        if(self.apple>=5):
            return "Sufficient Quantity"
        else:
            return "Insufficient Quantity"
    def checkorange(self):
        if(self.orange>=10):
            return "Sufficient Quantity"
        else:
            return "Insufficient Quantity"
    def table(self):
        info={'Sl.No':[1,2],'fruits': ['apple','orange'],'Quantity':[self.apple, self.orange]}
        a=pd.DataFrame(info)
        print(a)

obj=cart(int(input("Enter no. of apple: ")),int(input("Enter no. of orange: ")))
a=obj.checkapple()
b=obj.checkorange()
obj.table()
print('No of apple is',a)
print('No of orange is',b)