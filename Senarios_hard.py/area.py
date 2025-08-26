
class shape:
    def __init__(self):
        pass 
        
    def area(self):
        pass
    
class circle(shape):
    def __init__(self,radius):
        super().__init__()
        self.radius=radius
    def area(self):
        
        a=3.14*self.radius*self.radius
        return ({"area of circle ":a})
    
class rectangle(shape):
    def __init__(self,length,wither):
        super().__init__()
        self.len=length
        self.wither=wither
    def area(self):
        
        a=self.len*self.wither
        return ({"area of rectangle ":a})

class triangle(shape):
    def __init__(self,heigth,base):
        super().__init__()
        self.heigth=heigth
        self.base=base
    def area(self):
        
        a=(self.heigth*self.base)/2
        return ({"area of triangle  ":a})

areas=[]
while True: 
       
    print("enter your option ")
    print("1: circle ")
    print("2 rectangle ")
    print("3: triangle ")
    print("4: list of area ")
    c=int(input("enter your option "))
    s1=shape()
    
    if c==1:
        r=float(input("enter your radius "))
        s1=circle(r)
        print(s1.area())
        areas.append(s1.area())
    elif c==2:
        l=float(input("enter your length "))
        w=float(input("enter your wither "))
        s1=rectangle(l,w)
        print(s1.area())
        areas.append(s1.area())
    elif c==3:
        h=float(input("enter your height "))
        b=float(input("enter your base "))
        s3=triangle(h,b)
        print(s3.area())
        areas.append(s3.area())
    elif c==4:
        print(areas)
        
         
    

        
        



