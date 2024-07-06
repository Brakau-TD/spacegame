import time
import random
from grafiken import *
from objekte import *
clock = pygame.time.Clock()

def kollision(spielersprite,gegnersprite):
    if gegnersprite.ist_kollision(spielersprite):
        return True
    else:
        return False

def spielbild_zeichnen(spielersprite,gegnersprite,spielfenster,spielstandtext):
    spielfenster.hintergrund_zeichnen()
    spielfenster.text_zeichnen(spielstandtext,(20,20))
    gegnersprite.zeichnen(spielfenster)
    spielersprite.zeichnen(spielfenster)
    pygame.display.update()

def gewonnen(spielstand,spielfenster):
    time.sleep(0.25)
    spielfenster.neues_hintergrund_bild(gameoverbild)
    spielfenster.hintergrund_zeichnen()
    spielfenster.text_zeichnen(spielstand,(500,200))
    pygame.display.update()
    time.sleep(5)

def kollision_pruefen(spielstand,spielersprite,gegnersprite, abbrechen):
    if kollision(spielersprite,gegnersprite):
        spielstand += 1
        # gegnersprite.neue_position_setzen(random.randint(0,fensterbreite),random.randint(0,fensterhoehe))
        abbrechen = False
    if spielstand > 100:
        abbrechen = True
    return spielstand, abbrechen

def bewegung_aktualisieren(spielersprite,gegnersprite):
    maus_position = pygame.mouse.get_pos()
    gegnersprite.neue_position_rechnen()
    gegnersprite.ist_ausserhalb()
    spielersprite.neue_position_setzen(maus_position[0],maus_position[1])

def spiel_spielen(gegnersprite,spielersprite):
    abbrechen = False
    spielstand = 0
    while not abbrechen:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                abbrechen = True

        spielstand, abbrechen = kollision_pruefen(spielstand,spielersprite,gegnersprite, abbrechen)

        bewegung_aktualisieren(spielersprite,gegnersprite)

        spielbild_zeichnen(spielersprite,gegnersprite,spielfenster,spielstand)
        clock.tick(60)
    
    gewonnen(spielstand,spielfenster)
    pygame.quit()

spiel_spielen(gegnersprites,spielersprite)
