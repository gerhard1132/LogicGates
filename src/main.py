"""Main execution of the Editor"""

import pygame as pg
import sys

from components.layers import Layer, UsageLayer
from components.components import Menu, Pipe, Button
from components.gates import Box, AND_GATE, OR_GATE
from components.nodes import IoNode, IoInput, IoOutput
from components.utils import _check_mouse_state


# Create screen
pg.init()
screen = pg.display.set_mode((900, 500))
pg.display.set_caption("LogicGates")

# All inits
SL = Layer(screen)
BL = Layer(screen)
UL = UsageLayer(screen)

menu = SL.add(Menu(screen, 200))
bSave = UL.add(Button(screen=screen, action=lambda: print("clicked"), width=100, height=40, pos=(50, 450), text="Save"))
bAnd_gate = UL.add(Button(screen=screen, action=lambda: UL.add(AND_GATE(screen)), pos=(15,20), text="AND-Gate"))
bOr_gate = UL.add(Button(screen=screen, action=lambda: UL.add(OR_GATE(screen)), pos=(15,110), text="OR-Gate"))

input1 = UL.add(IoInput(screen, state=False, pos=(250,200), text="In1"))
input2 = UL.add(IoInput(screen, state=True, pos=(250,300), text="In2"))
out1 = UL.add(IoOutput(screen, state=False, pos=(800,250), text="Out1"))


# Main loop
clock = pg.time.Clock()

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        
        _check_mouse_state(UL.layer_elements)
        [elem._handle_event(event) for elem in UL.layer_elements]
        UL._element_clicked(event, )

    # Draw static shapes
    screen.fill((30, 30, 30))
    
    SL.render_layer()
    BL.render_layer()
    UL.render_layer()
    
    pg.display.flip()
    clock.tick(60)
