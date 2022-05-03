import pygame
import time
import random
import colours as cl
import buttons as bt
import ants
import GlobalVariables as gv
import loop
import SquareGameLoop as sgl
import HexGameLoop as hgl
pygame.init()

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

class HexCell():
    x, y = 0, 0
    colour = 0
    def Draw(self, gl):
        pygame.draw.polygon(gl.dis, gl.hexagonal_colours[self.colour],
                            [[self.x, self.y], [self.x + 3**(1/2) / 2 * gl.hex_size, self.y - 0.5 * gl.hex_size],
                            [self.x + 3**(1/2) * gl.hex_size, self.y], [self.x + 3**(1/2) * gl.size, self.y + gl.hex_size],
                            [self.x + 3**(1/2) / 2 * gl.hex_size, self.y + 1.5 * gl.hex_size], [self.x, self.y + gl.hex_size]])


class Cell:
    x, y = 0, 0
    colour = 0

    def Draw(self, gl):
        pygame.draw.rect(gl.dis, gl.square_colours[self.colour], [self.x * gl.size, self.y * gl.size, gl.size, gl.size])

def DrawInterface(gl, ic):
    ic.hexagonal_b.Draw(gl.dis)
    ic.square_b.Draw(gl.dis)
    ic.tick_b.Draw(gl.dis)
    ic.steps_per_tick_b.Draw(gl.dis)
    ic.cell_size_b.Draw(gl.dis)

def Draw(gl, ic):
    for box in ic.input_boxes:
        box.update()
    for box in ic.input_boxes:
        box.draw(gl.dis)


# gameLoop()

if __name__ == "__main__":
	loop.main()


