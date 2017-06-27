# Ping Pong

import pygame, sys, random, time

# Play Surface
X = 1280
Y = 800
playSurface = pygame.display.set_mode((X, Y))
pygame.display.set_caption('Ping Pong Game')
# time.sleep(5)

# Colors
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
brown = pygame.Color(165, 42, 42)

# FPS controller
fpsController = pygame.time.Clock()

# Variables
PadWidth = 100
PadHeight = 300
LeftPos = [0, 0, PadWidth, PadHeight]
RightPos = [X-100, 0, PadWidth, PadHeight]
BallPos = [X//2, Y//2]
BallRadius = 30
BallVel = [0, 0]
Spawn = random.randrange(0,2)
BallVel[0] = -random.randrange(120, 240) // 100
BallVel[1] = -random.randrange(60, 180) // 100
if Spawn == True:
    BallVel[0] *= -1


while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.event.post(pygame.event.Event(pygame.QUIT))

    keys = pygame.key.get_pressed()
    if keys[ord('w')] and LeftPos[1]>=10:
        LeftPos[1] -= 10
    if keys[ord('s')] and LeftPos[1]<=Y-310:
        LeftPos[1] += 10
    if keys[pygame.K_UP] and RightPos[1]>=10:
        RightPos[1] -= 10
    if keys[pygame.K_DOWN] and RightPos[1]<=Y-310:
        RightPos[1] += 10

    BallPos[0] += BallVel[0]
    BallPos[1] += BallVel[1]

    if BallPos[0] <= BallRadius + PadWidth:
        if LeftPos[1] <= BallPos[1] <= LeftPos[1]+PadHeight:
            BallVel[0] *= -1
            BallVel[1] *= 1

    elif BallPos[0] >= X - BallRadius - PadWidth:
        if RightPos[1] <= BallPos[1] <= RightPos[1]+PadHeight:
            BallVel[0] *= -1
            BallVel[1] *= 1

    elif BallPos[1] <= BallRadius:
        BallVel[1] = - BallVel[1]
    elif BallPos[1] >= Y - BallRadius:
        BallVel[1] = - BallVel[1]

    playSurface.fill(white)
    pygame.draw.rect(playSurface, green, pygame.Rect(LeftPos[0], LeftPos[1], LeftPos[2], LeftPos[3]))
    pygame.draw.rect(playSurface, green, pygame.Rect(RightPos[0], RightPos[1], RightPos[2], RightPos[3]))
    pygame.draw.circle(playSurface, red, BallPos, BallRadius, 0)
    pygame.display.flip()  # update
    fpsController.tick(60)