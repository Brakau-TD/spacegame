import pygame
bildschirm = pygame.display.set_mode((854, 480))

hintergrund_bild = pygame.image.load("hintergrund.png").convert()
hintergrund = pygame.transform.scale(hintergrund_bild, (854, 480))

roboter_bild = pygame.image.load("roboter.png").convert_alpha()
roboter = pygame.transform.scale(roboter_bild, (64, 64))

asteroid_bild = pygame.image.load("asteroid.png").convert_alpha()
asteroid = pygame.transform.scale(asteroid_bild, (64, 64))

asteroid2_bild = pygame.image.load("asteroid2.png").convert_alpha()
asteroid2 = pygame.transform.scale(asteroid2_bild, (64,64))

# pixilart