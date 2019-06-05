import pygame
from pygame.locals import *
import os
import sys
import math

os.environ["SDL_VIDEO_CENTERED"] = "1"
pygame.init()
pygame.font.init()
clock = pygame.time.Clock()
myfont = pygame.font.SysFont('sourcecodeproblack', 12)

BLACK = [0, 0, 0]
WHITE = [255, 255, 255]
WALLS = [220, 40, 30]

SIZE = [240, 240]
DSIZE = [480, 480]
TSIZE = [720, 720]

dub = False
trip = False

def normal():
    global screen
    screen = pygame.display.set_mode(SIZE)
    pygame.display.set_caption("METAL PACKET")

def full():
    global screen
    screen = pygame.display.set_mode((SIZE), pygame.FULLSCREEN)
    pygame.display.set_caption("METAL PACKET: Fullscreen Edition")

def doubled():
    global screen
    global window
    global res
    global invscale
    invscale = 1/2
    res = DSIZE
    window = pygame.display.set_mode(DSIZE)
    screen = pygame.Surface(SIZE)
    pygame.display.set_caption("METAL PACKET: Double Boogaloo")

def doubledfull():
    global screen
    global window
    global res
    global invscale
    invscale = 1/2
    res = DSIZE
    window = pygame.display.set_mode((DSIZE), pygame.FULLSCREEN)
    screen = pygame.Surface(SIZE)
    pygame.display.set_caption("METAL PACKET: Fullscreen Boogaloo")

def tripled ():
    global screen
    global window
    global res
    global invscale
    invscale = 1/3
    res = TSIZE
    window = pygame.display.set_mode(TSIZE)
    screen = pygame.Surface(SIZE)
    pygame.display.set_caption("METAL PACKET: Trifecta of Resolution")

def tripledfull ():
    global screen
    global window
    global res
    global invscale
    invscale = 1/3
    res = TSIZE
    window = pygame.display.set_mode((TSIZE), pygame.FULLSCREEN)
    screen = pygame.Surface(SIZE)
    pygame.display.set_caption("METAL PACKET: Fullscreen Trifecta Edition")

print("")
print("1: 240 x 240")
print("2: 480 x 480")
print("3: 720 x 720")
print("4: 240 x 240 Fullscreen")
print("5: 480 x 480 Fullscreen")
print("6: 720 x 720 Fullscreen")
print("")
res = input("Choose a video mode. ")
if res == ("1"):
    normal()
if res == ("2"):
    doubled()
    dub = True
if res == ("3"):
    tripled()
    trip = True
if res == ("4"):
    full()
if res == ("5"):
    doubledfull()
    dub = True
if res == ("6"):
    tripledfull()
    trip = True

class Walls(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.currentsprite = ()
    def draw(self):
        self.image = pygame.image.load(self.currentsprite)
        screen.blit(self.image, [0, 0])

room1 = Walls()
room1.currentsprite = ("room1.png")

collidelist = pygame.sprite.Group()

class WallColliders(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self, collidelist)
        self.rectval = []
    def collide(self):
        self.rect = (self.rectval)

topwall = WallColliders()
topwall.rectval = [0, 0, 240, 17]
bottomwall = WallColliders()
bottomwall.rectval = [0, 158, 240, 20]
leftwall = WallColliders()
leftwall.rectval = [0, 0, 14, 180]

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.collide = 0
        self.x = 0
        self.y = 0
        self.speed = 0
        self.currentsprite = ("char_arm.png")
        self.body = pygame.image.load("char.png")
        self.image = pygame.image.load(self.currentsprite)
        self.rect = self.image.get_rect()
    def collidedetect(self):
        if pygame.sprite.spritecollideany(player, collidelist):
            self.collide = 1
        else:
            self.collide = 0
    def move(self):
        key = pygame.key.get_pressed()
        if key[K_LEFT] or key[ord("a")]:
                self.x -= self.speed
        if key[K_RIGHT] or key[ord("d")]:
                self.x += self.speed
        if key[K_UP] or key[ord("w")]:
                self.y -= self.speed
        if key[K_DOWN] or key[ord("s")]:
                self.y += self.speed
        self.updaterect()
    def rotate(self):
        pos = pygame.mouse.get_pos()
        if dub == True or trip == True:
            pos = pos[0] * invscale, pos[1] * invscale
            mouse_x, mouse_y = pos
        mouse_x, mouse_y = pos
        rel_x, rel_y = mouse_x - self.x, mouse_y - self.y
        self.angle = (180 / math.pi) * -math.atan2(rel_y, rel_x) 
        self.rotimage = pygame.transform.rotate(self.image, self.angle)
        self.rect = self.rotimage.get_rect(center = (self.rect.center))
    def monitor(self):
        textsurface = myfont.render(str(int(self.angle)), False, (255, 255, 255))
        screen.blit(textsurface,(50,210))
    def draw(self):
        screen.blit(self.body, [self.x + 5, self.y + 1])
        screen.blit(self.rotimage, self.rect)
    def updaterect(self):
        self.rect = pygame.Rect(self.x, self.y, 20, 20)
    def moveandcollide(self):
        pos = (self.x, self.y)
        self.move()
        self.collidedetect()
        if player.collide:
            self.x, self.y = pos
            self.updaterect()
            self.collide = False

player = Player()
player.x = 29
player.y = 89
player.speed = 2

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            print("")
            print("See you next time.")
            pygame.quit()
            sys.exit(0)
            done = True

    screen.fill(BLACK)

    room1.draw()

    for x in collidelist:
        x.collide()

    player.moveandcollide()
    player.rotate()
    player.monitor()   
    player.draw()

    if dub == True or trip == True:        
        pygame.transform.scale(screen, res, window)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
