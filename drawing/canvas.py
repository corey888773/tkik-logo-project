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
        for dot in self.points:
            pygame.draw.circle(self.canvas, dot.color, dot.position, dot.size)
        self.screen.blit(self.canvas, (0, 0))
    
    def addDot(self, position: tuple, color: tuple, size=1.0) -> None:
        self.points.append(Dot(position, color, size))
        
    def clear(self) -> None:
        self.points = []
        self.canvas.fill(WHITE)

    def save(self, filepath: str) -> None:
        folder = os.path.dirname(os.path.realpath(__file__)).replace("\\", "/").rpartition('/')[0]
        if not os.path.exists(folder):
            os.makedirs(folder)
        filepath = os.path.join(folder, "images", filepath.replace("\\", "/").rpartition('/')[2])
        print(f"filename = {filepath}")
        
        pygame.image.save(self.canvas, filepath + '.png')
        
    def get_size(self) -> tuple:
        return self.canvas.get_size()