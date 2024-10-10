import pygame

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Catch the Fruits")

player_width = 100
player_height = 30
player_x = SCREEN_WIDTH // 2 - player_width // 2
player_y = SCREEN_HEIGHT - player_height

def draw_player(x, y):
    pygame.draw.rect(screen, (245, 66, 129), (x, y, player_width, player_height))


player_speed = 8

keys = pygame.key.get_pressed()




running = True
while running:
    
    screen.fill((148, 221, 255))

    draw_player(player_x, player_y)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
pygame.quit()
