add_library('pdf')
add_library('dashedlines')
def setup():

    size(2200, 2800, PDF, 'orderedlabels.pdf')
def draw():
    background(255)
    translate(width/2 + 180, width/8)
    voffset = width/3
    
    
    rectMode(CENTER)
    
    layeryy = width/15
    layeryx = - width/12
    layerx = width/3 - 100
    
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
    
    
    
    stroke(155)
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
    intercounter = 1
    
    faded = [1]*len(coords)
    keyli = [2,4,10,20, 28, 32]
    keyo = [5, 11, 13, 19, 23, 31]
    keymn = [14, 22]
    keyvac = [1, 29]
    
    inter = [[0,0], [0,0], [0,0]]
    # Interstitial 1
    for i in [0,1]:
        for j in keyli[0:3] + [keymn[0]] + keyo[0:3] + [keyvac[0]]:
            inter[0][i] += coords[j][i]
        inter[0][i] = inter[0][i]/8

        for j in keyli[2:4] + keymn + keyo[1:5]:
            inter[1][i] += coords[j][i]
        inter[1][i] = inter[1][i]/8
    
        for j in keyli[3:] + [keymn[1]] + keyo[3:] + [keyvac[1]]:
            inter[2][i] += coords[j][i]
    
        inter[2][i] = inter[2][i]/8    
    
    stroke(0,0,255,230)
    
    corners = [[keyli[0], keyo[2]],
               [keyli[1], keyo[1]],
               [keyli[2], keyo[1]],
               [keyvac[0], keymn[0]],
               
               [keyli[2], keyo[4]],
               [keyli[3], keyo[2]],
               [keyo[1], keymn[1]],
               [keyo[3], keymn[0]],
               
               [keyli[3], keyo[5]],
               [keyli[4], keyo[4]],
               [keyli[5], keyo[3]],
               [keyvac[1], keymn[1]]]
    dash.pattern(15,30)
    strokeWeight(2)
    for i in corners:
        w = 5
        
        w1x = (coords[i[0]][0] * w + coords[i[1]][0]) / (w+1)
        w1y = (coords[i[0]][1] * w + coords[i[1]][1]) / (w+1)
        
        w2x = (coords[i[0]][0] + coords[i[1]][0] * w) / (w+1)
        w2y = (coords[i[0]][1] + coords[i[1]][1] * w) / (w+1)
        dash.line(w1x, w1y, w2x, w2y)
               
    dash.pattern(width/100,width/100)
    
    for i in keyli + keyo + keymn + keyvac:
        faded[i] = 0
    
    for i in range(len(coords)):
        
        if faded[i] == 1:
            opac = 100
        else: opac = 255
        stroke(255-opac)
        
        if type[i] == 0:
            fill(0,255,0, opac)
            circle(coords[i][0], coords[i][1], diam)
            if faded[i] == 0:
                fill(0)
                text(str(licounter),coords[i][0], coords[i][1]-5)
                licounter += 1
            
        elif type[i] == 1:
            noFill()
            dash.rect(coords[i][0], coords[i][1], diam, diam)
            if faded[i] == 0:
                fill(0)
                text(str(vaccounter),coords[i][0], coords[i][1]-5)
                vaccounter += 1
        elif type[i] == 2:
            fill(255,0,0, opac)
            circle(coords[i][0], coords[i][1], diam)
            if faded[i] == 0:
                fill(0)
                text(str(ocounter),coords[i][0], coords[i][1]-5)
                ocounter += 1
        elif type[i] == 3:
            fill(128,0,128, opac)
            circle(coords[i][0], coords[i][1], diam)
            if faded[i] == 0:
                fill(255)
                text(str(mncounter),coords[i][0], coords[i][1]-5)
                mncounter += 1
        
    for i in inter:
        fill(180,180,255)
        stroke(0,0,255,200)
        
        circle(i[0], i[1],150)
        fill(255)
        text(str(intercounter), i[0], i[1] - 20)
        intercounter += 1
    
    stroke(0)
    strokeWeight(4)
    fill(0)
    translate(-width/2 - 100, 7*height/8)
    line(0,0,0,-150)
    ah = 10
    triangle(-ah, -150, ah, -150, 0, -150-2*ah)
    
    line(0,0,-layeryx*0.5,-layeryy*0.5)
    triangle(-layeryx*0.5 - ah, -layeryy*0.5, 
             -layeryx*0.5 + ah, -layeryy*0.5,
             -layeryx*0.55, -layeryy*0.55)

    line(0,0,150,0)
    triangle(150, ah, 150, -ah, 150+2*ah, 0)
    
    textSize(50)
    text('a',-layeryx*0.7-20, -layeryy*0.7 - 10)
    text('b',0, -210)
    text('c',190, -ah)
    noLoop()
    exit()
