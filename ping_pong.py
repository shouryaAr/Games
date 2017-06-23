# Ping Pong

import pygame, sys, random, time

# Play Surface
X = 1280
Y = 800
playSurface = pygame.display.set_mode((X, Y))
pygame.display.set_caption('Ping Pong Game')
#time.sleep(5)

# Colors
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
brown = pygame.Color(165, 42, 42)

# FPS controller
fpsController = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.event.post(pygame.event.Event(pygame.QUIT))
            
    playSurface.fill(white)
    pygame.draw.rect(playSurface, green, pygame.Rect(50, 50, 100, 100))
    pygame.display.flip()  # update
    fpsController.tick(25)
