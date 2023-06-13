'''class sumo:
    def __init__(self,lst):
        self.lst=lst
    def nosm(self):
        print("sum is ",sum(self.lst))
obj=sumo([1,2,3,4,5])
obj2=sumo([1,2,3,4])
obj.nosm()
obj2.nosm()'''
class sumo:
    def __int__(self):  #No need of writing this
        pass
    def sumof(self,list):   # Parameters are passed here
        return sum(list)    #returning the sum of list not self.list coz constructr value is passed
obj=sumo()                  #Class has no attributes
res=obj.sumof([1,2,3,4,5])  #Value passed to the function named sumof
print("SUM IS:",res)        #Pritnting the result