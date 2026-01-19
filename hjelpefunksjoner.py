"""
Ulike funksjoner som er til bruk i animasjonslogikk etc.
main.py skal helst ikke bli noe lengre.
"""
 
def processKeypress(event,helt,fiende):
    """
    Håndterer tastetrykk.
    """
    key = event.keysym
    fart = 3
 
    #Kontroller for helten
    if key == "w" or key == "W":
        helt.dy = -fart
        helt.dx = 0
    elif key == "s" or key == "S":
        helt.dy = fart
        helt.dx = 0
    elif key == "a" or key == "A":
        helt.dy = 0
        helt.dx = -fart
    elif key == "d" or key == "D":
        helt.dy = 0
        helt.dx = fart
    #Kontroller for fienden
    elif key == "Up":
        fiende.dy = -fart
        fiende.dx = 0
    elif key == "Down":
        fiende.dy = fart
        fiende.dx = 0
    elif key == "Left":
        fiende.dy = 0
        fiende.dx = -fart
    elif key == "Right":
        fiende.dy = 0
        fiende.dx = fart