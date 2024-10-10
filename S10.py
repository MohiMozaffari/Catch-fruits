import pygame
import random

pygame.init()
pygame.font.init()
pygame.mixer.init()

SCREEN_WIDTH = 1080
SCREEN_HEIGHT = 720
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Catch the Fruits")

#Song
BACK_SOUND = pygame.mixer.Sound("01 - Wolfgang Amadeus Mozart.mp3")
GAME_OVER_SOUND  = pygame.mixer.Sound("mixkit-falling-game-over-1942.wav")
BONUS_SOUND = pygame.mixer.Sound("game-bonus.mp3")
FAIL_SOUND = pygame.mixer.Sound("mixkit-failure.wav")

#Player
player_width = 250
player_height = 70
player_x = SCREEN_WIDTH // 2 - player_width // 2
player_y = SCREEN_HEIGHT - player_height
player_speed = 8


def draw_player(x, y):
    screen.blit(basket, (x, y))


#Fruit
fruit_width = 100
fruit_height = 100
fruit_x = 400
fruit_y = 0
fruit_speed = 5


BACKGROUND_IMAGE = pygame.image.load("Background.jpg")
BACKGROUND = pygame.transform.scale(BACKGROUND_IMAGE, (SCREEN_WIDTH, SCREEN_HEIGHT))
basket = pygame.transform.scale(pygame.image.load('basket.png'), (player_width, player_height))
FRUIT_IMAGE = pygame.image.load("Apple.png")

apple_img = pygame.transform.scale(FRUIT_IMAGE, (fruit_width, fruit_height))
watermelon_img = pygame.transform.scale(pygame.image.load("watermelon.png"), (fruit_width, fruit_height))
cherry_img = pygame.transform.scale(pygame.image.load("cherry.png"), (fruit_width, fruit_height))
pineapple_img = pygame.transform.scale(pygame.image.load("pineapple.png"), (fruit_width, fruit_height))

fruit_images = [apple_img, watermelon_img, pineapple_img, cherry_img]
fruit = random.choice(fruit_images)


def draw_fruit(x, y, fruit):
    screen.blit(fruit, (x, y))

#set up health
health = 3
heart_padding = 20
heart_image = pygame.transform.scale(pygame.image.load("heart.png"), (50,45))



def draw_hearts():
    heart_images = [heart_image for _ in range(health)]
    heart_x = SCREEN_WIDTH - len(heart_images) * (heart_image.get_width() + heart_padding)
    heart_y = 10
    for i, heart in enumerate(heart_images):
        screen.blit(heart, (heart_x + i * (heart.get_width() + heart_padding), heart_y))


#set up box
box = pygame.transform.scale(pygame.image.load("box.png"), (fruit_width, fruit_height))
box_x = random.randint(0, SCREEN_WIDTH - fruit_width)
box_y = 0
box_speed = 6

def draw_box(x,y):
    screen.blit(box, (x,y))


#set up heart
heart = pygame.transform.scale(pygame.image.load("heart.png"), (fruit_width, fruit_height))
heart_x = random.randint(0, SCREEN_WIDTH - fruit_width)
heart_y = - fruit_height
heart_speed = random.randint(5,10)

def draw_heart(x,y):
    screen.blit(heart, (x,y))

def game_over():
    GAME_OVER_SOUND.play()
    game_over_font = pygame.font.SysFont("Cheri liney", 82)
    game_over_text = game_over_font.render("Game Over", True, (0, 0, 0))
    screen.blit(game_over_text, (SCREEN_WIDTH//2 - game_over_text.get_width()//2, SCREEN_HEIGHT//2 - game_over_text.get_height()//2))
    pygame.display.flip()
    pygame.time.delay(2000)
    pygame.quit()


text_font = pygame.font.SysFont("IRAN Sans", 32)

clock = pygame.time.Clock()

score = 0
running = True
box_flag = False
heart_flag = False
BACK_SOUND.play()
while running:
    
    screen.blit(BACKGROUND, (0,0))

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

    #box
    if random.randint(1,600) == 50:
        box_flag = True

    if box_flag:
        box_y += box_speed

        if box_y >= SCREEN_HEIGHT:
            box_x = random.randint(0, SCREEN_WIDTH - box.get_width())
            box_y = - box.get_height()
            box_speed = random.randint(5,10)
            box_flag = False
        else:
            draw_box(box_x, box_y)

        if player_x < box_x + box.get_width() and player_x + player_width > box_x and player_y < box_y + box.get_height() and player_y + player_height > box_y:
            score += 10
            BONUS_SOUND.play()
            box_x = random.randint(0, SCREEN_WIDTH - box.get_width())
            box_y = - box.get_height()
            box_speed = random.randint(5,10)
            box_flag = False

    #heart
    if random.randint(1,1200) == 100 and health <= 4:
        heart_flag = True

    if heart_flag:
        heart_y += heart_speed

        if heart_y >= SCREEN_HEIGHT:
            heart_x = random.randint(0, SCREEN_WIDTH - heart.get_width())
            heart_y = - heart.get_height()
            heart_speed = random.randint(5,10)
            heart_flag = False
        else:
            draw_heart(heart_x, heart_y)

        if player_x < heart_x + heart.get_width() and player_x + player_width > heart_x and player_y < heart_y + heart.get_height() and player_y + player_height > heart_y:
            health += 1
            BONUS_SOUND.play()
            heart_x = random.randint(0, SCREEN_WIDTH - heart.get_width())
            heart_y = - heart.get_height()
            heart_speed = random.randint(5,10)
            heart_flag = False

    if fruit_y >= SCREEN_HEIGHT:
        health -=1
        FAIL_SOUND.play()
        if health > 0:
            fruit = random.choice(fruit_images)
            fruit_x = random.randint(0, SCREEN_WIDTH - fruit_width)
            fruit_y = 0
        else:
            game_over()

    #collision detection
    if player_x < fruit_x + fruit_width and player_x + player_width > fruit_x and player_y < fruit_y + fruit_height and player_y + player_height > fruit_y:
        score += 1
        fruit = random.choice(fruit_images)
        fruit_x = random.randint(0, SCREEN_WIDTH - fruit_width)
        fruit_y = 0

    score_text = text_font.render("Score: " + str(score), True, (255,0,0))
    screen.blit(score_text, (10,10))

    draw_player(player_x, player_y)
    draw_fruit(fruit_x, fruit_y, fruit)
    draw_hearts()


    pygame.display.flip()
    clock.tick(60)
pygame.quit()
