add_library('dashedlines')
add_library('pdf')
import random
def setup():
    size(3000,2500, PDF, 'batteryDischarge.pdf')
    strokeJoin(ROUND)
    

def roundedRect(x,y, w, h, rx, ry):
    beginShape()
    vertex(x, y+ry)
    bezierVertex(x,y,x,y,x+rx,y)
    
    vertex(x+w-rx,y)
    bezierVertex(x+w,y,x+w,y,x+w,y+ry)
    
    vertex(x+w,y+h-ry)
    bezierVertex(x+w,y+h,x+w,y+h,x+w-rx,y+h)
    
    vertex(x+rx,y+h)
    bezierVertex(x,y+h,x,y+h,x,y+h-ry)
    
    endShape(CLOSE)

class Li:
    def __init__(self, x, y, arrow = False):
        self.r = 100
        self.x = x
        self.y = y
        self.arrow = arrow
    def display(self):
        textSize(60)
        fill(100,255,100)
        circle(self.x, self.y, self.r)
        if self.arrow: text(u'\u2190', self.x + self.r, self.y)

        fill(0)
        text(u'Li\u207A',self.x, self.y)
        
    
def draw():
    noFill()
    background(255)
    translate(width/2, height/2)
    strokeWeight(4)
    myFont = createFont("Myriad", 100);
    textFont(myFont);
    
    textAlign(CENTER, CENTER)
    rh = 1500
    rw = 2800
    
    wireh = 200
    wireg = 75
    wireo = 50
    terminalp = 100
    terminaln = 50
    electrodew = 1000
    platew = 50
    strokeWeight(10)

    
    dash = DashedLines(this)
    dash.pattern(50,50)
    dash.offset(25)
    fill(155,155,155)
    strokeWeight(10)
    roundedRect(-rw/2,-rh/2,rw,rh, 50,50)
    text("Electrolyte", 0, rh/2 + wireh/2);
    
    strokeWeight(5)
    fill(255,100,100)
    roundedRect(-rw/2,-rh/2,electrodew,rh,50,50)
    
    text("Cathode", -rw/2 + electrodew/2, rh/2 + wireh/2);
    text(u"LiCoO\u2082", -rw/2 + electrodew/2, rh/2 + wireh*5/4);

    fill(100,100,255)
    roundedRect(rw/2-electrodew,-rh/2,electrodew,rh,50,50)
    text("Anode", rw/2 - electrodew/2, rh/2 + wireh/2);
    text("Graphite", rw/2 - electrodew/2, rh/2 + wireh*5/4);
    
    fill(200)
    rect(rw/2-wireo-platew/2,-rh/2,platew, rh*0.95)
    
    fill(184, 115, 51)
    rect(-(rw/2-wireo+platew/2),-rh/2,platew, rh*0.95)
    
    fill(0)
    strokeWeight(5)
    dash.line(0,-rh/2,0,rh/2)
    
    strokeWeight(5)
    
    line(wireo - rw/2,-rh/2, wireo - rw/2,-wireh-rh/2)
    line(-wireo + rw/2,-rh/2, -wireo + rw/2,-wireh-rh/2)
    
    line(wireo - rw/2,-wireh-rh/2, -wireg, -wireh-rh/2)
    line(-wireo + rw/2,-wireh-rh/2, wireg, -wireh-rh/2)
    
    # line(-wireg, -wireh-rh/2 + terminalp, -wireg, -wireh-rh/2 - terminalp)
    # line(wireg, -wireh-rh/2 + terminaln, wireg, -wireh-rh/2 - terminaln)
    noFill()
    roundedRect(-wireg,-rh/2-wireh - wireg*3/2,wireg*2,wireg*3.5,30,30)
    insetx = 15
    insety = 30
    yoff = 15
    fill(0)
    roundedRect(-wireg+insetx,-yoff-rh/2-wireh - wireg*3/2 +insety,wireg*2 -2*insetx,wireg*3.5 -2*insety,30,30)
    noFill()
    circle(0, -yoff-rh/2-wireh - wireg*3/2 +insety +225, 25)
    
    fill(255,255,50)
    beginShape()
    bolth = 150
    bolty = -1020
    boltyoff = -15
    boltxoff = 0
    boltw = 30
    vertex(0, bolty)

    vertex(boltxoff, bolty+bolth/2 + boltyoff)
    vertex(boltw, bolty+bolth/2 + boltyoff)
    
    vertex(0, bolty+bolth)
    
    vertex(-boltxoff, bolty+bolth/2 - boltyoff)
    vertex(-boltw, bolty+bolth/2 - boltyoff)
    endShape(CLOSE)
    fill(0)
    
    text(u'\u2190 e\u207B ',0,-(rh/2 + wireh + 2*terminalp))
    
    
    
    L = [Li(100,0, arrow = True), 
         Li(200,200, arrow = True),
         Li(-200,300, arrow = True),
         Li(-250,-300, arrow = True),
         Li(-200,300, arrow = True)]
    

    random.seed(1003)
    fill(50,50,255)
    stroke(30)
    for i in range(-rh/3+rh/10, rh/2, rh/4):
        beginShape(TRIANGLE_STRIP);
        s = 1
        d = -rw/2 + 80
        for j in range(13):
            vertex(d, i + 75*s)
            d += 75
            s *=-1
            if random.random() < 0.8: 
                if s == 1: L.append(Li(d,i+rh/8))
            if random.random() < 0.8: 
                if s == 1: L.append(Li(d,i-rh/8))
        endShape();
    
    stroke(30,30,30,200)
    strokeWeight(30)
    
    for i in range(-rh/3, rh/2, rh/6):
        line(rw/2-wireo-platew/2, i, rw/2-electrodew+40,i)
        for j in range(rw/2-wireo-platew, rw/2-electrodew+40,-((rw/2-wireo-platew)-(rw/2-electrodew+40))/5 ):
            if random.random() < 0.1: L.append(Li(j-50,i+rh/12))
            if random.random() < 0.1: L.append(Li(j-50,i-rh/12))
        fill(100,255,100)
    
    
    
    
    stroke(0)
    strokeWeight(10)
    for l in L: l.display()
    exit()
