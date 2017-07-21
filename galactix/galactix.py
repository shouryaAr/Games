# Galactix

import pygame, sys, random, time, os

# Play Surface
X = 1280
Y = 800
playSurface = pygame.display.set_mode((X, Y))
pygame.display.set_caption('Galactix Game')
pygame.init()
#time.sleep(3)

# Colors
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
brown = pygame.Color(165, 42, 42)

# FPS controller
fpsController = pygame.time.Clock()

# Variables
GameDir = os.path.dirname(os.path.realpath(sys.argv[0]))

class ImageInfo:
    def __init__(self, center, size, radius = 0, lifespan = None, animated = False):
        self.center = center
        self.size = size
        self.radius = radius
        if lifespan:
            self.lifespan = lifespan
        else:
            self.lifespan = float('inf')
        self.animated = animated

    def get_center(self):
        return self.center

    def get_size(self):
        return self.size

    def get_radius(self):
        return self.radius

    def get_lifespan(self):
        return self.lifespan

    def get_animated(self):
        return self.animated

ShipImage = pygame.image.load(GameDir+'\double_ship.png')
ShipImageRect = ShipImage.get_rect()
print(ShipImageRect[2])
ShipImageRect.center = (X/2, Y/2)
ShipInfo = ImageInfo([45, 45], [90, 90], 35)
print(GameDir+'\double_ship.png')

# Ship class
class Ship:
 
    def __init__(self, pos, vel, angle, image, info):
        self.pos = [pos[0], pos[1]]
        self.vel = [vel[0], vel[1]]
        self.thrust = False
        self.angle = angle
        self.angle_vel = 0
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()
 
    def draw(self, canvas):
        if self.thrust:
            playSurface.blit(MyShipImage, MyShipImageRect, (MyShipImageRect[2]/2, 0, MyShipImageRect[2], MyShipImageRect[3]))
        else:
            playSurface.blit(MyShipImage, MyShipImageRect, (0, 0, MyShipImageRect[2]/2, MyShipImageRect[3]))
        # canvas.draw_circle(self.pos, self.radius, 1, "White", "White")
        
    def update(self):
        # update angle
        self.angle += self.angle_vel
 
        # update position
        self.pos[0] = (self.pos[0] + self.vel[0]) % WIDTH
        self.pos[1] = (self.pos[1] + self.vel[1]) % HEIGHT
 
        # update velocity
        if self.thrust:
            acc = angle_to_vector(self.angle)
            self.vel[0] += acc[0] * .1
            self.vel[1] += acc[1] * .1
 
        self.vel[0] *= .99
        self.vel[1] *= .99
 
    def set_thrust(self, on):
        self.thrust = on
        #if on:
            #ship_thrust_sound.rewind()
            #ship_thrust_sound.play()
        #else:
            #ship_thrust_sound.pause()
 
    def increment_angle_vel(self):
        self.angle_vel += .05
 
    def decrement_angle_vel(self):
        self.angle_vel -= .05

MyShip = Ship([X / 2, Y / 2], [0, 0], 0, ShipImage, ShipInfo)
MyShipImage = getattr(MyShip, 'image')
MyShipImageRect = MyShipImage.get_rect()
print(MyShipImageRect)
MyShipImageRect.center = (X/2, Y/2)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.event.post(pygame.event.Event(pygame.QUIT))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
       MyShip.set_thrust(True)
    if keys[pygame.K_LEFT]:
       MyShip.increment_angle_vel()
    if keys[pygame.K_RIGHT]:
       MyShip.decrement_angle_vel()
                
    playSurface.fill(black)
    playSurface.blit(MyShipImage, MyShipImageRect, (0, 0, MyShipImageRect[2]/2, MyShipImageRect[3]))
    pygame.display.flip()
