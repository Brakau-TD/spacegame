import pygame
pygame.init()
pygame.font.init()

class Fensterdaten:
    def __init__(self):
        self.breite = 854
        self.hoehe = 480
        self.gameoverbild = "gameover.png"
        self.hintergrundbild = "hintergrund.png"
        self.bildschirm = pygame.display.set_mode((self.breite, self.hoehe))
        self.hintergrund = pygame.image.load(self.hintergrundbild).convert()
        self.schrift = pygame.font.SysFont('comicsans', 40)
        self.textfarbe = (255, 255, 255)
    
    def gebe_breite(self):
        return self.breite
    
    def gebe_hoehe(self):
        return self.hoehe
    
    def gebe_hintergrundbild(self):
        return self.hintergrund

fensterdata = Fensterdaten()

class Spielfenster(Fensterdaten):
    def __init__(self,*args,**kwargs):
        super().__init__()
        self.hintergrund = pygame.transform.scale(self.hintergrund, (self.breite,self.hoehe))
    
    def text_zeichnen(self,spielstandtext,position):
        text = self.schrift.render("Score: " + str(spielstandtext),1,self.textfarbe)
        self.bildschirm.blit(text,position)
    
    def hintergrund_zeichnen(self):
        self.bildschirm.blit(self.hintergrund,(0,0))

    def neues_hintergrund_bild(self, neues_bild):
        self.hintergrund = pygame.image.load(neues_bild).convert()
        self.hintergrund = pygame.transform.scale(self.hintergrund, (self.breite,self.hoehe))

    def gameoverbild_festlegen(self):
        self.neues_hintergrund_bild(self.gameoverbild)
    
spielfenster = Spielfenster()