import pygame
import time
from drawing.canvas import Canvas
from drawing.vehicle import Vehicle
from drawing.text_field import TextField
from drawing.execute_button import ExecuteButton

class MainWindow:
    window_name: str = 'Logo interpreter'
    window_size: tuple = (800, 600)
    default_color: tuple = (0, 0, 0) # white

    def __init__(self, program) -> None:
        pygame.init()
        pygame.display.set_caption(self.window_name)
        self.screen = pygame.display.set_mode((800, 600))
        self.screen.fill(self.default_color)
        self.canvas = Canvas(self.screen)
        self.vehicle = Vehicle(self.screen, self.canvas)

        self.text_field = TextField(self.screen, 12, initial_text=program)
        self.execute_button = ExecuteButton(self.screen, self.text_field)

    def nextFrame(self, event=None) -> None:
        self.screen.fill(self.default_color)
        self.canvas.nextFrame()
        self.vehicle.nextFrame()
        
        if(event != None):
            self.update_text_field(event)
            
        pygame.display.flip() # update the screen with what we've drawn.
    
    def update_text_field(self, event) -> None:
        self.text_field.handle_event(event)
        self.text_field.draw()
        self.execute_button.handle_event(event)
        self.execute_button.draw()
    
    def run_frames(self, frames: int) -> None:
        for _ in range(frames):
            self.nextFrame()
            time.sleep(1/300)

    def save(self, filename: str) -> None:
        self.vehicle.is_turtle_visible = False
        self.run_frames(1)
        self.canvas.save(filename)
        