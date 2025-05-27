
import pygame as pg

from .layers import UsageLayer


class IoNode(UsageLayer):
    def __init__(self, screen, pos=(0, 0), radius=10, state=False, text="", offset=(0,0)):
        super().__init__(screen)
        self.screen = screen
        self.radius = radius
        self.position = pos
        self.state = state
        self.text = text
        self.offset = offset


    def _draw(self, to_pos=None):
        if to_pos is None:
            to_pos = self.position
        pg.draw.circle(self.screen, pg.Color("red") if self.state else pg.Color("grey"), (to_pos[0]+self.offset[0], to_pos[1]+self.offset[1]), self.radius)
        font = pg.font.SysFont(None, 24)
        text_surf = font.render(self.text, True, pg.Color("white"))
        text_rect = text_surf.get_rect(center=(
           to_pos[0],
           to_pos[1] + self.radius * 2
        ))
        self.screen.blit(text_surf, text_rect)

    def is_hovered(self, mouse_pos):
        dx = mouse_pos[0] - self.position[0]
        dy = mouse_pos[1] - self.position[1]
        return dx * dx + dy * dy <= self.radius * self.radius

    def _handle_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            if self.is_hovered(event.pos):
                self.state = not(self.state)


class IoInput(IoNode):
    def __init__(self, screen, pos=(0, 0), radius=10, state=False, text="", offset=(0, 0)):
        super().__init__(screen, pos, radius, state, text, offset)
        
    
class IoOutput(IoNode):
    def __init__(self, screen, pos=(0, 0), radius=10, state=False, text="", offset=(0, 0)):
        super().__init__(screen, pos, radius, state, text, offset)
    
    def _handle_event(self, event):
        return 