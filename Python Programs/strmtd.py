'''class point:
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
    def __str__(self):
        return '(' + str(self.x) + ',' + str(self.y) + ')'
p=point(3,4)
print("when we use __str__ method")
x=str(p)
print(x)
print("when we use print method")
print(p)'''


'''
class point:
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
    def __str__(self):
        return '(' + str(self.x) + ',' + str(self.y) + ')'
p=point(3,4)
p1=point(5,6)
print("when we use __str__ method")
print(str(p))
print(type(str(p)) )
print(type(p))
print("when we use print method")
print(p)
print(p1)'''

class point:
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
    def __str__(self):
        return '(' + str(self.x) + ',' + str(self.y) + ')'
    def __add__(self,other):
        return self.x+other.x, self.y+other.y
    def __sub__(self,other):
        return self.x-other.x, self.y-other.y
    def __mul__(self,other):
        return self.x*other.x + self.y*other.y, self.x*other.x, self.y*other.y
    def __rmul__(self,other):
        return self.x*other.x + self.y*other.y

p=point(7,4)
p1=point(5,6)
p3=p + p1
print(p3)
p4=p - p1
print(p4)
p5=p * p1
print(p5)
p6=p * p1
print(p6)


