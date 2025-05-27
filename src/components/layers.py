
import pygame as pg


class Layer:
    def __init__(self, screen):
        self.layer_elements = []
        self.screen = screen
        self.clicked_elems = []

    def add(self, obj):
        self.layer_elements.append(obj)
    
    def remove(self, obj):
        assert obj in self.layer_elements
        self.layer_elements.remove(obj)

    def render_layer(self):
        for elem in self.layer_elements:
            elem._draw()
    
    def _layer_element_clicked(self):
        from .nodes import IoNode
        for obj in self.layer_elements:
            if obj.is_hovered(pg.mouse.get_pos()) and issubclass(type(obj), IoNode):
                return obj
    
    def _pipe_elements(self, obj1, obj2):
        from .components import Pipe
        new_pipe = Pipe(self.screen, obj1, obj2)
        self.add(new_pipe)

class UsageLayer(Layer):
    def __init__(self, screen):
        super().__init__(screen)

    def _element_clicked(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            print(self.clicked_elems)
            if self._layer_element_clicked():
                self.clicked_elems.insert(0, self._layer_element_clicked())
            if len(self.clicked_elems) >= 2:
                obj1 = self.clicked_elems[1]
                obj2 = self.clicked_elems[0]
                from .components import Pipe
                from .nodes import IoNode

                if obj1 == obj2 and isinstance(obj1, Pipe):
                    self.remove(obj1)
                elif obj1 != obj2 and issubclass(type(obj1), IoNode) and issubclass(type(obj2), IoNode):
                    self._pipe_elements(obj1, obj2)
                self.clicked_elems = []