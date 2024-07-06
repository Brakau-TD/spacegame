from grafiken import *

pygame.init()



# Rechtecke erstellen
# die Rechtecke werden in einer Liste gespeichert
# wichtig sind eigentlich nur die Startkoordinaten (x,y), 
# die in den ersten beiden Werten angegeben werden (z.B. 100, 100)
# die Rechtecke werden nicht gezeichnet, sondern dienen nur dazu,
# die Koordinaten für die Asteroide o.#. zu speichern
rects = [
    pygame.Rect(100, 100, 50, 50),
    pygame.Rect(200, 200, 50, 50),
    pygame.Rect(300, 300, 50, 50),
    pygame.Rect(10, 100, 50, 50),
    pygame.Rect(20, 200, 50, 50),
    pygame.Rect(30, 300, 50, 50),
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
    for rect in rects:
        if rect.colliderect(pointer_rect):
            rects.remove(rect)

    # Zeichnet die Hintergrundgrafik und die Asteroiden
    bildschirm.blit(hintergrund, (0, 0))
    for i, rect in enumerate(rects):
        rect.x += richtung[i][0]
        rect.y += richtung[i][1]
        bildschirm.blit(asteroid, (rect.x, rect.y))
        if rect.x > 854:
            rects.remove(rect)

    bildschirm.blit(roboter, mouse_pos)

    clock.tick(60)
    # Das Bild wird aktualisiert
    pygame.display.update()

pygame.quit()
