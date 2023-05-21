import pygame
import time
from drawing.canvas import Canvas
from drawing.vehicle import Vehicle

class MainWindow:
    window_name: str = 'Logo interpreter'
    window_size: tuple = (800, 600)
    default_color: tuple = (255, 255, 255) # white

    def __init__(self) -> None:
        pygame.init()
        pygame.display.set_caption(self.window_name)
        self.screen = pygame.display.set_mode((800, 600))
        self.canvas = Canvas(self.screen)
        self.vehicle = Vehicle(self.screen, self.canvas)

    def nextFrame(self) -> None:
        self.screen.fill(self.default_color)
        self.canvas.nextFrame()
        self.vehicle.nextFrame()
        pygame.display.flip() # update the screen with what we've drawn.
    
    def run_frames(self, frames: int) -> None:
        for _ in range(frames):
            self.nextFrame()
            time.sleep(1/60)
