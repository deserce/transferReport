add_library('dashedlines')

add_library('pdf')
def setup():
    size(3000, 3000, PDF, "mott.pdf")
    # background('#ffffff')
# pixelDensity(2)
    strokeWeight(10)

    # font = loadFont("MyriadPro-Regular-48.vlw")
    # textFont(font, 48);
    rectMode(CENTER)

    ellipseMode(CENTER)

def draw():
    background(255)
    dash = DashedLines(this)
    dash.pattern(15, 15)
    n = 20
    r = 80
    r1 = (width / n) * 3
    r2 = (width / n) * 6
    rmax = (width / n) * 9.5
    tmin = 10
    for i in range(1, n):
        for j in range(1, n):
            stroke(0)
            x = (i * width) / n
            y = (j * height) / n
            d = sqrt(abs(x - (width / 2)) ** 2 + abs(y - (height / 2)) ** 2)

            if d < r1:
                fill(255, 0, 0, 250)
            elif d < r2:
                fill(0, 255, 0, 250)
            else:
                noFill()
                t = (255 - tmin) * max([(rmax - d) / (rmax - r2), 0]) + tmin
                stroke(0, 0, 0, t)
            if d != 0:
                cx = x
                cy = y
                circle(x, y, r)
            else:
                noFill()

                dash.rect(x, y, r,r)

    pushMatrix()
    translate(width / 2, height / 2)
    noFill()

    strokeWeight(5)
    stroke(55, 55, 55, 150)
    circle(0, 0, r1 * 2)
    circle(0, 0, r2 * 2)

    # translate(-width/(168*n),-width/(4*n))
    # textMode(CENTER)
    textAlign(CENTER, CENTER)
    textSize(30)
    fill(0)
    # text('I',0, 5*(width/(2*n)) )
    # text('IIa',0, 9*(width/(2*n)) )
    # text('IIb',0, 13*(width/(2*n)) )

    exit()
