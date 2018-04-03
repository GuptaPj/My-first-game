import pygame
import time
import random

pygame.init()

window_width = 800
window_height = 600

tron_flour = (0, 255, 216)
black = (0,0,0)
white = (255,255,255)

gameDisplay = pygame.display.set_mode((window_width,window_height))
pygame.display.set_caption('Race Now')

tronImg = pygame.image.load('tron_trans.png')
tron_width = tronImg.get_width()
clock = pygame.time.Clock()

def crash():
    message_display('You Crashed')

def message_display(msg):
    msgFont = pygame.font.Font('ariblk.ttf',30)
    txtSurf , txtRect = text_objects(msgFont,msg)
    txtRect.center = (window_width/2,window_height/2)
    gameDisplay.blit(txtSurf,txtRect)
    pygame.display.update()
    time.sleep(2)
    game_play()

def somedisplay(dispx,dispy,dispw,disph,msg,color):
    msgFont = pygame.font.Font('ariblk.ttf',20)
    txtSurf , txtRect = text_objects(msgFont,msg)
    txtRect.x = dispx
    txtRect.y = dispy
    txtRect.width = dispw
    txtRect.height = disph
    gameDisplay.blit(txtSurf,txtRect)
    pygame.display.update()

def  text_objects(font,txt):
    txtSurface = font.render(txt,True,black)
    return txtSurface, txtSurface.get_rect()

def block(blockx,blocky,blockw,blockh,color):
    pygame.draw.rect(gameDisplay,color,(blockx,blocky,blockw,blockh))

def game_play():
    gameExit = False

    prevScore = 0
    score = 0
    

    def tron(x,y):
        gameDisplay.blit(tronImg,(x,y))

    x = (window_width * 0.45)
    y = (window_height * 0.9)
    x_change = 0

    block_startx = random.randrange(0,window_width)
    block_starty = -600
    blockw = 100
    blockh = 100
    block_speed = 7

    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                elif event.key == pygame.K_RIGHT:
                    x_change = 5
            if event.type == pygame.KEYUP:
                x_change = 0

            print(event)
        x += x_change
        if x < 0 or x > window_width-tron_width:
            crash()
        
        gameDisplay.fill(tron_flour)
        tron(x,y)
        block(block_startx,block_starty,blockw,blockh,black)
        block_starty += block_speed

        if block_starty > window_height:
            block_startx = random.randrange(0,window_width)
            block_starty = 0
            score += 1

        if score > prevScore:
            if score%10 == 0:
                block_speed += 1
                prevScore = score
            msg = "score : "+str(score)+" level : "+str(block_speed)
            print(msg)
            somedisplay(0,0,20,10,msg,white)

        if y <= block_starty+blockh:
            if block_startx <= x <= block_startx+blockw or block_startx <= x+tron_width <= block_startx+blockw:
                crash()

        pygame.display.update()
        clock.tick(60)

game_play()
pygame.quit()
quit()
