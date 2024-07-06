import pygame
import time

def spielbild_zeichnen(spielersprite,gegnersprites,spielfenster,spielstandtext):
    spielfenster.hintergrund_zeichnen()
    spielfenster.text_zeichnen(spielstandtext,(20,20))
    gegnersprites.zeichnen(spielfenster)
    spielersprite.zeichnen(spielfenster)
    pygame.display.update()

def gewonnen(spielstand,spielfenster, gameoverbild):
    pygame.mouse.set_visible(True)
    time.sleep(0.25)
    spielfenster.neues_hintergrund_bild(gameoverbild)
    spielfenster.hintergrund_zeichnen()
    spielfenster.text_zeichnen(spielstand,(500,200))
    pygame.display.update()
    time.sleep(5)