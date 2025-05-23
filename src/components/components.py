"""Basic components for building the editor"""

import pygame as pg

from .gates import Box

class Menu:
    def __init__(self, screen, width):
        self.screen = screen
        self.width = width
    
    def _draw(self):
        pg.draw.line(self.screen, "white", (self.width, 0), (self.width, self.screen.get_height()))
     

class Pipe:
    def __init__(self, ob1, ob2, color="green", line_width=3):
        self.ob1 = ob1
        self.ob2 = ob2
        self.color = color
        self.line_width = line_width
        
    def _draw(self, screen):
        pg.draw.line(screen, self.color,self.ob1.position, self.ob2.position)


class Button(Box):
    def __init__(self, screen=..., width=160, height=80, pos=(0,0), text="Hi", c="white", line_width=1, action=None):
        super().__init__(screen, width, height, pos, text, c, line_width)
        self.action = action
    
    def _handle_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            if self._is_hovered(event.pos):
                self.action()