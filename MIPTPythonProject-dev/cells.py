import pygame
import colours as cl
import random

square_rule = "RL"
hexagonal_rule = "54454"
square_rule_length = len(square_rule)
hexagonal_rule_length = len(hexagonal_rule)
square_colours = []
hexagonal_colours = []
for x in range(hexagonal_rule_length):
    hexagonal_colours.append(cl.standard_colours[random.randint(0, len(cl.standard_colours) - 1)])
for x in range(square_rule_length):
    square_colours.append(cl.standard_colours[random.randint(0, len(cl.standard_colours) - 1)])
dis_width = 800
dis_height = 800

size = 1
hex_size = 1
N = int(dis_height // size)
M = int(dis_width // size)

dis = pygame.display.set_mode((dis_width + 400, dis_height))

class HexCell:
    x, y = 0, 0
    colour = 0
    def Draw(self):
        pygame.draw.polygon(dis, hexagonal_colours[self.colour],
                            [[self.x, self.y], [self.x + 3**(1/2) / 2 * hex_size, self.y - 0.5 * hex_size],
                            [self.x + 3**(1/2) * hex_size, self.y], [self.x + 3**(1/2) * size, self.y + hex_size],
                            [self.x + 3**(1/2) / 2 * hex_size, self.y + 1.5 * hex_size], [self.x, self.y + hex_size]])


class Cell:
    x, y = 0, 0
    colour = 0

    def Draw(self):
        pygame.draw.rect(dis, square_colours[self.colour], [self.x * size, self.y * size, size, size])