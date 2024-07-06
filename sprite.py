from pygame.locals import *
from spielfenster import fensterdata
from grundobjekt import Grundobjekt

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
    def __init__(self, x,y,breite,hoehe,richtung,bildpfad,name,gesundheit,energie,speed):
        super().__init__(x,y,breite,hoehe,richtung,bildpfad,name,speed)
        self.fensterdata = fensterdata
        self.gesundheit = gesundheit # Gesundheits-Wert des Sprites. Damit können wir bestimmt später noch was anfangen
        self.energie = energie # Energie-Wert des Sprites. Damit können wir bestimmt später noch was anfangen

    def ist_ausserhalb(self):
        """
        prueft, ob das Sprite aus dem Spielfeld heraus ist und setzt es gegebenenfalls wieder hinein
        """
        if self.rect.x > self.fensterdata.gebe_breite():
            self.rect.x = - self.breite
        elif self.rect.x < -self.breite:
            self.rect.x = self.fensterdata.gebe_breite()
        if self.rect.y > self.fensterdata.gebe_hoehe():
            self.rect.y = - self.hoehe
        elif self.rect.y < - self.hoehe:
            self.rect.y = self.fensterdata.gebe_hoehe()

    def gebe_gesundheit(self):
        """
        gibt den Gesundheitswert der Spielfigur zurück
        noch nicht implementiert
        """
        return self.gesundheit
    
    def setze_gesundheit(self,neue_gesundheit):
        """
        ändert den Gesundheitswert der Spielfigur  
        noch nicht implementiert
        """
        self.gesundheit = neue_gesundheit

    def gebe_energie(self):
        """
        gibt den Energie-Wert der Spielfigur zurück
        """
        return self.energie
    
    def setze_energie(self,neue_energie):
        """
        ändert den Energie-Wert der Spielfigur  
        """
        self.energie = neue_energie


# du willst mehr als einen Gegner? Dann kannst du das hier machen
# gebe der Gegnerliste einfach mehrere Gegner hinzu, die du so erstellst wie unten
# z.B. gegnerliste = [gegner1,gegner2] und so weiter
# du willst eigene Sprites erstellen? Dann kannst du das hier machen
# gehe auf https://www.piskelapp.com/p/create/sprite und erstelle dir ein eigenes Sprite -> die Größe ist dort 32x32 Pixel,
# du kannst aber auch eine andere Größe wählen, wenn du das Bild dann in der Größe anpasst
# speichere das Sprite als .png Datei in den Programmordner
# und erstelle ein neues Sprite-Objekt mit den gewünschten Parametern
# experimentiere mit den x,y Koordinaten, der Größe, der Richtung, der Geschwindigkeit, der Gesundheit und der Energie
# die Richtungen funktionieren so: (1,0) bewegt sich das Sprite nach rechts, (0,1) bewegt sich das Sprite nach unten
# (1,1) bewegt sich das Sprite diagonal nach rechts unten, (-1,0) bewegt sich das Sprite nach links
# (-1,-1) bewegt sich das Sprite diagonal nach links oben, (0,-1) bewegt sich das Sprite nach oben
# wenn du Dezimalzahlen benutzt, bewegt sich das Sprite schräger

gegner1 = Sprite(x= 100,y= 100,breite = 50,hoehe = 50,richtung = (1,1),bildpfad = "asteroid_1.png",name = "Asteroid_1", gesundheit = 25,energie = 50,speed = 2)
#gegner2 = Sprite(x= 80,y= 30,breite = 50,hoehe = 50,richtung = (1,.5),bildpfad = "asteroid_2.png",name = "Runderoid", gesundheit = 25,energie = 50,speed = 1)
gegnerliste = [gegner1]
gegnersprites = gegnerliste
spielersprite = Sprite(x= 100,y= 100,breite = 64,hoehe = 64,richtung = (0,0),bildpfad = "spielerbild.png",name = "spieler", gesundheit=100,energie = 50,speed = 1)
anderesprites = []