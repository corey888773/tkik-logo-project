import pygame
import time
from drawing.canvas import Canvas
from drawing.vehicle import Vehicle
from drawing.vehicle import Direction
from drawing.text_field import TextField
from drawing.execute_button import ExecuteButton
from drawing.save_button import SaveButton

class MainWindow:
    window_name: str = 'Logo interpreter'
    window_size: tuple = (800, 800)
    default_color: tuple = (0, 0, 0) # white

    def __init__(self, script: str, outfile: str) -> None:
        pygame.init()
        pygame.display.set_caption(self.window_name)
        
        self.is_running = True
        
        self.outfile = outfile
        
        self.screen = pygame.display.set_mode(self.window_size)
        self.screen.fill(self.default_color)
        self.canvas = Canvas(self.screen)
        self.vehicle = Vehicle(self.screen, self.canvas)

        self.text_field = TextField(self.screen, 12, initial_text=script)
        self.execute_button = ExecuteButton(self.screen, self.text_field)
        self.save_button = SaveButton(self.screen, self.text_field)

    def nextFrame(self, event=None) -> bool:
        self.screen.fill(self.default_color)
        self.canvas.nextFrame()

        # Check if the turtle is going outside of the map
        if self.vehicle.is_turtle_outside_map():
            self.vehicle.change_direction(Direction.BACKWARD, 180)
            
        self.vehicle.nextFrame()
        self.text_field.draw()
        self.execute_button.draw()
        self.save_button.draw()
        
        if(event != None):
            self.update_text_field(event)
            
        if self.is_running:
            pygame.display.flip()
        
        return self.is_running
    
    def update_text_field(self, event) -> bool:
        self.text_field.handle_event(event)
        self.text_field.draw()
        self.execute_button.handle_event(event)
        self.execute_button.draw()
        should_save = self.save_button.handle_event(event)
        self.save_button.draw()
        
        if should_save:
            self.save()
            self.is_running = False
        
    def run_frames(self, frames: int) -> None:
        for _ in range(frames):
            self.nextFrame()
            time.sleep(1/300)

    def save(self) -> None:
        self.vehicle.is_turtle_visible = False
        self.run_frames(1)
        self.canvas.save(self.outfile)
        self.vehicle.is_turtle_visible = True
        self.run_frames(1)

        