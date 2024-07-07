import pygame
import random

pygame.init()

# Constants
WIDTH, HEIGHT = 900, 600
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

# Set up the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")
clock = pygame.time.Clock()
FPS = 30

# Striker class
class Striker:
    def __init__(self, posx, posy, width, height, speed, color):
        self.posx = posx
        self.posy = posy
        self.width = width
        self.height = height
        self.speed = speed
        self.color = color
        self.bewegung = 0
        self.alte_position = [0,0]
        self.geekRect = pygame.Rect(posx, posy, width, height)

    def display(self):
        pygame.draw.rect(screen, self.color, self.geekRect)

    def update(self, yFac):
        self.bewegung = yFac
        self.posy += self.speed * yFac
        if self.posy <= 0:
            self.posy = 0
        elif self.posy + self.height >= HEIGHT:
            self.posy = HEIGHT - self.height
        self.geekRect = (self.posx, self.posy, self.width, self.height)

    def in_bewegung(self):
        pass


class Ball:
    def __init__(self, posx, posy, radius, speed, color):
        self.posx = posx
        self.posy = posy
        self.radius = radius
        self.speed = speed
        self.farbe = color
        self.richtung = [1,0]
        self.player1_score = 0
        self.player2_score = 0
        self.spielerpedal = pygame.Rect(posx, posy, radius, radius)
    
    def display(self):
        pygame.draw.circle(screen, self.farbe, (self.posx, self.posy), self.radius)

    def kollision(self, striker):
        if self.spielerpedal.colliderect(striker.geekRect):
            self.richtung[0] *= -1
            self.richtung[1] = striker.bewegung
    
    def update(self):
        self.posx += self.speed * self.richtung[0]
        if self.posx <= 0 or self.posx >= WIDTH:  
            if self.posx <= 0:
                self.player1_score += 1
            else:
                self.player2_score += 1
            
            self.richtung[1] += random.uniform(-0.2, 0.2)  
            self.richtung[1] = max(min(self.richtung[1], 1), -1)
            
            self.richtung[0] *= -1
        self.spielerpedal.x = round(self.posx)
        
        self.posy += self.speed * self.richtung[1]
        if self.posy <= 0 or self.posy >= HEIGHT: 
            self.richtung[1] *= -1
        self.spielerpedal.y = round(self.posy)

# Spielfiguren erstellen
pedallinks = Striker(posx=20, posy=HEIGHT // 2 - 50, width=10, height=100, speed=10, color=WHITE)
pedalrechts = Striker(posx=WIDTH - 30, posy=HEIGHT // 2 - 50, width=10, height=100, speed=10, color=WHITE)
ball = Ball(posx=WIDTH // 2, posy=HEIGHT // 2, radius=10, speed=5, color=GREEN)

def punktestand_zeichnen(player1_score, player2_score):
    """
    hier musst du eigenen code schreiben, um den Punktestand zu zeichnen
    google nach pygame draw text oder pygame zeichne text
    """
    pass

def spiel_spielen():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        bewegung = 0
        if keys[pygame.K_w]:
            bewegung = -1
        elif keys[pygame.K_s]:
            bewegung = 1
        else: 
            bewegung = 0
        pedallinks.update(bewegung)

        bewegung = 0
        if keys[pygame.K_UP]:
            bewegung = -1
        elif keys[pygame.K_DOWN]:
            bewegung = 1
        else: 
            bewegung = 0
        pedalrechts.update(bewegung)

        # Bildschirm löschen
        screen.fill(BLACK)

        # Update ball position
        player2_score = ball.kollision(pedallinks)
        player1_score = ball.kollision(pedalrechts)
        ball.update()
        ball.display()
        # Spieler"figuren" zeichnen
        pedallinks.display()
        pedalrechts.display()

        punktestand_zeichnen(player1_score, player2_score)

        # Bildschirm aktualisieren
        pygame.display.flip()
        clock.tick(FPS)

spiel_spielen()
pygame.quit()