import pygame
import math
from drawing.pen import Pen

class Direction:
    FORWARD = 0
    RIGHT = 1
    BACKWARD = 2
    LEFT = 3

class Vehicle:
    def __init__(self, screen: pygame.Surface, canvas) -> None:
        self.screen: pygame.Surface = screen
        self.screen_size: tuple = canvas.get_size()
        self.image = pygame.image.load('./drawing/assets/vehicle.png').convert_alpha()
        self.img_size = (32, 32)
        
        # scale the image
        self.image = pygame.transform.scale(self.image, self.img_size)
        # mirror the image
        self.image = pygame.transform.flip(self.image, True, False)
        
        self.position: tuple = (self.screen_size[0]/2 - self.img_size[0]/2,
                                self.screen_size[1]/2 - self.img_size[1]/2)
        self.rotation: int = 0
        self.pen = Pen(screen, canvas, self.get_center_position())
        
        self.remaining_distance = 0
        
        self.is_turtle_visible = True
        self.go_home()
        
        
    def nextFrame(self) -> None:
        self.move()
        
        rotated_image = pygame.transform.rotate(self.image, -self.rotation)
        
        self.pen.draw(self.get_center_position())

        if self.is_turtle_visible:
            self.screen.blit(rotated_image, self.position) # draw the rotated image

    def move(self) -> None:
        if self.remaining_distance > 0:
            self.change_position()
            self.remaining_distance -= 1
        
    def change_position(self) -> None:
        self.position = (self.position[0] + math.cos(math.radians(self.rotation)),
                            self.position[1] + math.sin(math.radians(self.rotation)))
        

    def set_position(self, position: tuple) -> None:
        # 0 0 is the center of the screen
        self.position = (position[0] + self.screen_size[0]/2 - self.img_size[0]/2,
                            - position[1] + self.screen_size[1]/2 - self.img_size[1]/2)
        self.rotation = 0
        
    def change_direction(self, direction: Direction, degrees=0) -> None:
        if direction == Direction.RIGHT:
            self.rotation += degrees
        elif direction == Direction.LEFT:
            self.rotation -= degrees
        elif direction == Direction.BACKWARD:
            self.rotation += 180
        else :
            pass
        
    def go_home(self) -> None:
        self.position = (self.screen_size[0]/2 - self.img_size[0]/2,
                            self.screen_size[1]/2 - self.img_size[1]/2)
        self.rotation = 0

    def get_center_position(self) -> tuple:
        return (self.position[0] + self.img_size[0]/2,
                self.position[1] + self.img_size[1]/2)

    def is_turtle_outside_map(self) -> bool:
        map_width, map_height = self.screen_size
        turtle_x, turtle_y = self.get_center_position()

        return (
                turtle_x < 0 or turtle_x > map_width
                or turtle_y < 0 or turtle_y > map_height
        )

