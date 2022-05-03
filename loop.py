import pygame
import time
import random
import colours as cl
import buttons as bt
import ants
import GlobalVariables as gv
import SquareGameLoop as sgl
import AntGame as ag

def main():
    game_over = False
    gl = gv.Global()
    ic = gv.Interface()
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if ic.hexagonal_b.isOver(event.pos):
                    ag.hexGameLoop(gl, ic)
                if ic.square_b.isOver(event.pos):
                    sgl.squareGameLoop(gl, ic)
        pygame.display.update()
        ag.DrawInterface(gl, ic)
        sgl.squareGameLoop(gl, ic)
    pygame.quit()
    quit()