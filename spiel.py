from objekte import *
from bildschirm_zeichnen import *
clock = pygame.time.Clock()

def kollision(spielersprite,gegnersprite):
    if gegnersprite.ist_kollision(spielersprite):
        return True
    else:
        return False
    
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
    pygame.mouse.set_visible(False)
    while not abbrechen:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                abbrechen = True

        spielstand, abbrechen = kollision_pruefen(spielstand,spielersprite,gegnersprite, abbrechen)

        bewegung_aktualisieren(spielersprite,gegnersprite)

        spielbild_zeichnen(spielersprite,gegnersprite,spielfenster,spielstand)
        clock.tick(60)
    
    gewonnen(spielstand,spielfenster,gameoverbild)
    pygame.quit()

# starte das Spiel
spiel_spielen(gegnersprites,spielersprite)
