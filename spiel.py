from grafiken import *
import os

pygame.init()
pygame.font.init()

schrift = pygame.font.SysFont('comicsans', 40)

WHITE = (255, 255, 255)

# Rechtecke erstellen
# die Rechtecke werden in einer Liste gespeichert
# wichtig sind eigentlich nur die Startkoordinaten (x,y), 
# die in den ersten beiden Werten angegeben werden (z.B. 100, 100)
# die Rechtecke werden nicht gezeichnet, sondern dienen nur dazu,
# die Koordinaten für die Asteroide o.ä. zu speichern
rects = [
    pygame.Rect(100, 100, 50, 50),
    pygame.Rect(200, 200, 50, 50),
    pygame.Rect(300, 300, 50, 50),
    pygame.Rect(10, 100, 50, 50),
    pygame.Rect(20, 200, 50, 50),
    pygame.Rect(30, 300, 50, 50),
]

score = 0

bilder = [
    [asteroid,5],
    [asteroid,5],
    [asteroid2,-10],
    [asteroid,5],
    [asteroid,5],
    [asteroid2,-10]
]


# Richtungen festlegen
# es müssen so viele Richtungen festgelegt werden, wie ihr Rechtecke in Rects habt
richtung = [
    (1, 1),
    (-1, 0),
    (0, -1),
    (1, 1),
    (-1, 0),
    (0, -1),
]

# das Bild für den Mauszeiger an der Mausposition festlegem
pointer_rect = pygame.Rect(pygame.mouse.get_pos(), (20, 20))

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    mouse_pos = pygame.mouse.get_pos()
    pointer_rect = pygame.Rect(mouse_pos, (50, 50))

    # Überprüfung der Kollision: berührt der Mauszeiger einen
    # Asteroiden? Wenn ja, dann wird der Asteroid aus der Liste entfernt
    for i, rect in enumerate(rects):
        if rect.colliderect(pointer_rect):
            rects.remove(rect)
            richtung.pop(i)
            score = score + bilder[i][1]
            bilder.pop(i)
            print(score)

    # Zeichnet die Hintergrundgrafik und die Asteroiden
    bildschirm.blit(hintergrund, (0, 0))

    for i, rect in enumerate(rects):
        rect.x += richtung[i][0]
        rect.y += richtung[i][1]

        bildschirm.blit(bilder[i][0], (rect.x, rect.y))

        if rect.x > 854:
            rect.x = - 64
        elif rect.x < -64:
            rect.x = 854
        if rect.y > 480:
            rect.y = - 64
        elif rect.y < -64:
            rect.y = 480

    bildschirm.blit(roboter, mouse_pos)

    scoretext = schrift.render("Score: " + str(score),1,WHITE)
    bildschirm.blit(scoretext,(20, 20))

    clock.tick(60)
    # Das Bild wird aktualisiert
    pygame.display.update()

pygame.quit()
