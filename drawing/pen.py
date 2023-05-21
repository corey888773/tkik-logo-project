import pygame
from copy import deepcopy
from interpreter.logger import Logger

class Pen:

    def __init__(self, screen: pygame.Surface, canvas, position: tuple) -> None:
        self.screen: pygame.Surface = screen
        self.screen_size: tuple = screen.get_size()
        self.canvas = canvas

        self.color = (0,0,0)
        self.width = 1

        self.drawing_state = True

    def set_color(self, color: tuple) -> None:
        self.color = color

    def draw(self, position: tuple) -> None:
        pos = deepcopy(position)

        if self.drawing_state:
            self.canvas.addDot(pos, self.color, self.width)
    
    def set_pen_size(self, width) -> None:
        self.width = width

    def switch_drawing_state(self) -> None:
        self.drawing_state = not self.drawing_state