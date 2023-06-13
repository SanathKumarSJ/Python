class Point:
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
    def funct(self):
        return ((self.x**2)+(self.y**2))**0.5
obj = Point(3,4)
h = obj.funct()
print(h,obj.x)