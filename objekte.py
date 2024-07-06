import pygame
from pygame.locals import *
from optionen import *

class Sprite(pygame.sprite.Sprite):
    def __init__(self, x,y,breite,hoehe,richtung,bildpfad, name, energie):
        super().__init__()
        self.breite = breite
        self.hoehe = hoehe
        self.name = name
        self.energie = energie
        self.spritebild = pygame.image.load(bildpfad).convert_alpha()
        self.rect = self.scale(breite,hoehe)
        self.richtung = richtung
        self.rect.topleft = (x,y)

    def gebe_namen(self):
        return self.name
    
    def gebe_energie(self):
        return self.energie
    
    def setze_energie(self,neue_energie):
        self.energie = neue_energie
        
    def scale(self,breite,hoehe):
        self.spritebild = pygame.transform.scale(self.spritebild, (breite,hoehe))
        return self.spritebild.get_rect()
        
    def zeichnen(self, fenster):
        fenster.bildschirm.blit(self.spritebild, self.rect)
        
    def neue_position_rechnen(self):
        self.rect.x += self.richtung[0]
        self.rect.y += self.richtung[1]
        self.rect.topleft = (self.rect.x,self.rect.y)
        
    def neue_position_setzen(self,x,y):
        self.rect.x = x
        self.rect.y = y
        self.rect.topleft = (x,y)
        
    def hole_position(self):
        return self.rect.topleft
    
    def hole_richtung(self):
        return self.richtung
    
    def setze_richtung(self,neue_richtung):
        self.richtung = neue_richtung
        
    def ist_ausserhalb(self):
        if self.rect.x > fensterbreite:
            self.rect.x = - self.breite
        elif self.rect.x < -self.breite:
            self.rect.x = fensterbreite
        if self.rect.y > fensterhoehe:
            self.rect.y = - self.hoehe
        elif self.rect.y < - self.hoehe:
            self.rect.y = fensterhoehe
    
    def ist_kollision(self, spieler):
        if self.rect.colliderect(spieler):
            return True
        else:
            return False      

gegnerliste = []
gegneranzahl = 1
gegnername = "asteroid"+str(gegneranzahl)
gegnersprites = Sprite(x= 100,y= 100,breite = 50,hoehe = 50,richtung = (1,1),bildpfad = "asteroid.png",name = gegnername, energie = 25)
spielersprite = Sprite(x= 100,y= 100,breite = 64,hoehe = 64,richtung = (0,0),bildpfad = "roboter.png",name = "spieler", energie=100)