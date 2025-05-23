
import pygame as pg


class IoNode:
    def __init__(self, pos=(0, 0), radius=10, state=False, text=""):
        self.radius = radius
        self.position = list(pos)
        self.state = state
        self.text = text

    def _draw(self, screen):
        pg.draw.circle(screen, pg.Color("red") if self.state else pg.Color("grey"), self.position, self.radius)
        font = pg.font.SysFont(None, 24)
        text_surf = font.render(self.text, True, self.state)
        text_rect = text_surf.get_rect(center=(
            self.position[0],
            self.position[1] + self.radius * 2
        ))
        screen.blit(text_surf, text_rect)

    def _is_hovered(self, mouse_pos):
        dx = mouse_pos[0] - self.position[0]
        dy = mouse_pos[1] - self.position[1]
        return dx * dx + dy * dy <= self.radius * self.radius

    def _handle_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            if self._is_hovered(event.pos):
                self.state = not(self.state)


class IoInput(IoNode):
    def __init__(self, pos=(0, 0), radius=10, state=False, text=""):
        super().__init__(pos, radius, state, text)
        

class IoOutput(IoNode):
    def __init__(self, pos=(0, 0), radius=10, state=False, text=""):
        super().__init__(pos, radius, state, text)