class Point:
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

class Rectangle:
    def __init__(self, width, height, x, y):
        self.width = width
        self.height = height
        self.corner = Point(x, y)

    def find_center(self):
        p = Point()
        p.x = self.corner.x + self.width / 2
        print(self.corner.x,self.width)
        p.y = self.corner.y + self.height / 2
        print(p.x)
        return p

box = Rectangle(100.0, 200.0, 0.0, 0.0)
box.corner=Point(2.0,2.0)
center = box.find_center()
print(center.x, center.y)