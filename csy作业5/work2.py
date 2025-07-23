import math

class Circle :
    def __init__(self):
        self.center_x = 0
        self.center_y = 0
        self.radius = 0

    def set_center(self,x,y):
        self.center_x = x
        self.center_y = y

    def set_radius(self,r):
        self.radius = r

    def get_area(self):  
        return math.pi * self.radius**2

if __name__ == '__main__' :
    x = eval(input())
    y = eval(input())
    r= eval(input())
    c = Circle()
    c.set_center(x,y)            
    c.set_radius(r)
    print('center:(%.2f,%.2f),radius:%.2f'%(c.center_x,c.center_y,c.radius) )  
    print('area:%.2f'%c.get_area())

#跑不出来

        