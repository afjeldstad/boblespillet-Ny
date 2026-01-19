from boble import Boble
import math
 
class Helt(Boble):
    def __init__(self, r,x,y):
        super().__init__(r,x,y)
        self.type = "helt"
        self.outline = "green"
        self.poeng = 0
   
    def kollisjon(self,objekt2):
        if not self.levende or not objekt2.levende:
            return
       
        dx = self.x - objekt2.x
        dy = self.y - objekt2.y
 
        avstand = math.sqrt(dx**2+dy**2)
 
        if avstand < self.R:
            if self.areal() > objekt2.areal():
                nytt_areal = self.areal() + objekt2.areal()
                self.R = math.sqrt(nytt_areal / math.pi)
 
                objekt2.sprekk_boble()
                self.poeng += 1
 
 
            else:
                self.sprekk_boble()
   
 
 