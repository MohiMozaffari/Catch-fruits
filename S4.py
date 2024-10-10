import pygame
import random

pygame.init()

SCREEN_WIDTH = 1080
SCREEN_HEIGHT = 720
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Catch the Fruits")


#Player
player_width = 100
player_height = 30
player_x = SCREEN_WIDTH // 2 - player_width // 2
player_y = SCREEN_HEIGHT - player_height
player_speed = 8


def draw_player(x, y):
    pygame.draw.rect(screen, (245, 66, 129), (x, y, player_width, player_height))


#Fruit
fruit_width = 50
fruit_height = 50
fruit_x = 400
fruit_y = 0
fruit_speed = 5

def draw_fruit(x, y):
    pygame.draw.rect(screen, (255, 0,0), (x,y, fruit_width, fruit_height))


clock = pygame.time.Clock()

running = True
while running:
    
    screen.fill((148, 221, 255))

    draw_player(player_x, player_y)
    draw_fruit(fruit_x, fruit_y)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    
    if keys[pygame.K_RIGHT]:
        player_x += player_speed
    
    #Boundries for the player
    if player_x < 0:
        player_x = 0

    elif player_x > SCREEN_WIDTH - player_width :
        player_x = SCREEN_WIDTH - player_width

    #fruit movment
    fruit_y += fruit_speed

    #collision detection
    if player_x < fruit_x + fruit_width and player_x + player_width > fruit_x and player_y < fruit_y + fruit_height and player_y + player_height > fruit_y:
        fruit_x = random.randint(0, SCREEN_WIDTH - fruit_width)
        fruit_y = 0

    pygame.display.flip()
    clock.tick(60)
pygame.quit()
