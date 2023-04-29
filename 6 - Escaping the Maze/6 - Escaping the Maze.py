import pygame
from Maze import Maze
from Player import Player
import time

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


def handle_events(player, maze, screen):
    
    # Flag para indicar se o jogador já alcançou a célula de saída
    reached_exit = False

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            return True
        
        if event.type == pygame.KEYDOWN:
            # Atualizar o estado da variável de estado da tecla correspondente
            if event.key == pygame.K_LEFT:
                player.move_left = True
            elif event.key == pygame.K_RIGHT:
                player.move_right = True
            elif event.key == pygame.K_UP:
                player.move_up = True
            elif event.key == pygame.K_DOWN:
                player.move_down = True
        
        elif event.type == pygame.KEYUP:
            # Atualizar o estado da variável de estado da tecla correspondente
            if event.key == pygame.K_LEFT:
                player.move_left = False
            elif event.key == pygame.K_RIGHT:
                player.move_right = False
            elif event.key == pygame.K_UP:
                player.move_up = False
            elif event.key == pygame.K_DOWN:
                player.move_down = False
    
    # Mover o jogador de acordo com o estado das variáveis de estado da tecla correspondente
    new_col = player.col
    new_row = player.row
    if player.move_left:
        new_col -= 1
    elif player.move_right:
        new_col += 1
    elif player.move_up:
        new_row -= 1
    elif player.move_down:
        new_row += 1

    # Verificar se o jogador alcançou a célula de saída
    if maze.cells[player.row][player.col] == "$":
        reached_exit = True
    
    # Se o jogador já alcançou a célula de saída
    if reached_exit:
        draw_message(screen, "Parabéns, você concluiu o labirinto!")
        # Aguardar 3 segundos antes de encerrar o jogo
        time.sleep(3)
        pygame.quit()
        return True
    
    # Verificar se o jogador está tentando se mover para uma parede
    if not maze.cells[new_row][new_col] == "#":
        player.col = new_col
        player.row = new_row
                
    return False

def draw_message(screen, message):
    font = pygame.font.SysFont('comicsansms', 30)
    text = font.render(message, True, (150, 150, 150))
    text_rect = text.get_rect()
    text_rect.center = (screen.get_width() // 2, screen.get_height() // 2)
    screen.blit(text, text_rect)
    pygame.display.flip()

def main():
    filename = "6 - Maze.png"
    maze = Maze(filename)
    
    threshold = 250
    maze.cells, maze.width, maze.height, maze.object_size = Maze.simplify_pixels(filename, threshold=threshold)
    
    #maze.find_exit_cells(maze)

    maze.random_start_position(maze.width, maze.height, cells=maze.cells)
    startrow, startcol = maze.start

    maze.find_exit_cells()

    player = Player(startcol, startrow, object_size=maze.object_size)
    screen = create_screen(maze.width, maze.height, maze.object_size)
    screen.fill((255, 255, 255))

    clock = pygame.time.Clock()
    fps = 120

    while True:
        clock.tick(fps)
         
        if handle_events(player, maze, screen):
            break
            
        draw_objects(screen, maze, player)
    
    pygame.quit()

   
if __name__ == "__main__":
    main()

