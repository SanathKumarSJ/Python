class chr:
    def __init__(self,checkn,strkey):
        self.checkn=checkn
        self.strkey=strkey
    def op(self):
        count=0
        if self.strkey in self.checkn:
            for i in self.checkn:
                if i==self.strkey:
                    count+=1
            return True,count
        else:
            return False,count
obj=chr(input("Enter the string"),input("enter the key"))
res,c=obj.op()
if res:
    print("Character present {} times".format(c))
else:
    print("Character is not present")