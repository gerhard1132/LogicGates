"""Basic components for building the editor"""

import pygame as pg

class Menu:
    def __init__(self, width):
        self.width = width
    
    def _draw(self, screen: pg.Surface):
        pg.draw.line(screen, "white", (self.width, 0), (self.width, screen.get_height()))
     

class Pipe:
    def __init__(self, ob1, ob2, color="green", line_width=3):
        self.ob1 = ob1
        self.ob2 = ob2
        self.color = color
        self.line_width = line_width
        
    def _draw(self, screen):
        pg.draw.line(screen, self.color,self.ob1.position, self.ob2.position)