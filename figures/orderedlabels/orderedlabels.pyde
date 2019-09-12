add_library('pdf')
add_library('dashedlines')
def setup():

    size(2000, 2500, PDF, 'orderedlabels.pdf')
def draw():
    background(255)
    translate(width/2, width/8)
    voffset = width/3
    
    
    rectMode(CENTER)
    
    layeryy = width/15
    layeryx = - width/12
    layerx = width/3
    
    dash = DashedLines(this)
    dash.pattern(width/100,width/100)
    
    diam = width/12
    
    textAlign(CENTER, CENTER)
    f = createFont('Raleway', 100)
    textFont(f)
    
    coords = []
    for i in range(4):
        for lxi in range(-1,2,1):
            for lyi in range(-1,2,1):
                x = (lxi * layerx) + (lyi * layeryx)
                y = (i * voffset) + (lyi*layeryy)
                coords.append([x,y])
    
    type = [0]*len(coords)
    
    ovac = [1,7, 27, 29, 33, 35]
    for v in ovac: type[v] = 1
    
    ox = [3,5, 9, 11, 13, 15, 17, 19, 21, 23, 25, 31]
    for o in ox: type[o] = 2
    
    mn = [12, 14, 22]
    for m in mn: type[m] = 3
    
    
    
    # stroke(155)
    dash.line(coords[0][0], coords[0][1], coords[27][0], coords[27][1])
    dash.line(coords[2][0], coords[2][1], coords[29][0], coords[29][1])
    dash.line(coords[6][0], coords[6][1], coords[33][0], coords[33][1])
    dash.line(coords[8][0], coords[8][1], coords[35][0], coords[35][1])
    
    fill(205, 205, 205, 155)
    noStroke()
    for i in range(4):
        beginShape()
        vertex(coords[9*i][0], coords[9*i][1])
        vertex(coords[9*i + 2][0], coords[9*i + 2][1])
        vertex(coords[9*i + 8][0], coords[9*i + 8][1])
        vertex(coords[9*i + 6][0], coords[9*i + 6][1])
        endShape(CLOSE)
    stroke(0)
    
    ocounter = 1
    mncounter = 1
    licounter = 1
    vaccounter = 1
    
    faded = [1]*len(coords)
    keyli = [2,4,10,20, 28, 32]
    keyo = [5, 11, 13, 19, 23, 31]
    keymn = [14, 22]
    keyvac = [1, 29]
    for i in keyli + keyo + keymn + keyvac:
        faded[i] = 0
    
    for i in range(len(coords)):
        
        if faded[i] == 1:
            opac = 50
        else: opac = 255
        stroke(255-opac)
        
        if type[i] == 0:
            fill(0,255,0, opac)
            circle(coords[i][0], coords[i][1], diam)
            if faded[i] == 0:
                fill(0)
                text(str(licounter),coords[i][0], coords[i][1])
                licounter += 1
            
        elif type[i] == 1:
            noFill()
            dash.rect(coords[i][0], coords[i][1], diam, diam)
            if faded[i] == 0:
                fill(0)
                text(str(vaccounter),coords[i][0], coords[i][1])
                vaccounter += 1
        elif type[i] == 2:
            fill(255,0,0, opac)
            circle(coords[i][0], coords[i][1], diam)
            if faded[i] == 0:
                fill(0)
                text(str(ocounter),coords[i][0], coords[i][1])
                ocounter += 1
        elif type[i] == 3:
            fill(128,0,128, opac)
            circle(coords[i][0], coords[i][1], diam)
            if faded[i] == 0:
                fill(255)
                text(str(mncounter),coords[i][0], coords[i][1])
                mncounter += 1
    noLoop()
    exit()
