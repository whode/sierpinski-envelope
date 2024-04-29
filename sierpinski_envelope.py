import pygame, random, numba, sys
import numpy as np

@numba.njit(fastmath = True)
def choose_vertex_index(vertices_len, last_vertex_index):
    n1 = last_vertex_index - 1
    n2 = last_vertex_index + 1
    if n1 < 0:
        n1 = vertices_len - 1
    if n2 == vertices_len:
        n2 = 0
    vertex_index = (n1, last_vertex_index, n2)[random.randint(0, 2)]
    return vertex_index

@numba.njit(fastmath = True)
def _update_pixels(pixels, vertices, last_x, last_y, draw_count, last_vertex_index, color):
    for i in range(draw_count):
        vertex_index = choose_vertex_index(len(vertices), last_vertex_index)
        vx, vy = vertices[vertex_index]
        last_x, last_y = (last_x + vx) // 2, (last_y + vy) // 2
        pixels[last_x][last_y] = color
    return last_x, last_y, vertex_index

class ChaosGame:
    def __init__(self, pixels, draw_count, color):
        self.pixels = pixels
        self.draw_count = draw_count
        self.color = color
        w, h, d = pixels.shape
        self.vertices = ((0, 0), (w - 1, 0), (0, h - 1), (w - 1, h - 1))
        self.last_x, self.last_y = w // 2, h // 2
        self.last_vertex_index = 0
    
    def update_pixels(self):
        self.last_x, self.last_y, self.last_vertex_index = _update_pixels(self.pixels, self.vertices, self.last_x,
                                                                          self.last_y, self.draw_count, self.last_vertex_index, self.color)

commands = {}
for i in range(1, len(sys.argv) - 1, 2):
    commands[sys.argv[i]] = sys.argv[i + 1]
    
draw_count = int(commands.get('--draw_count', 1000))
update_count = int(commands.get('--update_count', 1))
draw_color = commands.get('--draw_color', '#ffffff').lstrip('#')
draw_color = tuple(int(draw_color[i: i + 2], 16) for i in (0, 2, 4))
background_color = commands.get('--background_color', '#000000').lstrip('#')
background_color = tuple(int(background_color[i: i + 2], 16) for i in (0, 2, 4))

width, height = 950, 950
        
pixels = np.full((width, height, 3), background_color, dtype = np.uint8)
game = ChaosGame(pixels, draw_count, draw_color)

pygame.init()
img = pygame.image.load('icon.png') 
pygame.display.set_icon(img) 
pygame.display.set_caption('Sierpinski Envelope - Chaos Game')
screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.VIDEORESIZE:
            width, height = event.size
            pixels = np.full((width, height, 3), background_color, dtype = np.uint8)
            game = ChaosGame(pixels, draw_count, draw_color)
            screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
    for i in range(update_count):
        game.update_pixels()
    pygame.surfarray.blit_array(screen, pixels)
    pygame.display.flip()

pygame.quit()