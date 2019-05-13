class color:
    r = 0
    g = 0
    b = 0
    def __init__(self,r, g, b):
        self.r = r
        self.g = g
        self.b = b
        pass
    pass


class point:
    x = 0
    y = 0
    color = color(0,0,0)
    def __init__(self,x, y, color):
        self.x = x
        self.y = y
        self.color = color
        pass
    def draw(self):
        glBegin(GL_POINTS);
        glColor3f(self.color.r,self.color.g,self.color.b);
        glVertex2f(self.x,self.y);
        glEnd();
        pass
    pass

class line:
    p1 = point(0,0,color(0,0,0))
    p2 = point(0,0,color(0,0,0))
    def __init__(self,p1, p2):
        self.p1 = p1
        self.p2 = p2
        pass
    def draw(self):
        glBegin(GL_LINES);
        glColor3f(self.p1.color.r,self.p1.color.g,self.p1.color.b);
        glVertex2f(self.p1.x,self.p1.y);
        glColor3f(self.p2.color.r,self.p2.color.g,self.p2.color.b);
        glVertex2f(self.p2.x,self.p2.y);
        glEnd();
        pass
    pass
class quad:
    p1 = point(0,0,color(0,0,0))
    p2 = point(0,0,color(0,0,0))
    p3 = point(0,0,color(0,0,0))
    p4 = point(0,0,color(0,0,0))
    def __init__(self,p1, p2, p3, p4):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.p4 = p4
        pass
    def draw(self):
        glBegin(GL_LINE_LOOP)
        glVertex2f(self.p1.x,self.p1.y)
        glVertex2f(self.p2.x,self.p2.y)
        glVertex2f(self.p3.x,self.p3.y)
        glVertex2f(self.p4.x,self.p4.y)
        glEnd()
        pass
    pass