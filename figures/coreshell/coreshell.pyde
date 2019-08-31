add_library('pdf')
def setup():
    size(3000, 1500, PDF, "coreshell.pdf")
    ellipseMode(CENTER)
    noFill()
    strokeWeight(6)
    strokeCap(ROUND)





def draw():
    core_r = 100

    core_c = [117, 112, 179]
    shell_r = 600
    shell_c = [27, 158, 119]
    nspring = 14
    springh = 12
    off = 180
    xpos = 400
    class coreShell:

        def __init__(self, x=0, y=0, offset=0,
                     core_r=100, shell_r=600,
                     core_c=[117, 112, 179],
                     shell_c=[27, 158, 119]):
            self.x = x
            self.y = y
            self.offset = offset
            self.core_r = core_r
            self.shell_r = shell_r
            self.shell_c = shell_c
            self.core_c = core_c

        def display(self):

            fill(*self.shell_c)
            circle(self.x + self.offset, self.y, self.shell_r)
            fill(*self.core_c)
            circle(self.x, self.y, self.core_r)

            dx = (self.offset / (nspring))

            noFill()
            beginShape()
            vertex(self.x, self.y)
            vertex(self.x + dx, self.y)

            hsign = 1
            for i in range(2, nspring - 1):
                vertex(self.x + i * dx, self.y + (springh * hsign))
                hsign *= -1

            vertex(self.x + self.offset - dx, self.y)
            vertex(self.x + self.offset, self.y)
            endShape()

    entities = []
    entities.append(coreShell(x=xpos, offset=off,
                              core_r=100, core_c=[255, 100,100],
                              shell_r=800, shell_c=[200, 200, 200]
                              )
                    )
    entities.append(coreShell(x=-xpos, offset=-off,
                              core_r=100, core_c=[100,100, 255],
                              shell_r=1200, shell_c=[200, 200, 200]))

    pushMatrix()
    translate(width / 2, height / 2)
    background(255)
    for e in entities:
        e.display()

    popMatrix()
    myFont = createFont("Myriad", 100);
    textFont(myFont);
    textAlign(CENTER, CENTER);
    
    translate(-xpos,650)
    text("- Ion", width/2, height/2);
    translate(2*xpos,0)
    fill(*[255,100,100])
    text("+ Ion", width/2, height/2);
    noLoop()
    exit()
