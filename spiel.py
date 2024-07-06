"""
Hauptmodul des Spiels. 
Zuerst werden einige andere Module (Files mit Funktionen) importiert, die für das Spiel benötigt werden,
    das Programm ist also tatsächlich in mehrere Dateien aufgeteilt und größer als es auf den ersten Blick erscheint.
Danach wird das Spiel gestartet und die Spiellogik ausgeführt.
"""
import pygame
from sprite import spielersprite, gegnersprites,anderesprites
from spielbilderzeichnen import SpielBild
from hintergrundlogik import kollision_pruefen, pruefe_spielende, bewegung_aktualisieren, sprite_entfernen, neuer_sprite


class Spiel:
    def __init__(self, gegnersprites, spielersprite, anderesprites):
        """
        Die Klasse 'Spiel' ist die Hauptklasse des Spiels.
        Zu Anfang werden die wichtigen Attribute und Objekte des Spiels initialisiert
        Über die Methode 'spiel_spielen' wird das Spiel gestartet.
        """
        self.gegnersprites = gegnersprites
        self.spielersprite = spielersprite
        self.anderesprites = anderesprites # noch nicht benutzt
        self.spielstand = 0
        self.spiel_vorbei = False
        self.SpielBild = SpielBild

    def spiel_spielen(self):
        """
        Das Hauptprogramm des Spiels. Vor der While-Schleife wird der Mauszeiger ausgeblendet, 
        damit er nicht stört. 
        Die While-Schleife läuft mit 60 Bildern pro Sekunde, solange bis die Variable spiel_vorbei auf True gesetzt wird.
        D.h. alles was unterhalb der While-Schleife eingerückt ist, wird so lange ausgeführt, bis das Spiel vorbei ist.
        """
        clock = pygame.time.Clock()
        pygame.mouse.set_visible(False)

        while not self.spiel_vorbei:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.spiel_vorbei = True

            self.spiellogik_pruefen()
            bewegung_aktualisieren(self.spielersprite,self.gegnersprites,pygame.mouse.get_pos())    

            self.SpielBild.spielbild_zeichnen(self.spielersprite,self.gegnersprites,self.anderesprites,self.spielstand)
            clock.tick(60)
        
        self.SpielBild.spielende_zeichnen(self.spielstand)
        pygame.quit()

    def spiellogik_pruefen(self):
        """
        Führt die Aktionen aus, die im Spiel vorkommen können.
        die Funktionen kollision_pruefen, gewinnbedingung_pruefen werden aufgerufen.
        In den Import-Zeilen steht, in welchen Modulen diese Funktionen definiert sind.
        """
        self.spielstand += kollision_pruefen(self.spielersprite,self.gegnersprites,self.anderesprites)
        self.spiel_vorbei = pruefe_spielende(self.spielstand, parameter = None)

# starte das Spiel
spiel = Spiel(gegnersprites,spielersprite,anderesprites)
spiel.spiel_spielen()

