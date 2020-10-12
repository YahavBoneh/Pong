
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


class PongSettings:
    def __init__(self):
        self.screen = ScreenSettings(width=600, height=400, color=(0, 0, 0))
        self.paddle = PaddleSettings(width=10, height=60, distance_from_edge=30, color=(250, 250, 250), speed_factor=0.5)
