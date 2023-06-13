class time:
    def __init__(self,hr=0,min=0,sec=0):
        self.hr=hr
        self.min=min
        self.sec=sec
        print(self.hr)

    def print_time(self):
        print("%d:%d:%d"%(self.hr,self.min,self.sec))


    def toi(self):
        min=self.hr*60+self.min
        sec=

    def incr(self,sec):
        self.sec=sec+self.sec
        while self.sec>=60:
            self.sec-=60
            self.min+=1
        while self.min>=60:
            self.min -= 60
            self.hr += 1
        return self
start=time(9,45,00)
start.print_time()
end=start.incr(1337)
end.print_time()