import pygame
from pygame.locals import *
from spielfenster import pygame,fensterdata
from grundobjekt import Grundobjekt

# Bilder für die Sprites
spielerbild = "roboter.png"
asteroid_1_bild = "asteroid.png"
asteroid_2_bild = "asteroid2.png"

roboter_bild = pygame.image.load(spielerbild).convert_alpha()
roboter = pygame.transform.scale(roboter_bild, (64, 64))

asteroid_sprite = pygame.image.load(asteroid_1_bild).convert_alpha()
asteroid = pygame.transform.scale(asteroid_sprite, (64, 64))

asteroid2_sprite = pygame.image.load(asteroid_2_bild).convert_alpha()
asteroid2 = pygame.transform.scale(asteroid2_sprite, (64,64))
# Ende der Bilder für die Sprites

class Sprite(Grundobjekt):
    """
    Diese Klasse erzeugt ein Sprite (Spielfigur) und setzt dessen Position, Größe, Gesundheit und Bewegungsrichtung.
    Jedes Spielobjekt kann folgende Methoden ausführen:
    - zeichnen: zeichnet das Sprite auf das Spielfenster
    - neue_position_rechnen: berechnet die neue Position des Sprites, wenn dies ein NPC ist
    - neue_position_setzen(x,y): setzt die Position des Sprites auf die übergebenen Koordinaten
    - ist_ausserhalb: prüft, ob das Sprite aus dem Spielfeld heraus ist und setzt es gegebenenfalls wieder hinein
    - ist_kollision(spielerposition): prüft, ob es eine Kollision mit einem anderen Sprite gibt
    
    Diese Klasse erbt von der Klasse Grundobjekt, die weitere Methoden für alle Spielobjekte bereitstellt.
    
    """
    def __init__(self, x,y,breite,hoehe,richtung,bildpfad,name,gesundheit):
        super().__init__(name,gesundheit)
        self.breite = breite
        self.hoehe = hoehe
        self.spritebild = pygame.image.load(bildpfad).convert_alpha()
        self.rect = self.scale(breite,hoehe)
        if self.name != "spieler":
            self.richtung = richtung # (x,y) - Richtung in der sich das Sprite bewegt. (0,0) steht für keine Bewegung, (1,0) für Bewegung nach rechts, (0,1) für Bewegung nach unten, etc.
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
        
    def ist_ausserhalb(self):
        """
        prueft, ob das Sprite aus dem Spielfeld heraus ist und setzt es gegebenenfalls wieder hinein
        """
        if self.rect.x > fensterdata.gebe_breite():
            self.rect.x = - self.breite
        elif self.rect.x < -self.breite:
            self.rect.x = fensterdata.gebe_breite()
        if self.rect.y > fensterdata.gebe_hoehe():
            self.rect.y = - self.hoehe
        elif self.rect.y < - self.hoehe:
            self.rect.y = fensterdata.gebe_hoehe()
    
    def ist_kollision(self, spieler):
        """
        prüft, ob es eine Kollision mit einem anderen Sprite gibt
        """
        if self.rect.colliderect(spieler):
            return True
        else:
            return False      

gegnerliste = []
gegneranzahl = 1
gegnername = "asteroid"+str(gegneranzahl)
gegnersprites = Sprite(x= 100,y= 100,breite = 50,hoehe = 50,richtung = (1,1),bildpfad = "asteroid.png",name = gegnername, gesundheit = 25)
spielersprite = Sprite(x= 100,y= 100,breite = 64,hoehe = 64,richtung = (0,0),bildpfad = "roboter.png",name = "spieler", gesundheit=100)