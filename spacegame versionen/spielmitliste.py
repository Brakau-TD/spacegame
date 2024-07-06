import pygame

pygame.init()

# erzeugt das Spielfenster
screen = pygame.display.set_mode((800, 600))

# Eine Liste von Rechtecken [x-Position, y-Position, Breite, Höhe]
rects = [
    pygame.Rect(100, 100, 50, 50),
    pygame.Rect(200, 200, 50, 50),
    pygame.Rect(300, 300, 50, 50),
]

def spiel():
    """
    diese Funktion enthält die gesamte "Logik" des Spiels, 
    also das, was passiert, wenn das Spiel läuft
    Hier beginnt der sogenannte "Game Loop", 
    also die Schleife, die das Spiel am Laufen hält
    die Schleife findet ab dem Befehl "while" statt und endet, 
    wenn die Variable "running" auf "False" gesetzt wird
    """
    pygame.mouse.set_visible(False) # Macht den Mauszeiger unsichtbar
    running = True
    while running:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # holt die Position der Maus
            mouse_pos = pygame.mouse.get_pos()
            pointer_rect = pygame.Rect(mouse_pos, (10, 10))

            # Prüft ob die Maus auf ein Rechteck zeigt
            for rect in rects:
                if rect.collidepoint(mouse_pos):
                    print("Collision detected!")
                    rects.remove(rect)

            # Zeichnet ein Rechteck an der Mausposition und an den Positionen der Rechtecke
            screen.fill((255, 255, 255))
            for rect in rects:
                pygame.draw.rect(screen, (255, 0, 0), rect)
            pygame.draw.rect(screen,(0,0,0), pointer_rect)

            # Erneuert das Display
            pygame.display.update()

    pygame.quit()

spiel()