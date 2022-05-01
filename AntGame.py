import pygame
import time
import random
import colours as cl
import buttons as bt
import ants
import GlobalVariables as gv
import main
import SquareGameLoop as sgl
import HexGameLoop as hgl
pygame.init()

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
	main.main()
