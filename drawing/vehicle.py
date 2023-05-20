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
        self.screen_size: tuple = screen.get_size()
        self.image = pygame.image.load('./drawing/assets/vehicle.png').convert_alpha()
        self.img_size = (32, 32)
        
        self.image = pygame.transform.scale(self.image, self.img_size)

        self.position: tuple = (self.screen_size[0]/2 - self.img_size[0]/2,
                                self.screen_size[1]/2 - self.img_size[1]/2)
        self.rotation: int = 0
        self.pen = Pen(screen, canvas, self.get_center_position())
        
        self.remaining_distance = 0
        
    def nextFrame(self) -> None:
        self.move()
        rotated_image = pygame.transform.rotate(self.image, -self.rotation)
        # self.move(self.velocity[0], self.velocity[1])
        self.pen.draw(self.get_center_position())

        self.screen.blit(rotated_image, self.position) # draw the rotated image

    def move(self) -> None:
        if self.remaining_distance > 0:
            self.change_position()
            self.remaining_distance -= 1
        
    def change_position(self) -> None:
        self.position = (self.position[0] + math.cos(math.radians(self.rotation)),
                            self.position[1] + math.sin(math.radians(self.rotation)))
        

    def set_position(self, position: tuple) -> None:
        self.position = position
        
    def change_direction(self, direction: Direction) -> None:
        if direction == Direction.RIGHT:
            self.rotation -= 90
        elif direction == Direction.LEFT:
            self.rotation += 90
        elif direction == Direction.BACKWARD:
            self.rotation += 180
        else :
            pass

    def get_center_position(self) -> tuple:
        return (self.position[0] + self.img_size[0]/2, self.position[1] + self.img_size[1]/2)
        