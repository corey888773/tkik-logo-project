import pygame
import pygame.freetype

EXECUTION_LINE = "\n=======================================\n"
BLACK = (0, 0, 0)
LIME_GREEN = (50, 205, 50)


class TextField:
    def __init__(self, screen: pygame.Surface, font_size, initial_text=""):
        self.screen = screen
        self.width = screen.get_width()
        self.height = screen.get_height() * .25
        self.pos_x = 0
        self.pos_y = screen.get_height() - self.height
        self.rect = pygame.Rect(self.pos_x, self.pos_y, self.width, self.height)
        self.color = BLACK
        self.font_size = font_size
        self.font = pygame.freetype.SysFont(None, self.font_size)
        self.scroll_pos = 0
        
        if initial_text:
            self.text = initial_text
            self.text += EXECUTION_LINE
        else:
            self.text = ""
            
        self.execution_script = initial_text
        
        self.draw()

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                if self.text.endswith(EXECUTION_LINE):
                    return
                self.text = self.text[:-1]
            elif event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                self.text += '\n'
            else:
                self.text += event.unicode
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 4:  # Scroll up
                self.scroll_up()
            elif event.button == 5:  # Scroll down
                self.scroll_down()

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect, 0)

        visible_lines = self.text.split('\n')[self.scroll_pos:]

        y = self.rect.y + 5
        for line in visible_lines:
            text_surface, _ = self.font.render(line, LIME_GREEN)
            self.screen.blit(text_surface, (self.rect.x + 5, y))
            y += self.font_size + 5

    def scroll_up(self):
        if self.scroll_pos > 0:
            self.scroll_pos -= 1

    def scroll_down(self):
        if self.scroll_pos < len(self.text):
            self.scroll_pos += 1
            
    def get_text(self):
        return self.text
    
    def execute_command(self):
        if self.text.endswith(EXECUTION_LINE):
            return
        
        self.execution_script = self.text.split(EXECUTION_LINE)[-1]
        self.text += EXECUTION_LINE
        
    def save_image(self):    
        self.screen.save()