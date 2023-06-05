import pygame
from drawing.text_field import TextField

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class SaveButton:
    def __init__(self, screen: pygame.Surface, text_field: TextField):
        self.screen = screen
        self.text_field = text_field
        
        self.button_rect = pygame.Rect(0, 0, 100, 30)
        self.button_color = WHITE
        self.button_text = "Save"
        self.button_font = pygame.freetype.SysFont(None, 18)
        
        # make this buttoon on the right corner of the text field 
        self.button_rect.x = self.text_field.rect.x + self.text_field.rect.width - self.button_rect.width - 10
        self.button_rect.y = self.text_field.rect.y + self.text_field.rect.height - self.button_rect.height - self.button_rect.height - 20
        
        self.draw()

    def handle_event(self, event) -> bool:
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                pos = pygame.mouse.get_pos()
                if self.button_rect.collidepoint(pos):
                    return True
                return False       

    def draw(self):
        pygame.draw.rect(self.screen, self.button_color, self.button_rect, 0)
        button_text_surface, _ = self.button_font.render(self.button_text, BLACK)
        button_text_x = self.button_rect.x + (self.button_rect.width - button_text_surface.get_width()) // 2
        button_text_y = self.button_rect.y + (self.button_rect.height - button_text_surface.get_height()) // 2
        self.screen.blit(button_text_surface, (button_text_x, button_text_y))