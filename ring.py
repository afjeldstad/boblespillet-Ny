class Ring():
    canvas = None
    farger = ["chartreuse","yellow","orange","red","magenta","peachpuff","black"]
   
    #Klasse for å tegne en ring
    def __init__(self,r,x,y):
        self.R = r
        self.x = x
        self.y = y
        self.canvas = Ring.canvas
        self.tag = "ring"
        self.outline = "white"
 
    def tegn(self):
        self.canvas.create_oval(self.x - self.R, self.y - self.R,
                                self.x + self.R, self.y + self.R,
                                outline = self.outline,
                                tags = self.tag)
 