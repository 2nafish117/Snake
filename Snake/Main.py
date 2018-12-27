import pygame as pg
import random
import time

from Snake import Snake
from Fruit import Fruit

def gameInput(key):
    if key == pg.K_UP and snake.direction != 'DOWN':
        print('UP')
        snake.direction = 'UP'
        snake.dx = 0
        snake.dy = -1
    elif key == pg.K_RIGHT and snake.direction != 'LEFT':
        print('RIGHT')
        snake.direction = 'RIGHT'
        snake.dx = 1
        snake.dy = 0
    elif key == pg.K_LEFT and snake.direction != 'RIGHT':
        print('LEFT')
        snake.direction = 'LEFT'
        snake.dx = -1
        snake.dy = 0
    elif key == pg.K_DOWN and snake.direction != 'UP':
        print('DOWN')
        snake.direction = 'DOWN'
        snake.dx = 0
        snake.dy = 1
    return

def gameUpdate():
    #update snake's body
    i = len(snake.body) - 1
    while i >= 1:
        snake.body[i][0] = snake.body[i - 1][0]
        snake.body[i][1] = snake.body[i - 1][1]
        i -= 1
    snake.position[0] += snake.dx
    snake.position[1] += snake.dy
    snake.position[0] = snake.position[0] % width
    snake.position[1] = snake.position[1] % height
    snake.body[0][0] = snake.position[0]
    snake.body[0][1] = snake.position[1]

    #check collision with self
    for part in snake.body[1:]:
        if snake.position[0] == part[0] and snake.position[1] == part[1]:
            print('collision at ' + str(part))
            gameOver()

    #check colision with fruit
    if(snake.position == fruit.position):
        fruit.position = [random.randint(0, width - 1), random.randint(0, height - 1)]
        global score
        score += 1
        eaten = snake.body[len(snake.body) - 1].copy()
        snake.body.append(eaten)
        #eatSound.play()
    return

def gameRender():
    #render ground
    for y in range(0, height):
        for x in range(0, width):
            gameDisplay.blit(grassTex, (scale * x, scale * y))

    #render fruit
    gameDisplay.blit(fruit.fruitTex, (scale * fruit.position[0], scale * fruit.position[1]))
    #render snake
    gameDisplay.blit(snake.headTex, (scale * snake.position[0], scale * snake.position[1]))
    for i in range(1, len(snake.body)):
        gameDisplay.blit(snake.bodyTex, (scale * snake.body[i][0], scale * snake.body[i][1]))
    #display score
    renderText('score:' + str(score), 2, 1)
    return

def renderText(text, x:int, y:int):
    gameText = TextFont.render(str(text), True, (255, 255, 255))
    gameRect = gameText.get_rect()
    gameRect.centerx = x * scale
    gameRect.centery = y * scale
    gameDisplay.blit(gameText, gameRect)

def gameOver():
    snake.dx = 0
    snake.dy = 0
    renderText('Game Over', width / 2, height / 2)
    pg.mixer.music.load('sounds/what happened.mp3')
    pg.mixer.music.set_volume(0.3)
    pg.mixer.music.play(0)

    pg.display.update()
    done = False
    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                global gameIsRunning
                gameIsRunning = False
                done = True
        clock.tick(FPS)

if __name__ == '__main__':
    pg.init()
    scale = 16
    height = 15
    width = 20
    displayHeight = scale * height
    displayWidth = scale * width
    FPS = 7
    score = 0

    gameDisplay = pg.display.set_mode((displayWidth, displayHeight))
    pg.display.set_caption('First Gameu!')
    clock = pg.time.Clock()

    grassTex = pg.image.load('textures/grassTex.png').convert()
    headTex = pg.image.load('textures/headTex.png').convert()
    bodyTex = pg.image.load('textures/bodyTex.png').convert()
    fruitTex = pg.image.load('textures/fruitTex.png').convert()
    TextFont = pg.font.Font('fonts/Digital_tech.otf', scale)
    pg.mixer.music.load('sounds/POL-miracle-park-short.wav')
    #eatSound = pg.mixer.Sound('sounds/what happened.mp3')
    
    pg.mixer.music.set_volume(0.1)
    pg.mixer.music.play(-1)
    #pg.mixer.music.set_volume(0.1)

    snake = Snake(20, 15, headTex, bodyTex)
    fruit = Fruit(10, 10, fruitTex)
    gameIsRunning = True

    while gameIsRunning:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                gameIsRunning = False
            if event.type == pg.KEYDOWN:
                gameInput(event.key)
            
        gameUpdate()
        gameRender()
        
        pg.display.update()
        clock.tick(FPS)

    pg.quit()
    quit()
