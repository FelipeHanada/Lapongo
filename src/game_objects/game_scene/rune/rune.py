import pgframework as pgf
from .rune_effects.rune_effect import RuneEffect
from ..inventory.rune_slot import RuneSlot


class Rune(pgf.GameObject):
    def __init__(self, sprite_file, *args, **kwargs):
        super().__init__(*args, **kwargs, rect=pgf.PygameRectAdapter(0, 0, 16, 16))

        #self._activation_effect = activation_effect

        self.add_child(pgf.components.sprite2d.Sprite2D(self, sprite_file))

        self._description_frame = self.add_child(RuneDescriptionFrame(self, self, visible=False))

        self._mouse_listener: pgf.components.mouse_listener.MouseListener = self.add_child(pgf.components.mouse_listener.MouseListener(self))
        self._mouse_listener.on_hover(self.on_mouse_hover)
        self._mouse_listener.on_unhover(self.on_mouse_unhover)

    def on_mouse_hover(self):
        if isinstance(self.get_parent(), RuneSlot):
            self._description_frame.set_visible(True)
        else:
            self._description_frame.set_visible(False)

    def on_mouse_unhover(self):
        self._description_frame.set_visible(False)

class RuneDescriptionFrame(pgf.GameObject):
    _sprite_file_path = 'src/assets/sprites/game_scene/rune_description_frame.png'
    
    def __init__(self, rune: Rune, *args, **kwargs):
        super().__init__(*args, **kwargs, rect=pgf.PygameRectAdapter(0, 0, 96, 72))

        self._rune = rune
        self._sprite2d = self.add_child(pgf.components.sprite2d.Sprite2D(self, self._sprite_file_path, draw_absolute=True))

    def draw_callback(self, renderer: pgf.Renderer) -> None:
        rune_absolute_rect = self._rune.get_absolute_rect()
        absolute_rect = self.get_absolute_rect().copy()
        render_size = renderer.get_render_size()
        
        if rune_absolute_rect.get_centerx() >= render_size[0] / 2:
            absolute_rect.set_right(rune_absolute_rect.get_left())
        else:
            absolute_rect.set_left(rune_absolute_rect.get_right())

        absolute_rect.set_y((render_size[1] - absolute_rect.get_height()) / (render_size[1] - rune_absolute_rect.get_height()) * rune_absolute_rect.get_y())

        self.set_absolute_rect(absolute_rect)
