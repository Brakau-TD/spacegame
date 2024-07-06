import pygame
import time

# beginnt Pygame
pygame.init()

# erzeugt das Spielfenster und den Taktgeber
spielfenster = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

def spielfenster_zeichnen(rechteck,rechteckfarbe,mausrechteck):
    # Zeichnet ein Rechteck an der Mausposition und an den Positionen der Rechtecke
    spielfenster.fill((255, 255, 255)) # Hintergrundfarbe des Spiels ist weiß
    rechteck.x = rechteck.x + 1 # Bewegt das Rechteck nach rechts
    rechteck.y = rechteck.y + 1 # Bewegt das Rechteck nach unten
    pygame.draw.rect(spielfenster, rechteckfarbe, rechteck) # Zeichnet das Rechteck
    pygame.draw.rect(spielfenster,(0,0,0), mausrechteck) # Zeichnet den Mauszeiger

    # Erneuert das Display
    pygame.display.update()

def spiel():
    """
    diese Funktion enthält die gesamte "Logik" des Spiels, 
    also das, was passiert, wenn das Spiel läuft
    Hier beginnt der sogenannte "Game Loop", 
    also die Schleife, die das Spiel am Laufen hält
    die Schleife findet ab dem Befehl "while" statt und endet, 
    wenn die Variable "running" auf "False" gesetzt wird
    """
    # Ein rotes Rechteck [x-Position, y-Position, Breite, Höhe] als "Gegner"
    rechteck=pygame.Rect(100, 100, 50, 50)
    rechteckfarbe = (255, 0, 0)
    am_laufen = True # Variable, die bestimmt, ob das Spiel läuft
    pygame.mouse.set_visible(False) # Macht den Mauszeiger unsichtbar

    while am_laufen:
        # diese Schleife prüft bei jedem Durchlauf, ob der Spieler auf "Schließen" geklickt hat
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                am_laufen = False

        # holt die Position der Maus
        mausposition = pygame.mouse.get_pos()
        mausrechteck = pygame.Rect(mausposition, (10, 10))

        # Prüft ob die Maus auf das Rechteck zeigt
        if rechteck.collidepoint(mausposition):
            print("Kollision gefunden!")
            rechteckfarbe = (0, 255, 0)
            am_laufen = False

        # ruft die Funktion auf, die das Spielfenster zeichnet
        spielfenster_zeichnen(rechteck,rechteckfarbe,mausrechteck)

        clock.tick(60) # sorgt dafür, dass das Spiel mit 60 Bildern pro Sekunde läuft
    time.sleep(2)
    pygame.quit()

spiel()