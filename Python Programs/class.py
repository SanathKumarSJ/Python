class employee:

    def getinfo(self):
        self.salary=int(input("enter salary"))
        self.hours=int(input("enter hours"))

    def addsal(self):
        if(self.salary<500):
            self.salary+=100

    def addwrk(self):
        if(self.hours>6):
            self.salary+=200
    def disp(self):
        print("salary=",self.salary)
        print("hours=",self.hours)
c1=employee()
c1.getinfo()
c1.addsal()
c1.addwrk()
c1.disp()