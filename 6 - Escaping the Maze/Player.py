import pygame

class Player:
    def __init__(self, col, row, object_size):
        self.col = col
        self.row = row
        self.object_size = object_size
        self.object_color = (100, 200, 50)
        self.move_left = False
        self.move_right = False
        self.move_up = False
        self.move_down = False
 
    def draw(self, screen):
        rect = pygame.Rect(self.col * self.object_size, self.row * self.object_size, self.object_size, self.object_size)
        pygame.draw.rect(screen, self.object_color, rect)
    
    def move(self, event):
        if event.type == pygame.KEYDOWN:
            new_col = self.col
            new_row = self.row
            if event.key == pygame.K_LEFT:
                new_col -= 1
            elif event.key == pygame.K_RIGHT:
                new_col += 1
            elif event.key == pygame.K_UP:
                new_row -= 1
            elif event.key == pygame.K_DOWN:
                new_row += 1
