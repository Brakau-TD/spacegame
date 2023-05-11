from grafiken import *
import os

pygame.init()
pygame.font.init()

schrift = pygame.font.SysFont('comicsans', 40)

WHITE = (255, 255, 255)

# Create rectangles
# the rectangles are stored in a list
# only the starting coordinates (x,y) are important, 
# which are specified in the first two values (e.g. 100, 100)
# the rectangles are not drawn, but only serve to
# save the coordinates for the asteroids or similar
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


# set directions for each sprite
# there have to be as many direction-tuples as there are sprites
richtung = [
    (1, 1),
    (-1, 0),
    (0, -1),
    (1, 1),
    (-1, 0),
    (0, -1),
]

# setting an image to the mouse-pointer
pointer_rect = pygame.Rect(pygame.mouse.get_pos(), (20, 20))

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    mouse_pos = pygame.mouse.get_pos()
    pointer_rect = pygame.Rect(mouse_pos, (50, 50))

   #collision detection for asteroids
    for i, rect in enumerate(rects):
        if rect.colliderect(pointer_rect):
            rects.remove(rect)
            richtung.pop(i)
            score = score + bilder[i][1]
            bilder.pop(i)
            print(score)

    # draw the background
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

    pygame.display.update()

pygame.quit()
