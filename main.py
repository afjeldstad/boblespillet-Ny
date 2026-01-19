import tkinter as tk
import time
from random import randint,random, uniform
from ring import Ring
from boble import Boble
from helt import Helt
from hjelpefunksjoner import processKeypress
from fiende import Fiende
 
window = tk.Tk()
window.lift()
window.focus_force()
bredde = 800
hoyde = 700
canvas_height = hoyde - 150
canvas_width = bredde
window.minsize(bredde,hoyde)
vindu_bakgrunn = "#FFFFFF"
tekst_bakgrunn = "#FFFFFF"
bunn_bakgrunn = "#3e3e3e"
vann_bakgrunn = "#292b52"
window.configure(background=vindu_bakgrunn)
window.pack_propagate(False)
 
#Canvas
canvas = tk.Canvas(window)
canvas.configure(
    width = canvas_width,
    height = canvas_height,
    background = vann_bakgrunn
)
canvas.pack(expand=True)
 
#Referanse til canvas i ring-klassen
Ring.canvas = canvas
 
#Helten
helten = Helt(uniform(10,20),50,50)
helten.dx = 0
helten.dy = 0
 
#Fienden
fienden = Fiende(uniform(10,20),canvas_width-50,canvas_height-50)
fienden.dx = 0
fienden.dy = 0
 
#Frame
topp = tk.Frame(window)
topp.configure(
    height = 50,
    width = bredde*0.75,
    background = vindu_bakgrunn,
)
topp.pack_propagate(False)
topp.pack()
 
#Overskrift
overskrift = tk.Label(topp)
overskrift["text"] = "Spis mindre bobler, pass deg for de store!"
overskrift.configure(
    font = ("Aptos",20),
    foreground = "black",
    background = tekst_bakgrunn
)
overskrift.pack()
 
 
#Mellomrom
mellomrom = tk.Label()
mellomrom.configure(
    height = 1,
    width = 1,
    bg = vindu_bakgrunn,
)
mellomrom.pack()
 
#Utskrift der resultatet skal havne
utskrift = tk.Label()
utskrift["text"] = "Helt: 0 poeng | Fiende: 0 poeng"
utskrift.configure(
    font = ("Aptos", 14),
    foreground = "black",
    bg = tekst_bakgrunn,
)
utskrift.pack()
 
 
# Lager en ramme nederst til avsluttknappen.
bunn = tk.Frame(window)
bunn.configure(
    width=bredde,
    height=50,
    background=bunn_bakgrunn,
)
bunn.pack()
bunn.pack_propagate(False)
 
def handle_avslutt():
    global isRunning
    isRunning = False
    window.destroy()
 
# Knapp
avslutt = tk.Button(bunn)
avslutt.configure(
    text = "Avslutt",
    command=lambda: handle_avslutt()
)
avslutt.pack()
 
#Bind tastetrykk
window.bind("<KeyPress>", lambda event: processKeypress(event, helten, fienden))
 
# ---- Spillogikk ----
xmin = 0
xmax = canvas_width
ymin = 0
ymax = canvas_height
 
 
 
 
bobler = []
teller = 0
R_MIN = 2
R_MAX = 40
 
isRunning = True
lastTime = time.time()
start_time = time.time()
slette_indexer = []
dt = 1/30
 
#Spill-loop
while isRunning:
    if time.time() - lastTime >= dt:
       
 
        #Tegn Helt
        if not helten.levende and not fienden.levende:
            utskrift.config(
                text = f"GAME OVER!",
                foreground = "red"
            )
        else:
            canvas.delete("ring")
            if helten.levende:
                helten.oppdater()
                #Sjekker om helten kolliderer
                for boble in bobler:
                    if helten.levende and boble.levende:
                        helten.kollisjon(boble)
            if fienden.levende:
                fienden.oppdater()
                #Sjekker om fienden kolliderer
                for boble in bobler:
                    if fienden.levende and boble.levende:
                        fienden.kollisjon(boble)
 
            #Oppdaterer poengutskrift
            utskrift.config(
                text = f"Helt: {helten.poeng} poeng | Fiende: {fienden.poeng} poeng"
            )
 
            #Lager ringer helt tilfeldig
            if random() < 0.04 and len(bobler) < 50:
                r = randint(R_MIN, R_MAX)
                x = randint(r, canvas_width - r)
                y = randint(r, canvas_height - r)
 
                ny_boble = Boble(r,x,y)
 
                ny_boble.dx = uniform(-2,2)
                ny_boble.dy = uniform(-2,2)
                #Legger til boblen i listen
                bobler.append(ny_boble)
 
            #Tegner og oppdaterer boblene
            for boble in bobler:
                boble.oppdater()
           
            #Sjekk for kollisjoner mellom bobler
            for i in range(len(bobler)):
                for j in range(len(bobler)):
                    if i != j:
                        bobler[i].kollisjon(bobler[j])
 
 
        lastTime = time.time()
    window.update()
window.mainloop()