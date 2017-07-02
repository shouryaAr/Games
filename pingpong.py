# Ping Pong

import pygame, sys, random, time

# Play Surface
X = 1280
Y = 800
playSurface = pygame.display.set_mode((X, Y))
pygame.display.set_caption('Ping Pong Game')
pygame.init()
time.sleep(3)

# Colors
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
brown = pygame.Color(165, 42, 42)

# FPS controller
fpsController = pygame.time.Clock()

# Variables
PadWidth = 30
PadHeight = 200
LeftPos = [0, 0, PadWidth, PadHeight]
RightPos = [X - PadWidth, 0, PadWidth, PadHeight]
BallPos = [X // 2, Y // 2]
BallRadius = 30
BallVel = [0, 0]
LEFT = False
RIGHT = True
BallSpeed = 0
PaddleSpeed = 5

def SpawnBall(direction):
    global BallPos, BallVel

    BallPos = [X // 2, Y // 2]
    BallVel[0] = -random.randrange(120, 240) // 100
    BallVel[1] = -random.randrange(60, 180) // 100

    if direction == True:
        BallVel[0] *= -1

def NewGame():
    global score1, score2

    score1 = 0
    score2 = 0
    SpawnBall(random.randrange(0, 2))

def RenderScore():
    global RenderLeft, RectLeft, RenderRight, RectRight

    pygame.init()
    Font = pygame.font.SysFont('monospace', 72)

    RenderLeft = Font.render(str(score1), True, white, black)
    RectLeft = RenderLeft.get_rect()
    RectLeft.center = (X / 4, Y / 4)

    RenderRight = Font.render(str(score2), True, white, black)
    RectRight = RenderRight.get_rect()
    RectRight.center = (X / 4 * 3, Y / 4)

NewGame()
RenderScore()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.event.post(pygame.event.Event(pygame.QUIT))

    # Paddle logic
    keys = pygame.key.get_pressed()
    if keys[ord('w')] and LeftPos[1] >= PaddleSpeed:
        LeftPos[1] -= PaddleSpeed
    if keys[ord('s')] and LeftPos[1] <= Y - PadHeight - PaddleSpeed:
        LeftPos[1] += PaddleSpeed
    if keys[pygame.K_UP] and RightPos[1] >= PaddleSpeed:
        RightPos[1] -= PaddleSpeed
    if keys[pygame.K_DOWN] and RightPos[1] <= Y - PadHeight - PaddleSpeed:
        RightPos[1] += PaddleSpeed

    # Ball logic
    BallPos[0] += BallVel[0]
    BallPos[1] += BallVel[1]

    if BallPos[0] <= BallRadius + PadWidth:
        if LeftPos[1] <= BallPos[1] <= LeftPos[1] + PadHeight:
            BallVel[0] *= -1
            BallVel[1] *= 1
            BallSpeed += 10
        else:
            SpawnBall(RIGHT)
            score2 += 1
            RenderScore()
            BallSpeed = 0

    elif BallPos[0] >= X - BallRadius - PadWidth:
        if RightPos[1] <= BallPos[1] <= RightPos[1] + PadHeight:
            BallVel[0] *= -1
            BallVel[1] *= 1
            BallSpeed += 10
        else:
            SpawnBall(LEFT)
            score1 += 1
            RenderScore()
            BallSpeed = 0

    elif BallPos[1] <= BallRadius:
        BallVel[1] = - BallVel[1]
    elif BallPos[1] >= Y - BallRadius:
        BallVel[1] = - BallVel[1]

    playSurface.fill(black)

    # Draw score
    playSurface.blit(RenderLeft, RectLeft)
    playSurface.blit(RenderRight, RectRight)

    # Draw paddles
    pygame.draw.rect(playSurface, white, pygame.Rect(LeftPos[0], LeftPos[1], LeftPos[2], LeftPos[3]))
    pygame.draw.rect(playSurface, white, pygame.Rect(RightPos[0], RightPos[1], RightPos[2], RightPos[3]))

    # Draw lines
    pygame.draw.line(playSurface, white, [X / 2, 0], [X / 2, Y], 5)
    pygame.draw.line(playSurface, white, [0 + PadWidth, 0], [0 + PadWidth, Y], 1)
    pygame.draw.line(playSurface, white, [X - PadWidth, 0], [X - PadWidth, Y], 1)

    # Draw ball
    pygame.draw.circle(playSurface, green, BallPos, BallRadius, 0)

    # Update
    pygame.display.flip()
    fpsController.tick(150 + BallSpeed)