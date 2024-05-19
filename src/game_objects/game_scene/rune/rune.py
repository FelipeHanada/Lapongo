import pgframework as pgf
from .rune_effects.rune_effect import RuneEffect


class Rune(pgf.GameObject):
    def __init__(self, sprite_file: str, name: str, description: str, *args, **kwargs):
        super().__init__(*args, **kwargs, rect=pgf.PygameRectAdapter(0, 0, 16, 16))

        #self._activation_effect = activation_effect

        self._name = name
        self._description = description

        self.add_child(pgf.components.sprite2d.Sprite2D(self, sprite_file))

    def get_name(self):
        return self._name

    def get_description(self):
        return self._description
