import pygame
import time
from spielfenster import spielfenster

class SpielbilderZeichnen:
    def __init__(self,spielfenster):
        self.spielfenster = spielfenster

    def spielbild_zeichnen(self, spielersprite,gegnersprites,anderesprites,spielstandtext):
        """
        Geht durch alle Spielobjekte, die an die Funktion übergeben werden und zeichnet sie auf das Spielfenster.
        Am Ende wird das Spielfenster aktualisiert, was bedeutet, dass die Änderungen sichtbar werden.
        """
        self.spielfenster.hintergrund_zeichnen()
        self.spielfenster.text_zeichnen(spielstandtext,(20,20))
        for gegner in gegnersprites:
                gegner.zeichnen(self.spielfenster)
        for anderer_sprite in anderesprites:
            anderer_sprite.zeichnen(self.spielfenster)
        spielersprite.zeichnen(self.spielfenster)
        pygame.display.update()

    def spielende_zeichnen(self, spielstand):
        """
        Wird aufgerufen, wenn das Spiel zu Ende ist. Zeigt das Game Over Bild an und den Spielstand.
        """
        pygame.mouse.set_visible(True)
        time.sleep(0.25)
        self.spielfenster.gameoverbild_festlegen()
        self.spielfenster.hintergrund_zeichnen()
        self.spielfenster.text_zeichnen(spielstand,(500,200))
        pygame.display.update()
        time.sleep(5)

SpielBild = SpielbilderZeichnen(spielfenster)