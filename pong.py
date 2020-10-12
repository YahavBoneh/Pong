import pygame
from pong_settings import PongSettings
from paddle import Paddle
import game_functions as gf


def run_game():
    pygame.init()
    settings = PongSettings()
    screen = pygame.display.set_mode((settings.screen.width, settings.screen.height))
    left_paddle = Paddle(screen, settings, is_left=True)
    right_paddle = Paddle(screen, settings, is_left=False)

    while True:
        gf.check_events(left_paddle, right_paddle)
        left_paddle.update()
        right_paddle.update()
        gf.update_screen(screen, settings, left_paddle, right_paddle)


if __name__ == "__main__":
    run_game()
