import time
import pygame


# create a pygame window
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Bot")

# create a ping pong paddle
paddle_width = 100
paddle_height = 10
paddle_x = 400
paddle_y = 550
paddle_color = (255, 255, 255)
paddle = pygame.Rect(paddle_x, paddle_y, paddle_width, paddle_height)

# create a small ball
ball_radius = 10
ball_x = 400
ball_y = 50
ball_color = (255, 255, 255)
ball = pygame.Rect(ball_x, ball_y, ball_radius, ball_radius)


# create a score
score = 0
font = pygame.font.SysFont("comicsansms", 30)
text = font.render("Score: " + str(score), True, (255, 255, 255))
text_x = 10
text_y = 10

# make the ball move in a random direction every 5 seconds
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # draw the screen
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, paddle_color, paddle)
    pygame.draw.circle(screen, ball_color, (ball_x, ball_y), ball_radius)
    screen.blit(text, (text_x, text_y))
    pygame.display.update()
    time.sleep(0.05)


    # move the paddle
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        paddle_x -= 10
    if keys[pygame.K_RIGHT]:
        paddle_x += 10

    # define the paddle's new position
    paddle.x = paddle_x
    paddle.y = paddle_y

    # define the ball's new position
    ball_x_change = 0
    ball_y_change = 0

    
    # move the ball
    ball_x = 400
    ball_y = 50
    ball_x += ball_x_change
    ball_y += ball_y_change

    # check if the ball hits the paddle
    if ball_x > paddle_x and ball_x < paddle_x + paddle_width:
        if ball_y > paddle_y and ball_y < paddle_y + paddle_height:
            ball_x_change = -ball_x_change
            ball_y_change = -ball_y_change
            score += 1
            text = font.render("Score: " + str(score), True, (255, 255, 255))

    # check if the ball hits the top or bottom of the screen
    if ball_y <= 0:
        ball_y_change = -ball_y_change
    if ball_y >= 600:
        ball_y_change = -ball_y_change

    # check if the ball hits the left or right of the screen
    if ball_x <= 0:
        ball_x_change = -ball_x_change
    if ball_x >= 800:
        ball_x_change = -ball_x_change


    # check if the ball hits the paddle
    if ball_x > paddle_x and ball_x < paddle_x + paddle_width:
        if ball_y > paddle_y and ball_y < paddle_y + paddle_height:
            ball_x_change = -ball_x_change
            ball_y_change = -ball_y_change
            score += 1
            text = font.render("Score: " + str(score), True, (255, 255, 255))

    # make the ball invert the direction when it hits the top or bottom of the screen
    if ball_y <= 0:
        ball_y_change = -ball_y_change
    if ball_y >= 600:
        ball_y_change = -ball_y_change

    # make the ball invert the direction when it hits the left or right of the screen
    if ball_x <= 0:
        ball_x_change = -ball_x_change
    if ball_x >= 800:
        ball_x_change = -ball_x_change

    # when the player presses the 'q' key, the game will quit
    if keys[pygame.K_q]:
        pygame.quit()
        quit()

    # don't let the paddle go off the screen
    if paddle_x < 0:
        paddle_x = 0
    if paddle_x > 700:
        paddle_x = 700
        
