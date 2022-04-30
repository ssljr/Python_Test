import sys
import pygame


def run_game():
    pygame.init()
    size = width, height = 320, 240
    speed = [2, 2]
    black = 0, 0, 0
    screen = pygame.display.set_mode(size)

    ball = pygame.image.load("intro_ball.gif")
    ball_test = ball.get_rect()
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        ball_test = ball_test.move(speed)
        if ball_test.left < 0 or ball_test.right > width:
            speed[0] = -speed[0]
        if ball_test.top < 0 or ball_test.bottom > height:
            speed[1] = -speed[1]
        screen.fill(black)
        screen.blit(ball, ball_test)
        pygame.display.flip()


run_game()
