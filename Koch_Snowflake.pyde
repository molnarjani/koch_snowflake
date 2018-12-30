from segment import Segment

segments = []

def setup():
    size(600, 800)
    a = PVector(0, 100)
    b = PVector(600, 100)
    c = PVector(300, 600)
    s1 = Segment(a, b)
    s2 = Segment(b, c)
    s3 = Segment(c, a)
    segments.extend([s1, s2, s3])
    
def mousePressed():
    global segments
    next_generation = []
    for segment in segments:
        children = segment.generate()
        next_generation.extend(children)
    segments = next_generation
        
    
def draw():
    background(0)
    translate(0, 100)
    
    stroke(255)
    for segment in segments:
        segment.show()
