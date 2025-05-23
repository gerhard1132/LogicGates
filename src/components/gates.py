
import pygame as pg

from .nodes import IoNode


class Box:
    def __init__(self, width=160, height=80, pos=(0,0), text="Hi", c="white", line_width= 1):
        self.width = width
        self.height = height
        self.position = pos
        self.text = text
        self.color = c
        self.line_width = line_width
        self.dragging = False

        
    def _draw(self, screen: pg.Surface):
        pg.draw.line(screen, self.color, (self.position[0], self.position[1]), (self.position[0]+self.width, self.position[1]), width=self.line_width) # Top line
        pg.draw.line(screen, self.color, (self.position[0], self.position[1]+self.height), (self.position[0]+self.width, self.position[1]+self.height), width=self.line_width) # bottom line
        pg.draw.line(screen, self.color, (self.position[0], self.position[1]), (self.position[0], self.position[1]+self.height), width=self.line_width) # Left line
        pg.draw.line(screen, self.color, (self.position[0]+self.width, self.position[1]), (self.position[0]+self.width, self.position[1]+self.height), width=self.line_width) # Left line
        
        # Text
        font = pg.font.SysFont(None, 24)
        text_surf = font.render(self.text, True, self.color)
        text_rect = text_surf.get_rect(center=(
            self.position[0] + self.width / 2,
            self.position[1] + self.height/ 2
        ))
        screen.blit(text_surf, text_rect)
        

    def _is_hovered(self, mouse_pos):
        x, y = self.position
        return x <= mouse_pos[0] <= x + self.width and y <= mouse_pos[1] <= y + self.height
    
    def _handle_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            if self._is_hovered(event.pos):
                self.dragging = True
                self.offset = (self.position[0] - event.pos[0], self.position[1] - event.pos[1])
        elif event.type == pg.MOUSEBUTTONUP:
            self.dragging = False
        elif event.type == pg.MOUSEMOTION and self.dragging:
            self.position = [event.pos[0] + self.offset[0], event.pos[1] + self.offset[1]]


class AND_GATE(Box):
    def __init__(self, width=160, height=80, pos=(0, 0), text="AND", c="white", line_width=1):
        super().__init__(width, height, pos, text, c, line_width)
        self.inputs = [
            IoNode(pos=(self.position[0],self.position[1]-self.height * .3)),
            IoNode(pos=(self.position[0],self.position[1]-self.height * .6))
            ]
        self.output = False
        
    def _draw(self, screen):
        for input_node in self.inputs:
            input_node._draw(screen)
        super()._draw(screen)
    
    def _is_hovered(self, mouse_pos):
        return super()._is_hovered(mouse_pos)