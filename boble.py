"""Klassedefinisjon for Boble"""
from ring import Ring
import math

class Boble(Ring):
    def __init__(self, r, x, y):
        super().__init__(r, x, y) # Sender 'r' til Ring, som lagrer den som self.R
        self.type = "boble"
        self.levende = True
        
        # Fart
        self.dx = 0
        self.dy = 0

    def areal(self):
        """Returnerer arealet til en boble"""
        # VIKTIG: Bruker self.R fordi det er det Ring-klassen bruker
        return math.pi * (self.R ** 2)

    def kollisjon(self, objekt2):
        """
        Håndterer kollisjon med andre bobler eller hindringer.
        """
        if not self.levende:
            return

        # Sjekk hindring
        if hasattr(objekt2, 'type') and objekt2.type == "hindring":
            self.sprekk_boble()
            return

        # Sjekk annen boble
        if hasattr(objekt2, 'type') and objekt2.type == "boble":
            # Vi spiser hvis vi er størst eller like store
            if self.areal() >= objekt2.areal():
                nytt_areal = self.areal() + objekt2.areal()
                
                # Regn ut ny radius og lagre i self.R
                self.R = math.sqrt(nytt_areal / math.pi)
                
                # Ny posisjon
                self.x = (self.x + objekt2.x) / 2
                self.y = (self.y + objekt2.y) / 2
                
                # Den andre dør
                objekt2.levende = False
                objekt2.R = 0 
            
            # Hvis vi er mindre, dør vi
            else:
                self.sprekk_boble()

    def sprekk_boble(self):
        """Boblen sprekker/dør"""
        self.levende = False
        self.R = 0 # Setter radius til 0 så den ikke tegnes

    def oppdater(self):
        "Oppdater fart, posisjon, sjekk kollisjon, tegn"
        self.x += self.dx
        self.y += self.dy
        
        # Sjekk vegger (bruker self.R)
        if self.x - self.R < 0 or self.x + self.R > self.canvas.winfo_width():
            self.dx = -self.dx
        
        if self.y - self.R < 0 or self.y + self.R > self.canvas.winfo_height():
            self.dy = -self.dy
            
        super().tegn()

        #test