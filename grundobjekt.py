import pygame

class Grundobjekt(pygame.sprite.Sprite):
    """
    Diese Klasse ist die Elternklasse für alle Spielobjekte.
    Sie bietet einige allgemeine Methoden, die von allen Spielobjekten genutzt werden können.
    Zum Stand des Beginns des Projektes wird keine der Methoden genutzt.
    Sie können nach und nach implementiert werden, während das Spiel wächst.
    
    - gebe_namen: gibt den Namen des Sprites zurück
    - gebe_gesundheit: gibt die Gesundheit des Sprites zurück
    - setze_gesundheit(neue_energie): setzt die Gesundheit des Sprites auf den übergebenen Wert
    - hole_position: gibt die aktuelle Position des Sprites zurück
    - hole_richtung: gibt die aktuelle Bewegungsrichtung des Sprites zurück
    - setze_richtung(x,y): setzt die Bewegungsrichtung des Sprites auf die übergebenen Koordinaten
    """
    def __init__(self, name, gesundheit):
        self.name = name
        self.gesundheit = gesundheit

    def gebe_namen(self):
        """
        gibt den Namen der Spielfigur zurück
        """
        return self.name
    
    def gebe_gesundheit(self):
        """
        gibt den Gesundheitswert der Spielfigur zurück
        noch nicht implementiert
        """
        return self.gesundheit
    
    def setze_gesundheit(self,neue_energie):
        """
        ändert den Gesundheitswert der Spielfigur  
        noch nicht implementiert
        """
        self.gesundheit = neue_energie

    def hole_position(self):
        """
        gibt die aktuelle Position des Sprites zurück
        noch nicht implementiert
        """
        return self.rect.topleft
    
    def hole_richtung(self):
        """
        gibt die aktuelle Bewegungsrichtung des Sprites zurück
        noch nicht implementiert
        """
        return self.richtung
    
    def setze_richtung(self,neue_richtung):
        """
        ändert die Bewegungsrichtung des Sprites
        noch nicht implementiert
        """
        self.richtung = neue_richtung