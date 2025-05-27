
import pygame as pg


def _check_mouse_state(clickable):
    if any(elem.is_hovered(pg.mouse.get_pos()) for elem in clickable):
        pg.mouse.set_cursor(pg.SYSTEM_CURSOR_HAND)
    else:
        pg.mouse.set_cursor(pg.SYSTEM_CURSOR_ARROW)