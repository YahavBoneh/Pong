import pygame


class Paddle:
    def __init__(self, screen, settings, is_left):
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.settings = settings
        self.is_left = is_left

        self.rect = pygame.Rect(0, 0, self.settings.paddle.width, self.settings.paddle.height)
        self.rect.centery = self.screen_rect.centery
        if self.is_left:
            self.rect.left = settings.paddle.distance_from_edge
        else:
            self.rect.right = self.screen_rect.right - settings.paddle.distance_from_edge

        self.float_centery = float(self.rect.centery)

        self.color = settings.paddle.color
        self.speed_factor = settings.paddle.speed_factor

        self.moving_up = False
        self.moving_down = False

    def get_rect(self):
        return self.rect

    def update(self):
        if self.moving_up and self.rect.top > 0:
            self.float_centery -= min(self.settings.paddle.speed_factor, self.rect.top)
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.float_centery += min(self.settings.paddle.speed_factor, self.screen_rect.bottom-self.rect.bottom)

        self.rect.centery = int(self.float_centery)

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
