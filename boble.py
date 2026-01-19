from ring import Ring
import math
 
class Boble(Ring):
    def __init__(self, r,x,y):
        super().__init__(r,x,y)
        self.type = "boble"
        self.levende = True
 
        #Farten til boblen
        self.dx = 0
        self.dy = 0
 
    def areal(self):
        return math.pi * self.R**2
   
    def kollisjon(self, objekt2):
        dx = self.x - objekt2.x
        dy = self.y - objekt2.y
 
        avstand = math.sqrt(dx**2+dy**2)
 
        if avstand < self.R:
            if self.areal() > objekt2.areal():
                nytt_areal = self.areal() + objekt2.areal()
                self.R = math.sqrt(nytt_areal / math.pi)
 
                objekt2.sprekk_boble()
 
            else:
                self.sprekk_boble()
 
    def sprekk_boble(self):
        self.levende = False
        self.R = 0
 
    def oppdater(self):
        if not self.levende:
            return
 
        self.x += self.dx
        self.y += self.dy
 
        if self.x - self.R < 0 or self.x + self.R >= 800:
            self.dx = -self.dx
        if self.y - self.R < 0 or self.y + self.R >= 550:
            self.dy = -self.dy
 
        super().tegn()