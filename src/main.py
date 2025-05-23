import pygame as pg
import sys

from components.components import Menu, Pipe
from components.gates import Box, AND_GATE
from components.nodes import IoNode, IoInput, IoOutput
from components.utils import _check_mouse_state


# Create screen
pg.init()
screen = pg.display.set_mode((900, 500))
pg.display.set_caption("pg Layout Example")

# All inits
menu = Menu(200)
and_game1 = AND_GATE(pos=(15,15))
input1 = IoNode(state=False, pos=(300,200), text="In1")
input2 = IoNode(state=True, pos=(300,300), text="In2")
out1 = IoNode(state=False, pos=(800,250), text="Out1")

static_layer = [menu]
background_layer = []
usage_layer = [and_game1, input1, input2, out1]


# Main loop
clock = pg.time.Clock()

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        
        _check_mouse_state(usage_layer)
        [elem._handle_event(event) for elem in usage_layer]

    # Draw static shapes
    screen.fill((30, 30, 30))
    [elem._draw(screen) for elem in static_layer]
    [elem._draw(screen) for elem in background_layer]
    [elem._draw(screen) for elem in usage_layer]
    
    pg.display.flip()
    clock.tick(60)
