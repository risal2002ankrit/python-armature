class Point:
    def __init__(self, x, y):     #constructor
        self.x=x
        self.y=y
        
    def move(self):
        print("move")
    
    def draw(self):
        print("draw")
    
point= Point(10,20)
print(point.x,point.y)
point.x=35
print(point.x,point.y)


