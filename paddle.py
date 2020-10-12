import pygame


class Paddle:
    def __init__(self, screen, settings, is_left):
        self.screen = screen
        self.settings = settings
        self.is_left = is_left
        self.screen_rect = self.screen.get_rect()

        if self.is_left:
            self.rect = pygame.Rect(settings.paddle.distance_from_edge, self.screen_rect.centery // 2,
                                    self.settings.paddle.width, self.settings.paddle.height)
        else:
            self.rect = pygame.Rect(self.screen_rect.right - settings.paddle.distance_from_edge,
                                    self.screen_rect.centery // 2, self.settings.paddle.width,
                                    self.settings.paddle.height)

        self.center = float(self.rect.y)

        self.color = settings.paddle.color
        self.speed_factor = settings.paddle.speed_factor

        self.moving_up = False
        self.moving_down = False

    def update(self):
        if self.moving_up and self.rect.top > 0:
            self.center -= min(self.settings.paddle.speed_factor, self.rect.top)
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.center += min(self.settings.paddle.speed_factor, self.screen_rect.bottom-self.rect.bottom)

        self.rect.centery = int(self.center)

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
