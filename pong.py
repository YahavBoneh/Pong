import pygame
from pong_settings import PongSettings
from paddle import Paddle
from ball import Ball
from score_board import ScoreBoard
import game_functions as gf


def run_game():
    pygame.init()
    settings = PongSettings()
    screen = pygame.display.set_mode((settings.screen.width, settings.screen.height))
    left_paddle = Paddle(screen, settings, is_left=True)
    right_paddle = Paddle(screen, settings, is_left=False)
    score_board = ScoreBoard(screen, settings)
    ball = Ball(screen, settings, left_paddle, right_paddle, score_board)

    while True:
        gf.process_events(left_paddle, right_paddle)
        left_paddle.update()
        right_paddle.update()
        ball.update()
        score_board.update()
        gf.update_screen(screen, settings, left_paddle, right_paddle, ball, score_board)


if __name__ == "__main__":
    run_game()
