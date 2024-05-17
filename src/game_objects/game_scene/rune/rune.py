import pgframework as pgf
from .rune_effects.rune_effect import RuneEffect


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
        print('hover')
        self._description_frame.set_visible(True)

    def on_mouse_unhover(self):
        self._description_frame.set_visible(False)

class RuneDescriptionFrame(pgf.GameObject):
    _sprite_file_path = 'src/assets/sprites/game_scene/rune_description_frame.png'
    
    def __init__(self, rune: Rune, *args, **kwargs):
        super().__init__(*args, **kwargs, rect=pgf.PygameRectAdapter(0, 0, 100, 100))

        self._rune = rune
        self.add_child(pgf.components.sprite2d.Sprite2D(self, self._sprite_file_path))

