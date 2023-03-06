import pygame
from Maze import Maze
from Player import Player

pygame.init()

def create_screen(maze_width, maze_height, cell_size=20):
    """
    Cria uma janela com tamanho baseado nas dimensões do labirinto e tamanho das células.

    Args:
        maze_width (int): largura do labirinto em número de células.
        maze_height (int): altura do labirinto em número de células.
        cell_size (int): tamanho das células em pixels. Default é 20.

    Returns:
        pygame.Surface: superfície da janela criada.

    """
    screen_width = maze_width * cell_size
    screen_height = maze_height * cell_size
    
    # Cria a janela com as dimensões definidas
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Maze")

    # Obtém o retângulo da janela e o centraliza
    screen_rect = screen.get_rect()
    screen_rect.center = (pygame.display.Info().current_w // 2, pygame.display.Info().current_h // 2)

    return screen

def draw_objects(screen, maze, player):
    screen.fill((255, 255, 255))
    maze.draw()
    player.draw(screen)
    pygame.display.flip()
    pygame.time.delay(10) # adiciona um pequeno intervalo de tempo para atualizar a tela novamente


def handle_events(player, maze):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            return True
        
        if event.type == pygame.KEYDOWN:
            new_col = player.col
            new_row = player.row
            if event.key == pygame.K_LEFT:
                new_col -= 1
            elif event.key == pygame.K_RIGHT:
                new_col += 1
            elif event.key == pygame.K_UP:
                new_row -= 1
            elif event.key == pygame.K_DOWN:
                new_row += 1
            
            # Check if the player is trying to move into a wall
            if not maze.cells[new_row][new_col] == "#":
                player.col = new_col
                player.row = new_row
    return False

def main():
    filename = "6 - Maze.png"
    maze = Maze(filename)
    
    threshold = 250
    maze.cells, maze.width, maze.height, maze.object_size = Maze.simplify_pixels(filename, threshold=threshold)
    
    maze.random_start_position(maze.width, maze.height, cells=maze.cells)
    startrow, startcol = maze.start

    player = Player(startcol, startrow, object_size=maze.object_size)
    screen = create_screen(maze.width, maze.height, maze.object_size)
    screen.fill((255, 255, 255))

    clock = pygame.time.Clock()
    fps = 120

    while True:
        clock.tick(fps)
         
        if handle_events(player, maze):
            break
            
        draw_objects(screen, maze, player)
    
    pygame.quit()

   
if __name__ == "__main__":
    main()

