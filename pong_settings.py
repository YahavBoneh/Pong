
class ScreenSettings:
    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = color


class PaddleSettings:
    def __init__(self, width, height, distance_from_edge, color, speed_factor):
        self.width = width
        self.height = height
        self.distance_from_edge = distance_from_edge
        self.color = color
        self.speed_factor = speed_factor


class BallSettings:
    def __init__(self, radius, picture_path, speed_factor, max_first_slope):
        self.radius = radius
        self.picture_path = picture_path
        self.speed_factor = speed_factor
        self.max_first_slope = max_first_slope


class ScoreBoardSettings:
    def __init__(self, text_color, font_size, space_between_scores):
        self.text_color = text_color
        self.font_size = font_size
        self.space_between_scores = space_between_scores


class PongSettings:
    def __init__(self):
        self.screen = ScreenSettings(width=600, height=400, color=(0, 0, 0))
        self.paddle = PaddleSettings(width=10, height=60, distance_from_edge=30, color=(250, 250, 250), speed_factor=0.5)
        self.ball = BallSettings(radius=10, picture_path="Figures/ball.bmp", speed_factor=0.25, max_first_slope=1)
        self.score_board = ScoreBoardSettings(text_color=(250, 250, 250), font_size=48, space_between_scores=5)
