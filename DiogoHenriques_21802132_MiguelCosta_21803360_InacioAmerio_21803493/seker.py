import pygame
import time

pygame.init()

#colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green =  (0, 255, 9)
blue = (0, 0, 255)

#sounds/music
keySound = pygame.mixer.Sound('keysound.wav')
winSound = pygame.mixer.Sound('winSound.wav')
pygame.mixer.music.load('song.mp3')
pygame.mixer.music.set_volume(1)

#imageLoad
walkDown = [pygame.image.load('D1.png'), pygame.image.load('D2.png'), pygame.image.load('D3.png'), pygame.image.load('D4.png'), pygame.image.load('D5.png'), pygame.image.load('D6.png')]
walkUp = [pygame.image.load('U1.png'), pygame.image.load('U2.png'), pygame.image.load('U3.png'), pygame.image.load('U4.png'), pygame.image.load('U5.png'), pygame.image.load('U6.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png')]
walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png')]

standingFront = pygame.image.load('S.png')
standingBack = pygame.image.load('B.png')

keyImg = pygame.image.load('key.png')
emptyImg = pygame.image.load('empty.png')

menuBg = pygame.image.load('bgseker.png')
gameBg = pygame.image.load('lab.jpg')
gameDarkness = pygame.image.load('darkness.png')

gameDarknessFilter = gameDarkness.copy()
alpha = 128
gameDarknessFilter.fill((255, 255, 255, alpha), None, pygame.BLEND_RGBA_MULT)

#Window properties
screenSize = [800,800]
screenWidth = screenSize[0]
screenHeight = screenSize[1]
screen = pygame.display.set_mode((screenWidth, screenHeight))

#name of the program
pygame.display.set_caption("SEKER")

#hide mouse
pygame.mouse.set_visible(False)

score = 0

#class with player properties
class character(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 2

        self.left = False
        self.right = False
        self.up = False
        self.down = False
        self.stepCounter = 0

    def draw(self, screen):
        if self.stepCounter + 1 >= 18:
            self.stepCounter = 0

        if self.left:
            screen.blit(walkLeft[self.stepCounter//3], (self.x, self.y))
            self.stepCounter += 1
        elif self.right:
            screen.blit(walkRight[self.stepCounter//3], (self.x, self.y))
            self.stepCounter += 1
        elif self.up:
            screen.blit(walkUp[self.stepCounter//3], (self.x, self.y))
            self.stepCounter += 1
        elif self.down:
            screen.blit(walkDown[self.stepCounter//3], (self.x, self.y))
            self.stepCounter += 1
        else:
            screen.blit(standingFront, (self.x, self.y))

#class with maze properties
class mazeWall(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw(self, screen):
        pygame.draw.rect(screen, blue, (self.x, self.y, self.width, self.height))

#class with key properties
class key(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    
    def draw(self, screen):
        screen.blit(keyImg, (self.x, self.y, self.width, self.height))

#function for the main menu/titlescreen
def titleScreen():
    menu = True
    controls = font.render('Controls ', 1, white)
    move = font.render('Movement: w, a, s, d ', 1, white)
    startControl = font.render('Start = Enter ', 1, white)
    titleImage = 1
    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                mainLoop()
                
        start = pygame.key.get_pressed()
        screen.blit(menuBg, (0, 0))
        screen.blit(controls, (10, 10))
        screen.blit(move, (10, 40))
        screen.blit(startControl, (10, 70))
        pygame.display.update()
        
#draw mazeWalls     
def wallBuild():
    # 1st wall border
    wallv1b1.draw(screen)
    wallv2b1.draw(screen)
    wallh1b1.draw(screen)
    wallh2b1.draw(screen)
    wallh3b1.draw(screen)

    # 2nd wall border
    wallv1b2.draw(screen)
    wallv2b2.draw(screen)
    wallv3b2.draw(screen)
    wallh1b2.draw(screen)
    wallh2b2.draw(screen)
    wallh3b2.draw(screen)
    wallh4b2.draw(screen)
    wallh5b2.draw(screen)

    # 3rd wall border
    wallv1b3.draw(screen)
    wallv2b3.draw(screen)
    wallv3b3.draw(screen)
    wallh1b3.draw(screen)
    wallh2b3.draw(screen)
    wallh3b3.draw(screen)

    # 4th wall border
    wallv1b4.draw(screen)
    wallv2b4.draw(screen)
    wallh1b4.draw(screen)
    wallh2b4.draw(screen)
    wallh3b4.draw(screen)
    wallh4b4.draw(screen)

    # 5th wall border
    wallv1b5.draw(screen)
    wallv2b5.draw(screen)
    wallh1b5.draw(screen)
    wallh2b5.draw(screen)
    wallh3b5.draw(screen)

    # 6th wall border
    wallv1b6.draw(screen)
    wallv2b6.draw(screen)
    wallh1b6.draw(screen)
    wallh2b6.draw(screen)
    wallh3b6.draw(screen)


    # obstacles
    obsv1.draw(screen)
    obsv2.draw(screen)
    obsv3.draw(screen)
    obsv4.draw(screen)
    obsv5.draw(screen)
    obsv6.draw(screen)
    obsv7.draw(screen)
    obsh1.draw(screen)
    obsh2.draw(screen)
    obsh3.draw(screen)
    obsh4.draw(screen)


#---------------------------------------
#1st wall border
#---------------------------------------
#vertical
wallv1b1 = mazeWall(775, 0,25, 800)
wallv2b1 = mazeWall(0, 0, 25, 800)

#---------------------------------------
#horizontal
wallh1b1 = mazeWall(0, 0, 400,25 )
wallh2b1 = mazeWall(450,0,350,25)
wallh3b1 = mazeWall(0,775,800,25)

#---------------------------------------
#2nd wall border
#---------------------------------------
#vertical
wallv1b2 = mazeWall(50,50,25,700)
wallv2b2 = mazeWall(725,50,25,450)
wallv3b2 = mazeWall(725,550,25,200)

#---------------------------------------
#horizontal
wallh1b2 = mazeWall(50,50,100,25)
wallh2b2 = mazeWall(200,50,400,25)
wallh3b2 = mazeWall(650,50,100,25)
wallh4b2 = mazeWall(50,725,250,25)
wallh5b2 = mazeWall(350,725,400,25)


#---------------------------------------
#3rd wall border
#---------------------------------------
#vertical
wallv1b3 = mazeWall(100,100,25,600)
wallv2b3 = mazeWall(675,100,25,250)
wallv3b3 = mazeWall(675,400,25,300)

#---------------------------------------
#horizontal
wallh1b3 = mazeWall(100,100,325,25)
wallh2b3 = mazeWall(475,100,225,25)
wallh3b3 = mazeWall(100,675,600,25)

#---------------------------------------
#4th wall border
#---------------------------------------
#vertical
wallv1b4 = mazeWall(150,150,25,500)
wallv2b4 = mazeWall(625,150,25,500)

#---------------------------------------
#horizontal
wallh1b4 = mazeWall(150,150,500,25)
wallh2b4 = mazeWall(150,625,50,25)
wallh3b4 = mazeWall(250,625,300,25)
wallh4b4 = mazeWall(600,625,50,25)

#--------------------------------------
#5th wall border
#--------------------------------------
#vertical
wallv1b5 = mazeWall(200,200,25,400)
wallv2b5 = mazeWall(575,200,25,400)

#--------------------------------------
#horizontal
wallh1b5 = mazeWall(200,200,125,25)
wallh2b5 = mazeWall(375,200,225,25)
wallh3b5 = mazeWall(200,575,400,25)

#-------------------------------------
#6th wall border
#--------------------------------------
#verical
wallv1b6 = mazeWall(250,250,25,300)
wallv2b6 = mazeWall(525,250,25,300)
#--------------------------------------
#horizontal
wallh1b6 = mazeWall(250,250,300,25)
wallh2b6 = mazeWall(250,525,200,25)
wallh3b6 = mazeWall(500,525,50,25)


#-------------------------------------
#Obstacules
#-------------------------------------
#vertical
obsv1 = mazeWall(225,25,25,25)
obsv2 = mazeWall(550,75,25,25)
obsv3 = mazeWall(175,125,25,25)
obsv4 = mazeWall(500,175,25,25)
obsv5 = mazeWall(300,225,25,25)
obsv6 = mazeWall(375,600,25,25)
obsv7 = mazeWall(125,750,25,25)
#------------------------------------
#horizontal
obsh1 = mazeWall(75,275,25,25)
obsh2 = mazeWall(225,350,25,25)
obsh3 = mazeWall(700,625,25,25)
obsh4 = mazeWall(750,175,25,25)

#collisions
hasKey1 = False
hasKey2 = False
hasKey3 = False
hasKey4 = False
hasKey5 = False
def playerCollision():
    global hasKey1
    global hasKey2
    global hasKey3
    global hasKey4
    global hasKey5
    global score

    mov = pygame.key.get_pressed()

    def wallCollision(wall):
        
        if (player.x < wall.x + wall.width and
            player.x + player.width > wall.x and
            player.y < wall.y + wall.height and
            player.y + player.height > wall.y):
            if mov[pygame.K_a]:
                player.x += wall.width - (player.x - wall.x)
            elif mov[pygame.K_d]:
                player.x -= player.width - (wall.x - player.x)
            elif mov[pygame.K_w]:
                player.y += wall.height - (player.y - wall.y)
            elif mov[pygame.K_s]:
                player.y -= player.height - (wall.y - player.y)

    # 1st wall border
    wallCollision(wallv1b1)
    wallCollision(wallv2b1)
    wallCollision(wallh1b1)
    wallCollision(wallh2b1)
    wallCollision(wallh3b1)

    # 2nd wall border
    wallCollision(wallv1b2)
    wallCollision(wallv2b2)
    wallCollision(wallv3b2)
    wallCollision(wallh1b2)
    wallCollision(wallh2b2)
    wallCollision(wallh3b2)
    wallCollision(wallh4b2)
    wallCollision(wallh5b2)

    # 3rd wall border
    wallCollision(wallv1b3)
    wallCollision(wallv2b3)
    wallCollision(wallv3b3)
    wallCollision(wallh1b3)
    wallCollision(wallh2b3)
    wallCollision(wallh3b3)

    # 4th wall border
    wallCollision(wallv1b4)
    wallCollision(wallv2b4)
    wallCollision(wallh1b4)
    wallCollision(wallh2b4)
    wallCollision(wallh3b4)
    wallCollision(wallh4b4)

    # 5th wall border
    wallCollision(wallv1b5)
    wallCollision(wallv2b5)
    wallCollision(wallh1b5)
    wallCollision(wallh2b5)
    wallCollision(wallh3b5)

    # 6th wall border
    wallCollision(wallv1b6)
    wallCollision(wallv2b6)
    wallCollision(wallh1b6)
    wallCollision(wallh2b6)
    wallCollision(wallh3b6)

    # obstacles
    wallCollision(obsv1)
    wallCollision(obsv2)
    wallCollision(obsv3)
    wallCollision(obsv4)
    wallCollision(obsv5)
    wallCollision(obsv6)
    wallCollision(obsv7)
    wallCollision(obsh1)
    wallCollision(obsh2)
    wallCollision(obsh3)
    wallCollision(obsh4)
    
    
    #------------------------------------------------------------------------------------------------------------------------------------------------------
    #key1
    #------------------------------------------------------------------------------------------------------------------------------------------------------
    if hasKey1 == False and (key1.x + key1.width >= player.x >= key1.x and key1.y + key1.height >= player.y >= key1.y):
        hasKey1 = True
        score += 1
        pygame.mixer.Sound.play(keySound)

    if hasKey1 == False and (key1.x + key1.width >= player.x + player.width >= key1.x and key1.y + key1.height >= player.y >= key1.y):
        hasKey1 = True
        score += 1
        pygame.mixer.Sound.play(keySound)
        
    if hasKey1 == False and (key1.x + key1.width >= player.x >= key1.x and key1.y + key1.height >= player.y + player.height >= key1.y):
        hasKey1 = True
        score += 1
        pygame.mixer.Sound.play(keySound)
        
    if hasKey1 == False and (key1.x + key1.width >= player.x + player.width >= key1.x and key1.y + key1.height >= player.y + player.height >= key1.y):
        hasKey1 = True
        score += 1
        pygame.mixer.Sound.play(keySound)

    #------------------------------------------------------------------------------------------------------------------------------------------------------
    #key2
    #------------------------------------------------------------------------------------------------------------------------------------------------------

    if hasKey2 == False and (key2.x + key2.width >= player.x >= key2.x and key2.y + key2.height >= player.y >= key2.y):
        hasKey2 = True
        score += 1
        pygame.mixer.Sound.play(keySound)

    if hasKey2 == False and (key2.x + key2.width >= player.x + player.width >= key2.x and key2.y + key2.height >= player.y >= key2.y):
        hasKey2 = True
        score += 1
        pygame.mixer.Sound.play(keySound)
        
    if hasKey2 == False and (key2.x + key2.width >= player.x >= key2.x and key2.y + key2.height >= player.y + player.height >= key2.y):
        hasKey2 = True
        score += 1
        pygame.mixer.Sound.play(keySound)
        
    if hasKey2 == False and (key2.x + key2.width >= player.x + player.width >= key2.x and key2.y + key2.height >= player.y + player.height >= key2.y):
        hasKey2 = True
        score += 1
        pygame.mixer.Sound.play(keySound)

    #------------------------------------------------------------------------------------------------------------------------------------------------------
    #key3
    #------------------------------------------------------------------------------------------------------------------------------------------------------

    if hasKey3 == False and (key3.x + key3.width >= player.x >= key3.x and key3.y + key3.height >= player.y >= key3.y):
        hasKey3 = True
        score += 1
        pygame.mixer.Sound.play(keySound)

    if hasKey3 == False and (key3.x + key3.width >= player.x + player.width >= key3.x and key3.y + key3.height >= player.y >= key3.y):
        hasKey3 = True
        score += 1
        pygame.mixer.Sound.play(keySound)
        
    if hasKey3 == False and (key3.x + key3.width >= player.x >= key3.x and key3.y + key3.height >= player.y + player.height >= key3.y):
        hasKey3 = True
        score += 1
        pygame.mixer.Sound.play(keySound)
            
    if hasKey3 == False and (key3.x + key3.width >= player.x + player.width >= key3.x and key3.y + key3.height >= player.y + player.height >= key3.y):
        hasKey3 = True
        score += 1
        pygame.mixer.Sound.play(keySound)

    #------------------------------------------------------------------------------------------------------------------------------------------------------
    #key4
    #------------------------------------------------------------------------------------------------------------------------------------------------------
        
    if hasKey4 == False and (key4.x + key4.width >= player.x >= key4.x and key4.y + key4.height >= player.y >= key4.y):
        hasKey4 = True
        score += 1
        pygame.mixer.Sound.play(keySound)
            
    if hasKey4 == False and (key4.x + key4.width >= player.x + player.width >= key4.x and key4.y + key4.height >= player.y >= key4.y):
        hasKey4 = True
        score += 1
        pygame.mixer.Sound.play(keySound)
        
    if hasKey4 == False and (key4.x + key4.width >= player.x >= key4.x and key4.y + key4.height >= player.y + player.height >= key4.y):
        hasKey4 = True
        score += 1
        pygame.mixer.Sound.play(keySound)
            
    if hasKey4 == False and (key4.x + key4.width >= player.x + player.width >= key4.x and key4.y + key4.height >= player.y + player.height >= key4.y):
        hasKey4 = True
        score += 1
        pygame.mixer.Sound.play(keySound)

    #------------------------------------------------------------------------------------------------------------------------------------------------------
    #key5
    #------------------------------------------------------------------------------------------------------------------------------------------------------
    
    if hasKey5 == False and (key5.x + key5.width >= player.x >= key5.x and key5.y + key5.height >= player.y >= key5.y):
        if score == 4:
            hasKey5 = True
            pygame.mixer.music.stop()
            pygame.mixer.Sound.play(winSound)
            time.sleep(8)
            pygame.quit()
        

    if hasKey5 == False and (key5.x + key5.width >= player.x + player.width >= key5.x and key5.y + key5.height >= player.y >= key5.y):
        if score == 4:
            hasKey5 = True
            pygame.mixer.music.stop()
            pygame.mixer.Sound.play(winSound)
            time.sleep(8)
            pygame.quit()
    if hasKey5 == False and (key5.x + key5.width >= player.x >= key5.x and key5.y + key5.height >= player.y + player.height >= key5.y):
        if score == 4:
            hasKey5 = True
            pygame.mixer.music.stop()
            pygame.mixer.Sound.play(winSound)
            time.sleep(8)
            pygame.quit()
            
    if hasKey5 == False and (key5.x + key5.width >= player.x + player.width >= key5.x and key5.y + key5.height >= player.y + player.height >= key5.y):
        if score == 4:
            hasKey5 = True
            pygame.mixer.music.stop()
            pygame.mixer.Sound.play(winSound)
            time.sleep(8)
            pygame.quit()
        
#draw
def gameWindow():
    global walkCount
    
    wallBuild()
    screen.blit(gameBg, (0, 0))
    player.draw(screen)
    text = font.render('Keys: ' + str(score), 1, white)
    text2 = font.render('/ 4 ', 1, white)
    text3 = font.render('Well done! The last key has now appeared somewhere on the map, hurry and get it!', 1, white)

    if hasKey1 == False:
        key1.draw(screen)
    else:
        screen.blit(emptyImg, (0,0))

    if hasKey2 == False:
        key2.draw(screen)
    else:
        screen.blit(emptyImg, (0,0))

    if hasKey3 == False:
        key3.draw(screen)
    else:
        screen.blit(emptyImg, (0,0))

    if hasKey4 == False:
        key4.draw(screen)
    else:
        screen.blit(emptyImg, (0,0))

    if hasKey1 == True and hasKey2 == True and hasKey3 == True and hasKey4 == True:
        if hasKey5 == False:
            key5.draw(screen)
        else:
            screen.blit(emptyImg, (0,0))

    screen.blit(gameDarkness, (player.x-992, player.y-992))
    if score == 4:
        screen.blit(text3, (80, 750))
    screen.blit(text, (5, 0))
    screen.blit(text2, (65,0))
            
    pygame.display.update()
    
#main Loop
font = pygame.font.SysFont('arial', 20, True)
player = character(425, 20, 14, 18)
key1 = key(80,310,14,14)
key2 = key(210,30,14,14)
key3 = key(110,760,14,14)
key4 = key(760,160,14,14)
key5 = key(400, 400, 14, 14)
pygame.mixer.music.play(loops=-1)

def mainLoop():
    global run
    run = True
    
    while run:
        pygame.time.delay(10)
        gameWindow()
        playerCollision()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                quit()

        mov = pygame.key.get_pressed()
        
        #player movement
        if mov[pygame.K_a]:
            player.x -= player.vel
            player.left = True
            player.right = False
            player.up = False
            player.down = False
            
        elif mov[pygame.K_d]: 
            player.x += player.vel
            player.left = False
            player.right = True
            player.up = False
            player.down = False
            
        elif mov[pygame.K_w]:
            player.y -= player.vel
            player.left = False
            player.right = False
            player.up = True
            player.down = False
            
        elif mov[pygame.K_s]:
            player.y += player.vel
            player.left = False
            player.right = False
            player.up = False
            player.down = True

        else:
            player.left = False
            player.right = False
            player.up = False
            player.down = False
            player.stepCounter = 0
            
        
titleScreen()
gameWindow()
        
pygame.quit()



        
    
