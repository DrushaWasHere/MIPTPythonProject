import pygame
import time
import random
import colours as cl
import buttons as bt
import ants

pygame.init()

clock = pygame.time.Clock()

FONT = pygame.font.Font(None, 32)

global square_rule, hexagonal_rule, hexagonal_rule_length, square_rule_length
square_rule = "RL"
hexagonal_rule = "54454"
tick = 1
steps_per_tick = 1


# 54454
# 44441 roads
# 44544 snowflakes :)
# 42221 not bad
# 54444
# 54554 another WOOWOWOWOWOW
# 54554 WOOOOOOOOOOOW
# 54141
# 55225
# 4441
# 5444
# 5414
# 5511
# 544
# 12521
# 12221
# 121
# 200121
# 3315133
# 5403452
#
#
# L1 R3 R3 L1
# L1 L1 R1 R1
# L4 L0 L0 L5 L4 L5
# L2 L0 L0 L1 L2 L1
# L1 L2 L0 L3 L2 L1 L4
# L5 L4 L0 L3 L4 L5 L2
# rule = [i for i in filter(None, rule_input.split(' '))]

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

size = 0.5
hex_size = 0.5
N = int(dis_height // size)
M = int(dis_width // size)

dis = pygame.display.set_mode((dis_width + 400, dis_height))
pygame.display.set_caption('AntGame')

clock = pygame.time.Clock()

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


hexagonal_b = bt.Button(cl.blue, dis.get_width() - 350, 100, 200, 50, "Hexagonal")
square_b = bt.Button(cl.red, dis.get_width() - 350, 200, 150, 50, "Square")
tick_b = bt.Button(cl.red, dis.get_width() - 350, 300, 150, 50, "Tick")
steps_per_tick_b = bt.Button(cl.red, dis.get_width() - 350, 400, 300, 50, "Steps per tick")
input_box_square_rule = bt.InputBox(square_b.x, square_b.y + 60, 200, 32, "RL")
input_box_hexagonal_rule = bt.InputBox(hexagonal_b.x, hexagonal_b.y + 60, 200, 32, "55544")
input_box_tick = bt.InputBox(tick_b.x, tick_b.y + 60, 200, 32, "0")
input_box_steps_per_tick = bt.InputBox(steps_per_tick_b.x, steps_per_tick_b.y + 60, 200, 32, "10000")
input_boxes = [input_box_square_rule, input_box_hexagonal_rule, input_box_tick, input_box_steps_per_tick]







def squareGameLoop():
    global square_rule, square_rule_length, tick, steps_per_tick
    tick = int(input_box_tick.text)
    steps_per_tick = int(input_box_steps_per_tick.text)
    square_rule = input_box_square_rule.text
    square_rule_length = len(square_rule)
    pygame.draw.rect(dis, cl.black, [0, 0, dis.get_width() - 400, dis.get_height()])
    game_over = False
    N = int(dis_height // size)
    M = int(dis_width // size)
    field = []
    global square_colours
    square_colours = []
    for x in range(square_rule_length):
        square_colours.append(cl.standard_colours[random.randint(0, len(cl.standard_colours) - 1)])
    for i in range(N):
        row = []
        for j in range(M):
            row.append(Cell())
            row[-1].x = i
            row[-1].y = j
        field += [row]
    ant = ants.SquareAnt()
    ant.rule = square_rule
    ant.i, ant.j = int(dis_height / (2 * size)), int(dis_width / (2 * size))
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if hexagonal_b.isOver(event.pos):
                    hexGameLoop()
                if square_b.isOver(event.pos) or tick_b.isOver(event.pos) or steps_per_tick_b.isOver(event.pos):
                    squareGameLoop()
            for box in input_boxes:
                box.handle_event(event)
        for box in input_boxes:
            box.update()
        for box in input_boxes:
            box.draw(dis)
        for i in range(steps_per_tick):
            ant.MakeMove(field)
            ant.FixCoords(N, M)
        pygame.display.update()
        clock.tick(tick)
    pygame.quit()
    quit()
# gameLoop()

def hexGameLoop():
    global hexagonal_rule, hexagonal_rule_length
    hexagonal_rule = input_box_hexagonal_rule.text
    hexagonal_rule_length = len(hexagonal_rule)
    pygame.draw.rect(dis, cl.black, [0, 0, dis.get_width() - 400, dis.get_height()])
    speed = 1000
    game_over = False
    N = int(dis_height // (hex_size * 1.5))
    M = int(dis_width // (hex_size * 3 ** (1/2)))
    field = []
    global hexagonal_colours
    hexagonal_colours = []
    for x in range(hexagonal_rule_length):
        hexagonal_colours.append(cl.standard_colours[random.randint(0, len(cl.standard_colours) - 1)])
    for i in range(N):
        row = []
        for j in range(M):
            row.append(HexCell())
            row[-1].x = (j * 3 ** (1/2)) * hex_size
            row[-1].y = i * (1.5) * hex_size
            if (i % 2 == 0):
                row[-1].x -= (3 ** (1/2) / 2) * hex_size
        field += [row]
    ant = ants.HexAnt()
    ant.rule = hexagonal_rule
    ant.i = N // 2
    ant.j = M // 2
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if hexagonal_b.isOver(event.pos):
                    hexGameLoop()
                if square_b.isOver(event.pos):
                    squareGameLoop()
            for box in input_boxes:
                box.handle_event(event)
        for box in input_boxes:
            box.update()

        for box in input_boxes:
            box.draw(dis)
        pygame.display.update()
        steps_per_tick = 10000
        for i in range(steps_per_tick):
            ant.MakeHexMove(field)
            ant.FixCoords(N, M)
        pygame.display.update()
        #clock.tick(speed)
    pygame.quit()
    quit()

def GameLoop():
    game_over = False
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if hexagonal_b.isOver(event.pos):
                    hexGameLoop()
                if square_b.isOver(event.pos):
                    squareGameLoop()
        pygame.display.update()
        #clock.tick(speed)
        hexagonal_b.Draw(dis)
        square_b.Draw(dis)
        tick_b.Draw(dis)
        steps_per_tick_b.Draw(dis)
    pygame.quit()
    quit()

GameLoop()


