import pygame
import random
import numpy as np
import random
import sys

# Initialiser Pygame
pygame.init()

# Définir la résolution de l'écran à celle de l'écran actuel
infoObject = pygame.display.Info()
screen_width, screen_height = infoObject.current_w, infoObject.current_h

# Créer une fenêtre en plein écran
screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)


middle_x = screen_width // 2
middle_y = screen_height // 2

count_move = 0
pair = 0

# Boucle principale
running = True
while running:

    UP = (0, -5)
    DOWN = (0, 5)
    LEFT = (-5, 0)
    RIGHT = (5, 0)
    colore = (255, 0, 0)
    col = (0, 0, 0)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:  # Appuyer sur Echap pour quitter
                pygame.quit()
                sys.exit()

    # Effacer l'écran
    screen.fill((0, 0, 0))

    start_pos = (middle_x, middle_y)
    end_pos = (middle_x, middle_y)

    while end_pos[0] <= screen_width or end_pos[1] <= screen_height:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:  # Appuyer sur Echap pour quitter
                    pygame.quit()
                    sys.exit()

                elif event.key == pygame.K_SPACE:
                    waiting = True
                    while waiting:
                        for wait_event in pygame.event.get():
                            if wait_event.type == pygame.KEYDOWN:
                                if wait_event.key == pygame.K_SPACE:
                                    waiting = False
                                elif wait_event.key == pygame.K_ESCAPE:  # Appuyer sur Echap pour quitter
                                    pygame.quit()
                                    sys.exit()
                            elif wait_event.type == pygame.QUIT:
                                pygame.quit()
                                sys.exit()


        
        values = np.random.uniform(0, 255, 3)
        color = tuple(np.round(values))

        col = ((col[0] + 10)%256, (col[1] + 10)%256, (col[2] + 10)%256)

        MoveChoice = [RIGHT, UP, LEFT, DOWN]
        move = MoveChoice[count_move % 4]
        end_pos = (start_pos[0] + move[0], start_pos[1] + move[1])
        pygame.draw.line(screen, col, start_pos, end_pos, 1)
        start_pos = end_pos

        if pair % 2 == 1:
            UP = (0, UP[1] - 5)
            DOWN = (0, DOWN[1] + 5)
            LEFT = (LEFT[0] - 5, 0)
            RIGHT = (RIGHT[0] + 5, 0)

        count_move += 1
        pair += 1

        pygame.display.flip()
        pygame.time.delay(5)  # Ajout d'un délai de 0.5 seconde

# Quitter Pygame
pygame.quit()
