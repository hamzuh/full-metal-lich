import os
import sys
import pygame
from pygame.locals import *
import math
import random

pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()
os.environ["SDL_VIDEO_CENTERED"] = "1"
clock = pygame.time.Clock()
pygame.font.init()
font = pygame.font.SysFont("impact", 18)

shot = pygame.mixer.Sound("music/shot.wav")
pause = pygame.mixer.Sound("music/pause.wav")
playerhit = pygame.mixer.Sound("music/playerhit.wav")
enemyhit = pygame.mixer.Sound("music/enemyhit.wav")
enemydeath = pygame.mixer.Sound("music/enemydeath.wav")
wallhit = pygame.mixer.Sound("music/wallhit.wav")
win = pygame.mixer.Sound("music/win.wav")
pickup = pygame.mixer.Sound("music/pickup.wav")
footstep = pygame.mixer.Sound("music/step.wav")
gateopen = pygame.mixer.Sound("music/gateopen.wav")
gateclose = pygame.mixer.Sound("music/gateclose.wav")

SIZE = [240, 240]
DSIZE = [480, 480]
TSIZE = [720, 720]

doubleres = False
tripleres = False

pygame.display.set_caption("FULL METAL LICH: No Bones About It")
screen = pygame.Surface(SIZE)

def normal():
    global screen
    screen = pygame.display.set_mode(SIZE)


def doubled():
    global screen
    global window
    global res
    global invscale
    invscale = 1/2
    res = DSIZE
    window = pygame.display.set_mode(DSIZE)

def tripled():
    global screen
    global window
    global res
    global invscale
    invscale = 1/3
    res = TSIZE
    window = pygame.display.set_mode(TSIZE)

def tripledfull():
    global screen
    global window
    global res
    global invscale
    invscale = 1/3
    res = TSIZE
    window = pygame.display.set_mode((TSIZE), pygame.FULLSCREEN)

print("\nWelcome to FULL METAL LICH (name and trademark pending)!")
print("Kill robots, clear rooms, open gates and traverse the dungeon's many floors.")
print("\nCONTROLS: ")
print("AIM - Move the mouse.")
print("SHOOT - Click left mouse.")
print("WALK - WASD or ARROW keys.")
print("PAUSE - 'P' key.")
print("MUTE MUSIC - 'M' key.")
print("QUIT - ESC key, pansy.")

print("\n1: 240 x 240")
print("2: 480 x 480")
print("3: 720 x 720")
print("4: 720 x 720 Fullscreen")
res = input("\nChoose a video mode. ")

if res == ("1"):
    normal()
elif res == ("2"):
    doubled()
    doubleres = True
elif res == ("3"):
    tripled()
    tripleres = True
elif res == ("4"):
    tripledfull()
    tripleres = True
else:
    print("\nRestart and enter a valid answer.")
    sys.exit(0)

class Walls(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.currentroom = "roomall"
        self.roomcheck = "roomall"
        self.activegates = ["top", "bottom", "left", "right"]
    def walldecide(self):
        for wall in collidelist:
                wall.kill()
        if self.currentroom == "roomall":
            topwall = WallColliders([0, 0, 0, 0])
            topleftwall = WallColliders([0, 0, 85, 22])
            toprightwall = WallColliders([155, 0, 85, 22])
            bottomwall = WallColliders([0, 0, 0, 0])
            bottomleftwall = WallColliders([0, 159, 85, 85])
            bottomrightwall = WallColliders([155, 159, 85, 85])
            leftwall = WallColliders([0, 0, 0, 0])
            rightwall = WallColliders([0, 0, 0, 0])
            self.activegates = ["top", "bottom", "left", "right"]
        if self.currentroom == "roombottomleft":
            topwall = WallColliders([0, 0, 240, 22])
            topleftwall = WallColliders([0, 0, 0, 0])
            toprightwall = WallColliders([0, 0, 0, 0])
            bottomwall = WallColliders([0, 0, 0, 0])
            bottomleftwall = WallColliders([0, 159, 85, 85])
            bottomrightwall = WallColliders([155, 159, 85, 85])
            leftwall = WallColliders([0, 0, 0, 0])
            rightwall = WallColliders([221, 0, 19, 180])
            self.activegates = ["bottom", "left"]
        if self.currentroom == "roombottomonly":
            topwall = WallColliders([0, 0, 240, 22])
            topleftwall = WallColliders([0, 0, 0, 0])
            toprightwall = WallColliders([0, 0, 0, 0])
            bottomwall = WallColliders([0, 0, 0, 0])
            bottomleftwall = WallColliders([0, 159, 85, 85])
            bottomrightwall = WallColliders([155, 159, 85, 85])
            leftwall = WallColliders([0, 0, 19, 180])
            rightwall = WallColliders([221, 0, 19, 180])
            self.activegates = ["bottom"]
        if self.currentroom == "roombottomright":
            topwall = WallColliders([0, 0, 240, 22])
            topleftwall = WallColliders([0, 0, 0, 0])
            toprightwall = WallColliders([0, 0, 0, 0])
            bottomwall = WallColliders([0, 0, 0, 0])
            bottomleftwall = WallColliders([0, 159, 85, 85])
            bottomrightwall = WallColliders([155, 159, 85, 85])
            leftwall = WallColliders([0, 0, 19, 180])
            rightwall = WallColliders([0, 0, 0, 0])
            self.activegates = ["bottom", "right"]
        if self.currentroom == "roomhorzbottom":
            topwall = WallColliders([0, 0, 240, 22])
            topleftwall = WallColliders([0, 0, 0, 0])
            toprightwall = WallColliders([0, 0, 0, 0])
            bottomwall = WallColliders([0, 0, 0, 0])
            bottomleftwall = WallColliders([0, 159, 85, 85])
            bottomrightwall = WallColliders([155, 159, 85, 85])
            leftwall = WallColliders([0, 0, 0, 0])
            rightwall = WallColliders([0, 0, 0, 0])
            self.activegates = ["bottom", "left", "right"]
        if self.currentroom == "roomhorzonly":
            topwall = WallColliders([0, 0, 240, 22])
            topleftwall = WallColliders([0, 0, 0, 0])
            toprightwall = WallColliders([0, 0, 0, 0])
            bottomwall = WallColliders([0, 159, 240, 25])
            bottomleftwall = WallColliders([0, 0, 0, 0])
            bottomrightwall = WallColliders([0, 0, 0, 0])
            leftwall = WallColliders([0, 0, 0, 0])
            rightwall = WallColliders([0, 0, 0, 0])
            self.activegates = ["left", "right"]
        if self.currentroom == "roomhorztop":
            topwall = WallColliders([0, 0, 0, 0])
            topleftwall = WallColliders([0, 0, 85, 22])
            toprightwall = WallColliders([155, 0, 85, 22])
            bottomwall = WallColliders([0, 159, 240, 25])
            bottomleftwall = WallColliders([0, 0, 0, 0])
            bottomrightwall = WallColliders([0, 0, 0, 0])
            leftwall = WallColliders([0, 0, 0, 0])
            rightwall = WallColliders([0, 0, 0, 0])
            self.activegates = ["top", "left", "right"]
        if self.currentroom == "roomleftonly":
            topwall = WallColliders([0, 0, 240, 22])
            topleftwall = WallColliders([0, 0, 0, 0])
            toprightwall = WallColliders([0, 0, 0, 0])
            bottomwall = WallColliders([0, 159, 240, 25])
            bottomleftwall = WallColliders([0, 0, 0, 0])
            bottomrightwall = WallColliders([0, 0, 0, 0])
            leftwall = WallColliders([0, 0, 0, 0])
            rightwall = WallColliders([221, 0, 19, 180])
            self.activegates = ["left"]
        if self.currentroom == "roomrightonly":
            topwall = WallColliders([0, 0, 240, 22])
            topleftwall = WallColliders([0, 0, 0, 0])
            toprightwall = WallColliders([0, 0, 0, 0])
            bottomwall = WallColliders([0, 159, 240, 25])
            bottomleftwall = WallColliders([0, 0, 0, 0])
            bottomrightwall = WallColliders([0, 0, 0, 0])
            leftwall = WallColliders([0, 0, 19, 180])
            rightwall = WallColliders([0, 0, 0, 0])
            self.activegates = ["right"]
        if self.currentroom == "roomtopleft":
            topwall = WallColliders([0, 0, 0, 0])
            topleftwall = WallColliders([0, 0, 85, 22])
            toprightwall = WallColliders([155, 0, 85, 22])
            bottomwall = WallColliders([0, 159, 240, 25])
            bottomleftwall = WallColliders([0, 0, 0, 0])
            bottomrightwall = WallColliders([0, 0, 0, 0])
            leftwall = WallColliders([0, 0, 0, 0])
            rightwall = WallColliders([221, 0, 19, 180])
            self.activegates = ["top", "left"]
        if self.currentroom == "roomtoponly":
            topwall = WallColliders([0, 0, 0, 0])
            topleftwall = WallColliders([0, 0, 85, 22])
            toprightwall = WallColliders([155, 0, 85, 22])
            bottomwall = WallColliders([0, 159, 240, 25])
            bottomleftwall = WallColliders([0, 0, 0, 0])
            bottomrightwall = WallColliders([0, 0, 0, 0])
            leftwall = WallColliders([0, 0, 19, 180])
            rightwall = WallColliders([221, 0, 19, 180])
            self.activegates = ["top"]
        if self.currentroom == "roomtopright":
            topwall = WallColliders([0, 0, 0, 0])
            topleftwall = WallColliders([0, 0, 85, 22])
            toprightwall = WallColliders([155, 0, 85, 22])
            bottomwall = WallColliders([0, 159, 240, 25])
            bottomleftwall = WallColliders([0, 0, 0, 0])
            bottomrightwall = WallColliders([0, 0, 0, 0])
            leftwall = WallColliders([0, 0, 19, 180])
            rightwall = WallColliders([0, 0, 0, 0])
            self.activegates = ["top", "right"]
        if self.currentroom == "roomvertleft":
            topwall = WallColliders([0, 0, 0, 0])
            topleftwall = WallColliders([0, 0, 85, 22])
            toprightwall = WallColliders([155, 0, 85, 22])
            bottomwall = WallColliders([0, 0, 0, 0])
            bottomleftwall = WallColliders([0, 159, 85, 85])
            bottomrightwall = WallColliders([155, 159, 85, 85])
            leftwall = WallColliders([0, 0, 0, 0])
            rightwall = WallColliders([221, 0, 19, 180])
            self.activegates = ["top", "bottom", "left"]
        if self.currentroom == "roomvertonly":
            topwall = WallColliders([0, 0, 0, 0])
            topleftwall = WallColliders([0, 0, 85, 22])
            toprightwall = WallColliders([155, 0, 85, 22])
            bottomwall = WallColliders([0, 0, 0, 0])
            bottomleftwall = WallColliders([0, 159, 85, 85])
            bottomrightwall = WallColliders([155, 159, 85, 85])
            leftwall = WallColliders([0, 0, 19, 180])
            rightwall = WallColliders([221, 0, 19, 180])
            self.activegates = ["top", "bottom"]
        if self.currentroom == "roomvertright":
            topwall = WallColliders([0, 0, 0, 0])
            topleftwall = WallColliders([0, 0, 85, 22])
            toprightwall = WallColliders([155, 0, 85, 22])
            bottomwall = WallColliders([0, 0, 0, 0])
            bottomleftwall = WallColliders([0, 159, 85, 85])
            bottomrightwall = WallColliders([155, 159, 85, 85])
            leftwall = WallColliders([0, 0, 19, 180])
            rightwall = WallColliders([0, 0, 0, 0])
            self.activegates = ["top", "bottom", "right"]
        if self.currentroom == "secret":
            topwall = WallColliders([0, 0, 240, 22])
            topleftwall = WallColliders([0, 0, 0, 0])
            toprightwall = WallColliders([0, 0, 0, 0])
            bottomwall = WallColliders([0, 159, 240, 25])
            bottomleftwall = WallColliders([0, 0, 0, 0])
            bottomrightwall = WallColliders([0, 0, 0, 0])
            leftwall = WallColliders([0, 0, 19, 180])
            rightwall = WallColliders([221, 0, 19, 180])
            self.activegates = []
    def draw(self):
        self.image = pygame.image.load("sprites/rooms/" + (str(self.currentroom)) + ".png")
        screen.blit(self.image, [0, 0])

room = Walls()
roomlist = ["roomall", "roombottomleft", "roombottomonly", "roombottomright", "roomhorzbottom", "roomhorzonly", "roomhorztop", "roomleftonly", "roomrightonly", "roomtopleft", "roomtoponly", "roomtopright", "roomvertleft", "roomvertonly", "roomvertright", "secret"]
toprooms = ["roomall", "roombottomleft", "roombottomonly", "roombottomright", "roomhorzbottom", "roomvertleft", "roomvertonly", "roomvertright"]
bottomrooms = ["roomall", "roomhorztop", "roomtopleft", "roomtoponly", "roomtopright", "roomvertleft", "roomvertonly", "roomvertright"]
leftrooms = ["roomall", "roombottomright", "roomhorzbottom", "roomhorzonly", "roomhorztop", "roomrightonly", "roomtopright", "roomvertright"]
rightrooms = ["roomall", "roombottomleft", "roomhorzbottom", "roomhorzonly", "roomhorztop", "roomleftonly", "roomtopleft", "roomvertleft"]

collidelist = pygame.sprite.Group()

class WallColliders(pygame.sprite.Sprite):
    def __init__(self, rectval):
        pygame.sprite.Sprite.__init__(self, collidelist)
        self.rect = rectval
    def gatecheck(self):
        if room.currentroom != room.roomcheck:
            for gatetype in room.activegates:
                newgate = GateColliders(gatetype)
            room.roomcheck = room.currentroom

exitlist = pygame.sprite.Group()

class ExitColliders(pygame.sprite.Sprite):
    def __init__(self, rectval, name):
        pygame.sprite.Sprite.__init__(self, exitlist)
        self.rect = pygame.Rect(rectval)
        self.name = name
    def checkcollide(self):
        if pygame.sprite.collide_rect(self, player):
            if self.name == ("top"):
                room.currentroom = random.choice(toprooms)
                player.y = 234
            if self.name == ("bottom"):
                room.currentroom = random.choice(bottomrooms)
                player.y = 5
            if self.name == ("left"):
                room.currentroom = random.choice(leftrooms)
                player.x = 234
            if self.name == ("right"):
                room.currentroom = random.choice(rightrooms)
                player.x = 5

topexit = ExitColliders([85, -15, 70, 1], "top")
bottomexit = ExitColliders([85, 254, 70, 1], "bottom")
leftexit = ExitColliders([-15, 40, 0, 120], "left")
rightexit = ExitColliders([254, 40, 1, 120], "right")

gatelist = pygame.sprite.Group()

class GateColliders(pygame.sprite.Sprite):
    def __init__(self, direction):
        pygame.sprite.Sprite.__init__(self, gatelist)
        self.direction = direction
        self.rect = pygame.Rect(0, 0, 0, 0)
        self.image = pygame.image.load("sprites/gates/" + direction + ".png").convert_alpha()
        self.playsound = True
    def activate(self):
        if player.x > 7 and player.x < 213 and player.y > 12 and player.y < 153:
            self.collide()
            screen.blit(self.image, [0, 0])
            if self.playsound:
                gateclose.play()
                self.playsound = False
    def collide(self):
        if self.direction == "top":
            self.rect = pygame.Rect(85, 0, 70, 14)
        if self.direction == "bottom":
            self.rect = pygame.Rect(85, 172, 70, 2)
        if self.direction == "left":
            self.rect = pygame.Rect(0, 0, 8, 180)
        if self.direction == "right":
            self.rect = pygame.Rect(232, 0, 8, 180)

bulletlist = pygame.sprite.Group()
bullets = []
hitlist = []

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, angle):
        pygame.sprite.Sprite.__init__(self, bulletlist)
        self.image = pygame.image.load("sprites/bullets/bullet.png").convert_alpha()
        self.speed = 3
        self.x = x
        self.y = y
        self.angle = angle
        self.x_add = 0
        self.y_add = 0
        self.rect = self.image.get_rect()
    def assign(self):
        self.x_add = (self.speed * math.cos(math.radians(self.angle)))
        self.y_add = (self.speed * math.sin(math.radians(self.angle)))
    def collide(self):
        if pygame.sprite.spritecollideany(self, collidelist) or pygame.sprite.spritecollideany(self, enemylist) or pygame.sprite.spritecollideany(self, gatelist):
            if pygame.sprite.spritecollideany(self, collidelist) or pygame.sprite.spritecollideany(self, gatelist):
                wallhit.play()
            hit = BulletHit(self.x, self.y)
            hitlist.append(hit)
            bullets.remove(self)
            self.kill()
    def update(self):
        self.x += self.x_add
        self.y -= self.y_add
        self.rect = pygame.Rect(self.x, self.y, 6, 6)
        if self.x >= 240 or self.x <= 0:
            bullets.remove(self)
            self.kill()
        if self.y >= 240 or self.y <= 0:
            bullets.remove(self)
            self.kill()
    def draw(self):
        screen.blit(self.image, (self.x, self.y))

class BulletHit(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.hitelapsed = 0
        self.image = pygame.image.load("sprites/bullets/bullethit.png").convert_alpha()
    def explode(self):
        self.hitelapsed += 1
        if self.hitelapsed >= 5:
            hitlist.remove(self)
            self.kill()
    def draw(self):
        screen.blit(self.image, (self.x, self.y))

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.charnum = 1
        self.walknum = 1
        self.moveelapsed = 0
        self.runelapsed = 0
        self.idleelapsed = 0
        self.shootelapsed = 0
        self.x = 30
        self.y = 80
        self.speed = 1
        self.angle = 0
        self.armchanger_x = 5
        self.body = pygame.image.load("sprites/player/char.png").convert_alpha()
        self.image = pygame.image.load("sprites/player/char_arm.png").convert_alpha()
        self.rect = self.body.get_rect()
        self.direction = "right"
        self.health = 5
        self.vulnerable = True
        self.vulnerablecount = 0
        self.shotsfired = 0
        self.shotshit = 0
    def idleanimation(self):
        if not any (pygame.key.get_pressed()):
            self.walknum = 1
            self.charnum += 1
            if self.charnum > 4:
                self.charnum = 1
            if self.direction == "right":
                self.body = pygame.image.load("sprites/player/char" + str(self.charnum) + ".png").convert_alpha()
                self.image = pygame.image.load("sprites/player/char_arm.png").convert_alpha()
            if self.direction == "left":
                self.body = pygame.transform.flip((pygame.image.load("sprites/player/char" + str(self.charnum) + ".png").convert_alpha()), True, False)
                self.image = pygame.transform.flip((pygame.image.load("sprites/player/char_arm.png").convert_alpha()), False, True)
    def walking(self):
        if self.direction == "right":
            if key[K_RIGHT] or key[ord("d")] or key[K_UP] or key[ord("w")] or key[K_DOWN] or key[ord("s")]:
                self.walknum += 1
                self.charnum = 1
                if self.walknum > 17:
                    self.walknum = 1
                self.body = pygame.image.load("sprites/player/char_run" + str(self.walknum) + ".png").convert_alpha()
        if self.direction == "left":
            if key[K_LEFT] or key[ord("a")] or key[K_UP] or key[ord("w")] or key[K_DOWN] or key[ord("s")]:
                self.walknum += 1
                self.charnum = 1
                if self.walknum > 17:
                    self.walknum = 1
                self.body = pygame.transform.flip(pygame.image.load("sprites/player/char_run" + str(self.walknum) + ".png").convert_alpha(), True, False)
        if self.walknum == 8 or self.walknum == 16:
            footstep.play()
    def shoot(self):
        if mouse[0] and self.shootelapsed >= 10:
            shot.play()
            new_bullet = Bullet(self.x + 4, self.y + 9, self.angle)
            bullets.append(new_bullet)
            new_bullet.assign()
            self.shootelapsed = 0
            self.shotsfired += 1
    def updater(self):
        self.moveelapsed += 1
        self.runelapsed += 1
        self.idleelapsed += 1
        self.shootelapsed += 1
        if self.moveelapsed >= 1:
            self.moveelapsed = 0
            self.moveandcollide()
        if self.runelapsed >= 3:
            self.runelapsed = 0
            self.walking()
        if self.idleelapsed >= 5:
            self.idleelapsed = 0
            self.idleanimation()
    def move(self):
        if key[K_LEFT] or key[ord("a")]:
            self.x -= self.speed
            self.direction = "left"
        if key[K_RIGHT] or key[ord("d")]:
            self.x += self.speed
            self.direction = "right"
        if key[K_UP] or key[ord("w")]:
            self.y -= self.speed
        if key[K_DOWN] or key[ord("s")]:
            self.y += self.speed
        self.updaterect()
    def moveandcollide(self):
        playerpos = self.x, self.y
        self.move()
        if pygame.sprite.spritecollideany(player, collidelist) or pygame.sprite.spritecollideany(self, gatelist):
            self.x, self.y = playerpos
            self.updaterect()
        if pygame.sprite.spritecollideany(self, enemylist) and self.vulnerable:
            playerhit.play()
            self.health -= 1
            self.vulnerable = False
        if self.vulnerable == False:
            self.vulnerablecount += 1
            if self.vulnerablecount >= 45:
                self.vulnerable = True
                self.vulnerablecount = 0
    def rotate(self):
        rel_x, rel_y = mouse_x - (self.x + 4), mouse_y - (self.y + 9)
        self.angle = (180 / math.pi) * -math.atan2(rel_y, rel_x)
        self.rotimage = pygame.transform.rotate(self.image, self.angle)
        self.armpos = self.rotimage.get_rect(center = (self.rect.center))
    def updaterect(self):
        self.rect = pygame.Rect(self.x, self.y, 20, 20)
    def draw(self):
        screen.blit(self.body, (self.x, self.y))
        if self.direction == "right":
            self.armchanger_x = 5
        if self.direction == "left":
            self.armchanger_x = -5
        screen.blit(self.rotimage, (self.armpos[0] - self.armchanger_x, self.armpos[1] - 1))

player = Player()

class Cursor(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("sprites/menuelements/crosshair.png").convert_alpha()
    def crosshair(self):
        cursorpos = ((mousepos[0] - 7), (mousepos[1] - 7))
        screen.blit(self.image, cursorpos)

cursor = Cursor()

enemylist = pygame.sprite.Group()

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self, enemylist)
        self.x = x
        self.y = y
        self.speed = random.randint(2, 4) / 10
        self.health = 5
        self.image = pygame.image.load("sprites/enemies/enemy_walk1.png").convert_alpha()
        self.rect = pygame.Rect(self.x, self.y, 13, 18)
        self.hitenemy = False
        self.hitelapsed = 0
        self.deathelapsed = 0
        self.deathnum = 1
        self.addkill = True
        self.walkelapsed = 0
        self.walkframe = 1
        self.pause = False
        self.pauseelapsed = 0
        self.pauseframe = random.randint(130, 310)
        self.pauselength = random.randint(25, 50)
    def collide(self):
        if self.health <= 0:
            self.pause = True
            self.rect = pygame.Rect(0, 0, 0, 0)
            if self.hitenemy == True:
                counter.killcount += 1
                enemydeath.play()
            self.hitenemy = False
            self.deather()
            return
        if pygame.sprite.spritecollideany(self, bulletlist):
            self.pause = True
            enemyhit.play()
            self.health -= 1
            self.image = pygame.image.load("sprites/enemies/enemy_hit.png").convert_alpha()
            self.hitenemy = True
            player.shotshit += 1
        if self.hitenemy == True:
            self.hitelapsed += 1
            if self.hitelapsed >= 5:
                self.image = pygame.image.load("sprites/enemies/enemy_walk1.png").convert_alpha()
                self.hitenemy = False
                self.hitelapsed = 0
                self.pause = False
        self.rect = pygame.Rect(self.x, self.y, 13, 18)
    def walk(self):
        if self.pause == True:
            return
        if player.x > self.x:
            self.x += self.speed
        if player.x < self.x:
            self.x -= self.speed
        if player.y > self.y:
            self.y += self.speed
        if player.y < self.y:
            self.y -= self.speed
    def animation(self):
        self.pauseelapsed += 1
        if self.pauseelapsed >= self.pauseframe:
            self.pause = True
            self.image = pygame.image.load("sprites/enemies/enemy_walk1.png").convert_alpha()
            if self.pauseelapsed >= (self.pauseframe + self.pauselength):
                self.pause = False
                self.pauseelapsed = 0
                self.walkframe = 1
                self.walkelapsed = 0
        if self.pause == True:
            return
        self.walkelapsed += 1
        if self.walkelapsed >= 4:
            self.walkframe += 1
        if self.walkframe == 13:
            self.walkframe = 1
        self.image = pygame.image.load("sprites/enemies/enemy_walk" + str(self.walkframe) + ".png").convert_alpha()
    def deather(self):
        self.image = pygame.image.load("sprites/enemies/enemy_death" + str(self.deathnum) + ".png").convert_alpha()
        self.deathelapsed += 1
        if self.deathelapsed >= 10:
            self.deathnum += 1
            self.deathelapsed = 0
            if self.deathnum == 6:
                self.kill()
    def draw(self):
        screen.blit(self.image, (self.x, self.y)) 

class ProgressCheck(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.killcount = 0
        self.enemyimage = pygame.image.load("sprites/hudelements/headcount.png").convert_alpha()
        self.clearimage = pygame.image.load("sprites/hudelements/roomclear/roomclear1.png").convert_alpha()
        self.livesimage = pygame.image.load("sprites/hudelements/lives/lives5.png").convert_alpha()
        self.roomsentered = 0
        self.roomselapsed = 0
        self.clearplay = True
        self.clearelapsed = 0
        self.clearframe = 0
        self.clearanim = False
        self.rangebottom = 2
        self.rangetop = 4
    def roomcheck(self):
        if len(enemylist) == 0:
            for gate in gatelist:
                gate.kill()
            if self.roomsentered >= 1:
                if self.clearplay:
                    self.clearanim = True
                    gateopen.play()
                    if self.roomselapsed == 4:
                        self.rangebottom += 1
                        self.rangetop += 1
                        self.roomselapsed = 0
                    self.clearplay = False
        if room.currentroom != room.roomcheck:
            self.roomsentered += 1
            self.roomselapsed += 1
            self.clearplay = True
    def animateclear(self):
        if self.clearframe == 20:
            self.clearanim = False
            self.clearframe = 0
        if self.clearanim == True:
            self.clearelapsed += 1
            if self.clearelapsed == 2:
                self.clearelapsed = 0
                self.clearframe += 1
                self.clearimage = pygame.image.load("sprites/hudelements/roomclear/roomclear" + str(self.clearframe) + ".png").convert_alpha()
    def playerlives(self):
        if player.health <= 0:
            print("\nYou have perished.")
            global done
            done = True
        self.livesimage = pygame.image.load("sprites/hudelements/lives/lives" + str(player.health) + ".png").convert_alpha()
    def display(self):
        screen.blit(self.livesimage, (0, 0))
        screen.blit(self.enemyimage, (5, 200))
        killsdisplay = font.render(str(self.killcount), False, (255,255,255))
        screen.blit(killsdisplay, (51, 199))
        if self.clearanim == True:
            screen.blit(self.clearimage, (0, 0))

counter = ProgressCheck()

class MuteMusic(object):
    def __init__(self):
        self.playing = True
    def toggle(self):
        if self.playing:
            pygame.mixer.music.pause()
        if not self.playing:
            pygame.mixer.music.unpause()
        self.playing = not self.playing

mute = MuteMusic()

def enemyspawn():
    if room.currentroom != room.roomcheck:
        for enemy in enemylist:
            enemy.kill()
        for bullet in bulletlist:
            bullets.remove(bullet)
            bullet.kill()
        for x in range(random.randint(counter.rangebottom, counter.rangetop)):
            enemy = Enemy((random.randint(30, 200)), (random.randint(40, 130))) 

def musictoggle():
    if key[ord("p")]:
        if paused:
            pygame.mixer.music.load("music/pausemusic.mp3")
        if not paused:
            pygame.mixer.music.load("music/gameplaymusic.mp3")
        pygame.mixer.music.play(-1)

intro = True

while intro:
    screen.blit((pygame.image.load("sprites/menuelements/title.png")), [0, 0])
    if doubleres or tripleres:
        pygame.transform.scale(screen, res, window)
    pygame.display.update()
    clock.tick()
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            intro = False
            pygame.mouse.set_visible(False)
            pygame.mixer.music.load("music/gameplaymusic.mp3")
            pygame.mixer.music.play(-1)

paused = False
done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                print("\nQuitting so soon?")
                done = True
                pygame.quit()
                sys.exit(0)
            if event.key == pygame.K_p:
                pause.play()
                paused = not paused
                mute.playing = True
            if event.key == pygame.K_m:
                pause.play()
                mute.toggle()

    key = pygame.key.get_pressed()
    mouse = pygame.mouse.get_pressed()

    mousepos = pygame.mouse.get_pos()
    if doubleres or tripleres:
        mousepos = mousepos[0] * invscale, mousepos[1] * invscale
    mouse_x, mouse_y = mousepos

    room.walldecide()
    room.draw()

    enemyspawn()
    counter.roomcheck()

    for item in collidelist:
        item.gatecheck()

    for gate in gatelist:
        gate.activate()

    for leave in exitlist:
        leave.checkcollide()

    if not paused:
        player.shoot()
        player.updater()
        player.rotate()
    player.draw()

    for bullet in bullets:
        if not paused:
            bullet.update()
        bullet.draw()

    for enemy in enemylist:
        if not paused:
            enemy.collide()
            enemy.walk()
            enemy.animation()
        enemy.draw()

    for bullet in bullets:
        if not paused:
            bullet.collide()

    for hit in hitlist:
        if not paused:
            hit.explode()
        hit.draw()

    counter.playerlives()
    counter.animateclear()
    counter.display()

    musictoggle()

    if paused:
        screen.blit((pygame.image.load("sprites/menuelements/pausescreen.png")), [0, 0])

    cursor.crosshair()

    if doubleres or tripleres:
        pygame.transform.scale(screen, res, window)
    clock.tick(60)
    pygame.display.update()

pygame.quit()

print("\nSTATS:")
print("KILLS - " + str(counter.killcount))
print("SHOTS FIRED - " + str(player.shotsfired))
if player.shotsfired > 0:
    print("ACCURACY - " + str(int((player.shotshit / player.shotsfired) * 100)) + "%")
print("ROOMS ENTERED - " + str(counter.roomsentered))

savestats = input("\nPress ENTER if you would like to save these stats. ")

if savestats == (""):
    name = input("Enter your name (entering a saved name will overwrite previous stats): ")
    savefile = open("stats/" + str(name) + "'s_stats.txt", "w+")
    savefile.write("KILLS - " + str(counter.killcount) + "\n")
    savefile.write("SHOTS FIRED - " + str(player.shotsfired) + "\n")
    if player.shotsfired > 0:
        savefile.write("ACCURACY - " + str(int((player.shotshit / player.shotsfired) * 100)) + "%\n")
    savefile.write("ROOMS ENTERED - " + str(counter.roomsentered))
    savefile.close()

print("\nTry again next time!")

sys.exit(0)
