
import pygame as pg

from .nodes import IoNode
from .layers import UsageLayer


class Box(UsageLayer):
    def __init__(self, screen, width=160, height=80, pos=None, text="Hi", c="white", line_width= 1):
        super().__init__(screen)
        self.screen = screen
        self.width = width
        self.height = height
        self.position = pos if pos else (screen.get_width()/2, screen.get_height()/2)
        self.text = text
        self.color = c
        self.line_width = line_width
        self.dragging = False

        
    def _draw(self):
        pg.draw.line(self.screen, self.color, (self.position[0], self.position[1]), (self.position[0]+self.width, self.position[1]), width=self.line_width) # Top line
        pg.draw.line(self.screen, self.color, (self.position[0], self.position[1]+self.height), (self.position[0]+self.width, self.position[1]+self.height), width=self.line_width) # bottom line
        pg.draw.line(self.screen, self.color, (self.position[0], self.position[1]), (self.position[0], self.position[1]+self.height), width=self.line_width) # Left line
        pg.draw.line(self.screen, self.color, (self.position[0]+self.width, self.position[1]), (self.position[0]+self.width, self.position[1]+self.height), width=self.line_width) # Left line
        
        # Text
        font = pg.font.SysFont(None, 24)
        text_surf = font.render(self.text, True, self.color)
        text_rect = text_surf.get_rect(center=(
            self.position[0] + self.width / 2,
            self.position[1] + self.height/ 2
        ))
        self.screen.blit(text_surf, text_rect)
        

    def is_hovered(self, mouse_pos):
        x, y = self.position
        return x <= mouse_pos[0] <= x + self.width and y <= mouse_pos[1] <= y + self.height
    
    def _handle_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            if self.is_hovered(event.pos):
                self.dragging = True
                self.offset = (self.position[0] - event.pos[0], self.position[1] - event.pos[1])
        elif event.type == pg.MOUSEBUTTONUP:
            self.dragging = False
        elif event.type == pg.MOUSEMOTION and self.dragging:
            self.position = [event.pos[0] + self.offset[0], event.pos[1] + self.offset[1]]


class AND_GATE(Box):
    def __init__(self, screen, width=160, height=80, pos=None, text="AND-Gate", c="white", line_width=1):
        super().__init__(screen, width, height, pos, text, c, line_width)
        self.position = pos if pos else (screen.get_width()/2, screen.get_height()/2)
        self.nodes = [
            IoNode(self.screen, offset=(0, self.height*.3)),
            IoNode(self.screen, offset=(0, self.height*.6)),
            IoNode(self.screen, offset=(self.width, self.height/2))
            ]
        self.output = False
        
    def _draw(self):
        super()._draw()
        for input_node in self.nodes:
            input_node._draw(to_pos=(self.position))


class OR_GATE(Box):
    def __init__(self, screen, width=160, height=80, pos=None, text="OR-GATE", c="white", line_width=1):
        super().__init__(screen, width, height, pos, text, c, line_width)
        self.position = pos if pos else (screen.get_width()/2, screen.get_height()/2)
        self.nodes = [
            IoNode(self.screen, offset=(0, self.height*.3)),
            IoNode(self.screen, offset=(0, self.height*.6)),
            IoNode(self.screen, offset=(self.width, self.height/2))
            ]
        self.output = False
        
    def _draw(self):
        super()._draw()
        for input_node in self.nodes:
            input_node._draw(to_pos=(self.position))