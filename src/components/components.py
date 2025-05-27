"""Basic components for building the editor"""

import pygame as pg

from .gates import Box
from .layers import UsageLayer

class Menu:
    def __init__(self, screen, width):
        self.screen = screen
        self.width = width
    
    def _draw(self):
        pg.draw.line(self.screen, "white", (self.width, 0), (self.width, self.screen.get_height()))


class Pipe(UsageLayer):
    def __init__(self, screen, obj1, obj2, color="green", line_width=8):
        super().__init__(screen)
        self.obj1 = obj1
        self.obj2 = obj2
        self.color = color
        self.line_width = line_width
        
    def _draw(self):
        pg.draw.line(self.screen, self.color,self.obj1.position, self.obj2.position)
    
    def is_hovered(self, mouse_pos):
        start = self.obj1.position
        end = self.obj2.position
        direction = (end[0]-start[0], end[1]-start[1])
        print(start,end,direction)
        
    def _handle_event(self, event):
        pass


class Button(Box):
    def __init__(self, screen, width=160, height=80, pos=..., text="Hi", c="white", line_width=1, action=None):
        super().__init__(screen, width, height, pos, text, c, line_width)
        self.action = action
    
    def _handle_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            if self.is_hovered(event.pos):
                self.action()