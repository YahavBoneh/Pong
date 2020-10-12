import pygame
import sys


def key_down_events(event, left_paddle, right_paddle):
    if event.key == pygame.K_UP:
        right_paddle.moving_up = True
    elif event.key == pygame.K_DOWN:
        right_paddle.moving_down = True
    elif event.key == pygame.K_w:
        left_paddle.moving_up = True
    elif event.key == pygame.K_s:
        left_paddle.moving_down = True


def key_up_events(event, left_paddle, right_paddle):
    if event.key == pygame.K_UP:
        right_paddle.moving_up = False
    elif event.key == pygame.K_DOWN:
        right_paddle.moving_down = False
    elif event.key == pygame.K_w:
        left_paddle.moving_up = False
    elif event.key == pygame.K_s:
        left_paddle.moving_down = False


def process_events(left_paddle, right_paddle):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            key_down_events(event, left_paddle, right_paddle)
        elif event.type == pygame.KEYUP:
            key_up_events(event, left_paddle, right_paddle)


def update_screen(screen, settings, left_paddle, right_paddle, ball, score_board):
    screen.fill(settings.screen.color)
    left_paddle.draw()
    right_paddle.draw()
    ball.draw()
    score_board.draw()
    pygame.display.flip()
