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
    def __init__(self, x,y,breite,hoehe,richtung,bildpfad,name):
        self.name = name
        self.breite = breite
        self.hoehe = hoehe
        self.spritebild = pygame.image.load(bildpfad).convert_alpha()
        self.rect = self.scale(breite,hoehe)
        if self.name != "spieler":
            self.richtung = richtung
        self.rect.topleft = (x,y)
    
    def scale(self,breite,hoehe):
        """
        vergrößert oder verkleinert das Spritebild auf die übergebenen Maße
        """
        self.spritebild = pygame.transform.scale(self.spritebild, (breite,hoehe))
        return self.spritebild.get_rect()
        
    def zeichnen(self, fensterobjekt):
        """
        zeichnet das Sprite auf das Spielfenster
        """
        fensterobjekt.bildschirm.blit(self.spritebild, self.rect)
        
    def neue_position_rechnen(self):
        """
        errechnet eine neue Position für das Sprite, wenn dieses sich bewegen soll
        """
        self.rect.x += self.richtung[0]
        self.rect.y += self.richtung[1]
        self.rect.topleft = (self.rect.x,self.rect.y)
        
    def neue_position_setzen(self,x,y):
        """
        setzt eine neue Position für das Sprite
        """
        self.rect.x = x
        self.rect.y = y
        self.rect.topleft = (x,y)
        
    def ist_kollision(self, spieler):
        """
        prüft, ob es eine Kollision mit einem anderen Sprite gibt
        """
        if self.rect.colliderect(spieler):
            return True
        else:
            return False      

    def gebe_namen(self):
        """
        gibt den Namen der Spielfigur zurück
        """
        return self.name

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