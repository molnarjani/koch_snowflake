class Segment:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        
    def generate(self):
        children = []
        v = PVector.sub(self.b, self.a)
        v.div(3)
        
        b1 = PVector.add(self.a, v)
        children.append(Segment(self.a, b1))
        
        a1 = PVector.sub(self.b, v)
        children.append(Segment(a1, self.b))
        
        v.rotate(-PI/3)
        c = PVector.add(b1, v)
    
        children.append(Segment(b1, c))
        children.append(Segment(c, a1))
        return children
    
    def show(self):
        stroke(255)
        line(self.a.x, self.a.y, self.b.x, self.b.y)
