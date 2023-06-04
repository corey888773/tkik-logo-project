import pygame
import os

WHITE = (255, 255, 255)

class Dot:
    def __init__(self, position: tuple, color: tuple, size: float) -> None:
        self.position = position
        self.color = color
        self.size = size

class Canvas:
    def __init__(self, screen: pygame.Surface) -> None:
        self.screen = screen
        self.sizeX = screen.get_width() 
        self.sizeY = screen.get_height() * .75
        self.canvas = pygame.Surface((self.sizeX, self.sizeY))
        self.canvas.fill(WHITE)
        self.clear()

    def nextFrame(self) -> None:
        # display the canvas on the screen
        self.screen.blit(self.canvas, (0, 0))
        self.canvas.fill(WHITE)
        for dot in self.points:
            pygame.draw.circle(self.screen, dot.color, dot.position, dot.size)
    
    def addDot(self, position: tuple, color: tuple, size=1.0) -> None:
        self.points.append(Dot(position, color, size))
        
    def clear(self) -> None:
        self.points = []
        self.canvas.fill(WHITE)

    def save(self, filename: str, folder: str = 'images') -> None:
        if not os.path.exists(folder):
            os.makedirs(folder)
        folder = os.path.abspath(folder)
        filename = os.path.join(folder, filename)
        print(f"filename = {filename}")
        pygame.image.save(self.screen, filename + '.png')
        
    def get_size(self) -> tuple:
        return self.canvas.get_size()