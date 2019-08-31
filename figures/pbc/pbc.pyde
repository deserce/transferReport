add_library('dashedlines')
add_library('pdf')
def setup():
    
    size(3000,3000, PDF, 'pbc.pdf')

    rectMode(CENTER)
    ellipseMode(CENTER)
    background(255)
def draw():
    pushMatrix()
    translate(width/2, height/2)
    dash=DashedLines(this)
    dashl = width/100
    dash.pattern(dashl, 2*dashl)
    
    
    bsize = width/3.2
    
    
    def op(x,y, xi, yi, r):
        if sqrt((x-xi)**2 + (y-yi)**2) < r:
            return 255
        else:
            return 100
    n = 2
    xi = 0
    yi = 0
    xi = bsize*0.4
    yi = - bsize*0.4
    
    r = bsize/1.5
    
    for i in range(-n,n+1):
        for j in range(-n,n+1):
            stroke(205)
            strokeWeight(width/200)
            
            rect(bsize*i, bsize*j, bsize,bsize)
            
            #draw atoms
            strokeWeight(bsize/60)
            #red
            x = bsize*i+bsize/3
            y = bsize*j + bsize*0.3
            o = op(x,y,xi, yi,r)
            fill(255,100,100,o)
            stroke(0,0,0,o)
            circle(x,y, bsize/6)
            
            #Green
            x = bsize*i
            y = bsize*j
            o = op(x,y,xi, yi,r)
            fill(100,255,100,o)
            stroke(0,0,0,o)
            circle(x,y, bsize/6)
            
                    #Blue
            x = bsize*i + xi
            y = bsize*j + yi
            o = op(x,y,xi, yi,r)
            fill(100,100,255,o)
            stroke(0,0,0,o)
            circle(x,y, bsize/6)
            
            #Green
            x = bsize*i - bsize*0.35
            y = bsize*j - bsize*0.25
            o = op(x,y,xi, yi,r)
            fill(100,255,255,o)
            stroke(0,0,0,o)
            circle(x,y, bsize/6)
            
            x = bsize*i - bsize*0.35
            y = bsize*j + bsize*0.25
            o = op(x,y,xi, yi,r)
            fill(255,255,100,o)
            stroke(0,0,0,o)
            circle(x,y, bsize/6)
            
            noFill()
    stroke(0)
    rect(0,0,bsize,bsize)
    rect(bsize,0,bsize,bsize)
    rect(0,-bsize,bsize,bsize)
    rect(bsize,-bsize,bsize,bsize)
    strokeWeight(width/500)
    dash.ellipse(xi,yi,r*2,r*2)
    popMatrix()
    noLoop()
    exit()
