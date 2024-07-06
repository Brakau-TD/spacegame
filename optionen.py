import pygame
pygame.init()
pygame.font.init()
schrift = pygame.font.SysFont('comicsans', 40)

textfarbe = (255, 255, 255)
fensterbreite = 854
fensterhoehe = 480
spielerbild = "roboter.png"
bildpfad = "hintergrund.png"
gameoverbild = "gameover.jpg"
asteroid_1_bild = "asteroid.png"
asteroid_2_bild = "asteroid2.png"

bildschirm = pygame.display.set_mode((854, 480))

roboter_bild = pygame.image.load(spielerbild).convert_alpha()
roboter = pygame.transform.scale(roboter_bild, (64, 64))

asteroid_sprite = pygame.image.load(asteroid_1_bild).convert_alpha()
asteroid = pygame.transform.scale(asteroid_sprite, (64, 64))

asteroid2_sprite = pygame.image.load(asteroid_2_bild).convert_alpha()
asteroid2 = pygame.transform.scale(asteroid2_sprite, (64,64))

class Spielfenster:
    def __init__(self, breite, hoehe, bild):
        self.bildschirm = pygame.display.set_mode((breite, hoehe))
        self.hintergrundbild = pygame.image.load(bild).convert()
        self.hintergrund = pygame.transform.scale(self.hintergrundbild, (breite,hoehe))
    
    def text_zeichnen(self,spielstandtext,position):
        text = schrift.render("Score: " + str(spielstandtext),1,textfarbe)
        self.bildschirm.blit(text,position)
    
    def hintergrund_zeichnen(self):
        self.bildschirm.blit(self.hintergrund,(0,0))

    def neues_hintergrund_bild(self, bild):
        self.hintergrundbild = pygame.image.load(bild).convert()
        self.hintergrund = pygame.transform.scale(self.hintergrundbild, (fensterbreite,fensterhoehe))
    
spielfenster = Spielfenster(fensterbreite,fensterhoehe, bildpfad)