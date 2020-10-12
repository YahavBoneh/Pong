import pygame.sysfont


class ScoreBoard:
    def __init__(self, screen, settings):
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.settings = settings

        self.text_color = self.settings.score_board.text_color
        self.font = pygame.font.SysFont(None, settings.score_board.font_size)

        self.left_score = 0
        self.right_score = 0

        self.update()

    def update(self):
        self.text = str(self.left_score) + self.settings.score_board.space_between_scores*" " + str(self.right_score)
        self.score_image = self.font.render(self.text, True, self.text_color, self.settings.screen.color)
        self.score_image_rect = self.score_image.get_rect()
        self.score_image_rect.centerx = self.screen_rect.centerx
        self.score_image_rect.top = 0

    def draw(self):
        self.screen.blit(self.score_image, self.score_image_rect)
