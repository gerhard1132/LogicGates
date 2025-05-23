import pygame as pg
import sys

from components.components import Menu, Pipe, Button
from components.gates import Box, AND_GATE, OR_GATE
from components.nodes import IoNode, IoInput, IoOutput
from components.utils import _check_mouse_state


# Create screen
pg.init()
screen = pg.display.set_mode((900, 500))
pg.display.set_caption("LogicGates")

# All inits
menu = Menu(screen, 200)
bSave = Button(screen=screen, action=lambda: print("clikced"), width=100, height=40, pos=(50, 450), text="Save")
bAnd_gate = Button(screen=screen, action=lambda: usage_layer.append(AND_GATE(screen)), pos=(15,20), text="AND-Gate")
bOr_gate = Button(screen=screen, action=lambda: usage_layer.append(OR_GATE(screen)), pos=(15,110), text="OR-Gate")

# and_gate1 = AND_GATE(screen=screen, pos=(15,15))
input1 = IoInput(screen, state=False, pos=(300,200), text="In1")
input2 = IoInput(screen, state=True, pos=(300,300), text="In2")
out1 = IoOutput(screen, state=False, pos=(800,250), text="Out1")

static_layer = [menu]
background_layer = []
usage_layer = [input1, input2, out1, bAnd_gate, bOr_gate, bSave]


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
    [elem._draw() for elem in static_layer]
    [elem._draw() for elem in background_layer]
    [elem._draw() for elem in usage_layer]
    
    pg.display.flip()
    clock.tick(60)
