import pygame
import os

class Dot:
    def __init__(self, position: tuple, color: tuple, size: float) -> None:
        self.position = position
        self.color = color
        self.size = size

class Canvas:
    def __init__(self, screen: pygame.Surface) -> None:
        self.screen = screen
        self.canvas = pygame.Surface(screen.get_size())
        self.clear()

    def nextFrame(self) -> None:
        for dot in self.points:
            pygame.draw.circle(self.screen, dot.color, dot.position, dot.size)
    
    def addDot(self, position: tuple, color: tuple, size=1.0) -> None:
        self.points.append(Dot(position, color, size))
        
    def clear(self) -> None:
        self.points = []
        self.canvas.fill((255, 255, 255))

    def save(self, filename: str, folder: str = 'images') -> None:
        if not os.path.exists(folder):
            os.makedirs(folder)
        folder = os.path.abspath(folder)
        filename = os.path.join(folder, filename)
        print(filename)
        pygame.image.save(self.screen, filename + '.png')