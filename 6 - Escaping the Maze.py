import pygame
import random

# Configurações do labirinto
maze_image = pygame.image.load("6 - Maze.png")
MAZE_WIDTH, MAZE_HEIGHT = maze_image.get_size()
maze_image = pygame.transform.scale(maze_image, (MAZE_WIDTH // 2, MAZE_HEIGHT // 2))

# Criação da janela do jogo
screen = pygame.display.set_mode((MAZE_WIDTH // 2, MAZE_HEIGHT // 2))
pygame.display.set_caption("Labirinto")

# Inicialização do Pygame
pygame.init()

# Definições do labirinto
CELL_SIZE = 40
NUM_ROWS = MAZE_HEIGHT // CELL_SIZE
NUM_COLS = MAZE_WIDTH // CELL_SIZE
WALL_COLOR = (0, 0, 0)
BACKGROUND_COLOR = (255, 255, 255)

# Criar a matriz do labirinto com as paredes
maze = []
for i in range(NUM_ROWS):
    maze.append([1] * NUM_COLS)

# Remover as paredes onde o labirinto tem espaço em branco
for row in range(NUM_ROWS):
    for col in range(NUM_COLS):
        if col * CELL_SIZE >= maze_image.get_width() or row * CELL_SIZE >= maze_image.get_height():
            continue
        if maze_image.get_at((col * CELL_SIZE, row * CELL_SIZE)) == (255, 255, 255):
            maze[row][col] = 0

# Função para gerar uma posição aleatória no labirinto
def get_random_position():
    min_x = CELL_SIZE
    min_y = CELL_SIZE
    max_x = MAZE_WIDTH - CELL_SIZE
    max_y = MAZE_HEIGHT - CELL_SIZE
    x = random.randint(min_x, max_x) // CELL_SIZE * CELL_SIZE
    y = random.randint(min_y, max_y) // CELL_SIZE * CELL_SIZE
    while maze[y // CELL_SIZE][x // CELL_SIZE] == 1:
        # Se a posição gerada estiver dentro de uma parede, tenta novamente
        x = random.randint(min_x, max_x) // CELL_SIZE * CELL_SIZE
        y = random.randint(min_y, max_y) // CELL_SIZE * CELL_SIZE
    return (x, y)

# Função para desenhar um grid de linhas e colunas na tela
def draw_grid():
    for x in range(0, MAZE_WIDTH // 2, CELL_SIZE):
        pygame.draw.line(screen, (128, 128, 128), (x, 0), (x, MAZE_HEIGHT // 2))
    for y in range(0, MAZE_HEIGHT // 2, CELL_SIZE):
        pygame.draw.line(screen, (128, 128, 128), (0, y), (MAZE_WIDTH // 2, y))

# Desenhar o labirinto na tela
def draw_maze():
    for row in range(NUM_ROWS):
        for col in range(NUM_COLS):
            x = col * CELL_SIZE
            y = row * CELL_SIZE
            if maze[row][col] == 1:
                pygame.draw.rect(screen, WALL_COLOR, (x, y, CELL_SIZE, CELL_SIZE))
    draw_grid()


# Desenhar o labirinto e o objeto na tela
def draw_screen():
    screen.fill(BACKGROUND_COLOR)
    screen.blit(maze_image, (0, 0))
    object_color = (255, 0, 0) # vermelho
    object_size = CELL_SIZE // 4 
    pygame.draw.circle(screen, object_color, object_position, object_size)
    pygame.display.update()

def move_object(pos, key):
    x, y = pos
    if key == pygame.K_LEFT:
        x -= CELL_SIZE
    elif key == pygame.K_RIGHT:
        x += CELL_SIZE
    elif key == pygame.K_UP:
        y -= CELL_SIZE
    elif key == pygame.K_DOWN:
        y += CELL_SIZE
    return (x, y)

# Gerar posição aleatória para o objeto, evitando posições com paredes
object_position = get_random_position()
while maze[object_position[1] // CELL_SIZE][object_position[0] // CELL_SIZE] == 1:
    object_position = get_random_position()


# Loop principal do jogo
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        if event.type == pygame.KEYDOWN:
            # Movimentar objeto com as teclas direcionais
            if event.key in [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN]:
                object_position = move_object(object_position, event.key)
                new_position = move_object(object_position, event.key)
                row = new_position[1] // CELL_SIZE
                col = new_position[0] // CELL_SIZE
                if maze[row][col] == 0:
                    # Atualizar a posição do objeto se não houver parede
                    object_position = new_position

    # Desenhar o labirinto e o objeto na tela
    draw_screen()

    # Verificar se o objeto chegou ao final do labirinto
    if object_position[0] == MAZE_WIDTH - CELL_SIZE and object_position[1] == MAZE_HEIGHT - CELL_SIZE:
        print("Você venceu!")
        pygame.time.wait(3000)
        pygame.quit()

    # Atualizar a tela
    pygame.display.update()
