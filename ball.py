import pygame
import random
import numpy as np
from score_board import ScoreBoard


def normalize(v):
    u = np.array(v)
    norm = np.linalg.norm(u)
    if norm == 0:
        return u.tolist()
    return (u / norm).tolist()


def random_normalized_vector(max_slope):
    return normalize([random.choice([1, -1]), random.uniform(-1 * max_slope, max_slope)])


class Ball:
    def __init__(self, screen, settings, left_paddle, right_paddle, score_board):
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.settings = settings
        self.left_paddle = left_paddle
        self.right_paddle = right_paddle
        self.left_paddle_rect = self.left_paddle.get_rect()
        self.right_paddle_rect = self.right_paddle.get_rect()
        self.score_board = score_board

        self.direction = random_normalized_vector(self.settings.ball.max_first_slope)

        self.image = pygame.transform.scale(pygame.image.load(self.settings.ball.picture_path),
                                            (2 * self.settings.ball.radius, 2 * settings.ball.radius))
        self.rect = self.image.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery

        self.float_centerx = float(self.rect.centerx)
        self.float_centery = float(self.rect.centery)

        self.speed_factor = self.settings.ball.speed_factor

    def update(self):
        if self.rect.top < 0:
            self.direction[1] = abs(self.direction[1])
        elif self.rect.bottom > self.screen_rect.bottom:
            self.direction[1] = -abs(self.direction[1])

        if self.rect.colliderect(self.left_paddle_rect) and self.rect.left >= self.left_paddle_rect.left:
            self.direction[0] = abs(self.direction[0])
        elif self.rect.colliderect(self.right_paddle_rect) and self.rect.right <= self.right_paddle_rect.right:
            self.direction[0] = -abs(self.direction[0])

        if self.rect.left < 0 or self.rect.right > self.screen_rect.right:
            if self.rect.left < 0:
                self.score_board.right_score += 1
            else:
                self.score_board.left_score += 1

            self.rect.centerx = self.screen_rect.centerx
            self.rect.centery = self.screen_rect.centery
            self.float_centerx = float(self.rect.centerx)
            self.float_centery = float(self.rect.centery)
            self.direction = random_normalized_vector(self.settings.ball.max_first_slope)
            return

        self.float_centerx += self.direction[0] * self.speed_factor
        self.float_centery += self.direction[1] * self.speed_factor

        self.rect.centerx = int(self.float_centerx)
        self.rect.centery = int(self.float_centery)

    def draw(self):
        self.screen.blit(self.image, self.rect)
