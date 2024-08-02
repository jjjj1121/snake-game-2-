import pygame
import time
import random
pygame.init()

screen_height=500
screen_width=500

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("jjjj's fisrt game")
clock = pygame.time.Clock()
game_over = False

x=200
y=200
snake_speed=10
x_change=0
y_change=0

font_style = pygame.font.SysFont(None, 50)

snake_list =[]
length_of_snake = 1

def draw_snake(snake_list):
    for xx in snake_list:
        pygame.draw.rect(screen, (255,255,255), (xx[0], xx[1],20,20))

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [screen_width/2-50, screen_height/2])

foodx = round(random.randrange(0,screen_width)/20.0)*20
foody = round(random.randrange(0,screen_height)/20.0)*20

while not game_over :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over =True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change=-20
                y_change=0
            elif event.key == pygame.K_RIGHT:
                x_change=20
                y_change=0
            elif event.key == pygame.K_UP:
                x_change=0
                y_change=-20
            elif event.key == pygame.K_DOWN:
                x_change=0
                y_change=20
    if x >= screen_width or x<=0 or y>=screen_width or y<=0 :
        game_over = True

    x+=x_change
    y+=y_change
    screen.fill((0,0,0))
    pygame.draw.rect(screen,(255,0,0),[foodx,foody,20,20])
    snake_head =[]
    snake_head.append(x)
    snake_head.append(y)
    snake_list.append(snake_head)
    if len(snake_list) > length_of_snake:
        del snake_list[0]
    for xx in snake_list[:-1]:
        if xx ==snake_head:
            game_over = True
    draw_snake(snake_list)

    pygame.display.update()

    if x==foodx and y==foody :
        print("good to eat!")
        foodx = round(random.randrange(0,screen_width-20)/20.0)*20
        foody = round(random.randrange(0,screen_height-20)/20.0)*20
        length_of_snake += 1

    clock.tick(snake_speed)

message("LOST", (255,0,0))
pygame.display.update()
time.sleep(2)
pygame.quit()