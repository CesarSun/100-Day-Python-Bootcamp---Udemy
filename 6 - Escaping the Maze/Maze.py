import pygame     # importa a biblioteca Pygame para criar jogos em Python
import random
import math
from PIL import Image, ImageDraw   # importa a biblioteca Pillow para processamento de imagem em Python
from pygame.locals import QUIT


class Maze:
    def __init__(self, filename):  # define uma classe Maze que recebe um nome de arquivo como argumento
        if not isinstance(filename, str):
            raise ValueError("O nome do arquivo deve ser uma string.")
        self.filename = filename  # atribui o nome do arquivo recebido ao atributo de classe filename
        self.object_size = 0  # armazena o tamanho do objeto como atributo da classe
        self.width = 0  # atribui 0 ao atributo de classe width
        self.height = 0  # atribui 0 ao atributo de classe height
        self.walls = set()  # cria um conjunto vazio para armazenar as paredes do labirinto
        self.start = (0, 0)  # atribui a posição de partida do jogador como (0, 0)
        self.cells = None   # cria um atributo de classe cells para armazenar a matriz de células do labirinto
        
    def convert_to_bw(pixel, threshold):
        # Calcula a intensidade do pixel como a média dos valores RGB
        intensity = sum(pixel) // 3
        
        # Atribui a cor preta ou branca ao pixel dependendo da intensidade em relação ao limiar
        if intensity < threshold:
            return (0, 0, 0) # preto
        else:
            return (255, 255, 255) # branco

    @staticmethod
    def simplify_pixels(filename, threshold=126):
        try:
            with Image.open(filename) as img:
                pixels = img.load()
                width, height = img.size
        except (FileNotFoundError, IOError) as e:
            print(f"Erro ao abrir a imagem: {e}")
            return None, None, None, None

        # Exibe a imagem original em uma nova janela
        #img.show()
        
        # Calcula o tamanho ideal para uma célula, baseado no tamanho da imagem
        cell_size = math.gcd(width, height)
        
        if cell_size == 0 or cell_size == 1 or cell_size >= 50:
            print("AVISO: tamanho da célula ajustado para", cell_size)
            cell_size = 9
        print("cell_size:", cell_size)
        
        # Calcula a quantidade de células em cada direção
        cells_x = width // cell_size
        cells_y = height // cell_size
        
        # Cria uma matriz de células para representar o labirinto
        cells = [[None for _ in range(cells_x)] for _ in range(cells_y)]

        # Cria uma nova imagem para representar a grade de células
        grid_img = img.copy()
        grid_draw = ImageDraw.Draw(grid_img)
        cell_w = width // cells_x
        cell_h = height // cells_y
        for y in range(cells_y):
            for x in range(cells_x):
                grid_draw.rectangle((x * cell_w, y * cell_h, (x + 1) * cell_w, (y + 1) * cell_h), outline="black")

        # Exibe a nova imagem em uma nova janela
        #grid_img.show()

        # Preenche a matriz de células com paredes ou corredores
        for y in range(cells_y):
            for x in range(cells_x):
                # Verifica se a célula é uma parede ou um corredor
                wall_count = 0 # contador de pixels que são considerados paredes
                total_count = 0 # contador de pixels dentro da célula
                for j in range(cell_size): # loop sobre os pixels da célula ao longo do eixo y
                    for i in range(cell_size): # loop sobre os pixels da célula ao longo do eixo x
                        
                        # Calcula a posição absoluta do pixel na imagem original
                        px, py = x * cell_size + i, y * cell_size + j
                        
                        # Verifica se a posição do pixel está dentro dos limites da imagem original
                        if px >= width or py >= height:
                            continue # pula para a próxima iteração se a posição estiver fora dos limites
                        
                        # Obtém a cor do pixel na posição (px, py)
                        color = Maze.convert_to_bw(pixels[px, py], threshold=threshold)
                                                
                        # Verifica se a cor do pixel é uma cor de parede (valor abaixo do limiar)
                        if sum(color) / 3 > threshold:
                            wall_count += 1 # incrementa o contador de paredes se a cor for uma cor de parede 
                        total_count += 1 # incrementa o contador total de pixels dentro da célula
                
                # Verifica se a célula é uma parede ou um corredor com base na proporção de pixels de parede na célula
                if wall_count / total_count >= 1: # se todos os pixels forem considerados paredes
                    cells[y][x] = " " # a célula é uma parede
                else:
                    cells[y][x] = "#" # a célula é um corredor
        
        # Cria uma nova imagem para representar o labirinto simplificado
        maze_img = Image.new("RGB", (width, height), color="black")
        maze_draw = ImageDraw.Draw(maze_img)
        cell_w = width // cells_x
        cell_h = height // cells_y
        for y in range(cells_y):
            for x in range(cells_x):
                if cells[y][x] == "#":
                    maze_draw.rectangle((x * cell_w, y * cell_h, (x + 1) * cell_w, (y + 1) * cell_h), fill="white")

        # Exibe a nova imagem em uma nova janela
        #maze_img.show()

        return cells, cells_x, cells_y, cell_size

    def draw(self, cell_size=20): #alteração
        
        cell_size = self.object_size
        width = len(self.cells[0]) * cell_size
        height = len(self.cells) * cell_size
        
        screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Maze")
        
        colors = {"#": (0, 0, 0), " ": (255, 255, 255)}
        
        for y in range(len(self.cells)):
            for x in range(len(self.cells[y])):
                rect = pygame.Rect(x * cell_size, y * cell_size, cell_size, cell_size)
                color = colors[self.cells[y][x]]
                pygame.draw.rect(screen, color, rect)
                
    def random_start_position(self, cells_x, cells_y, cells):
        """
        Escolhe uma posição aleatória para iniciar o jogador no labirinto.

        Args:
            cells_x (int): número de colunas de células no labirinto.
            cells_y (int): número de linhas de células no labirinto.
            cells (list): uma lista de listas que representa as células do labirinto,
                onde 0 representa uma célula vazia e 1 representa uma parede.

        """
        try:
            startrow = random.randint(0, cells_y-1)
            startcol = random.randint(0, cells_x-1)
            
                      
            # Verifica se a lista de células tem as dimensões corretas
            if len(cells) != cells_y or len(cells[0]) != cells_x:
                print(f"startrow: {startrow}, startcol: {startcol}, cells_x: {cells_x}, cells_y: {cells_y}")
                raise ValueError("As dimensões da lista de células não correspondem aos valores especificados por cells_x e cells_y.")

            # verifica se a posição escolhida está dentro dos limites do labirinto e não é uma parede
            
            if startrow >= cells_y or startcol >= cells_x or cells[startrow][startcol] == "#":
                # contador de tentativas
                attempts = 0

                # loop até encontrar uma posição válida ou atingir 10 tentativas
                while True:
                    # se já tentou 10 vezes, interrompe o loop
                    if attempts == 10:
                        print("Não foi possível encontrar uma posição inicial válida após 10 tentativas.")
                        break

                    # escolhe uma linha e uma coluna aleatória
                    print("Invalid starting position, finding new position...")
                    print("startrow", startrow)
                    print("startcol", startcol)
                    startrow = random.randint(0, cells_y-1)
                    startcol = random.randint(0, cells_x-1)

                    # verifica se a posição escolhida está dentro dos limites do labirinto e não é uma parede
                    if startrow < cells_y and startcol < cells_x and cells[startrow][startcol] != 1:
                        break

                    # incrementa o contador de tentativas
                    attempts += 1


            # define a posição de início do jogador como uma tupla (row, col)
            self.start = (startrow, startcol)
        except Exception as e:
            print(f"Error in random_start_position: {e}")
            self.start = None
