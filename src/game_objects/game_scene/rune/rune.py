import pgframework as pgf
from .rune_effects.rune_effect import RuneEffect


class Rune(pgf.GameObject):
    def __init__(self, sprite_file: str, name: str, description: str, activation_effect: RuneEffect, *args, **kwargs):
        super().__init__(*args, **kwargs, rect=pgf.PygameRectAdapter(0, 0, 16, 16))

        self._activation_effect: RuneEffect = activation_effect
        #self._rune_induction_effect: RuneEffect = rune_induction_effect

        self._name = name
        self._description = description

        self.add_child(pgf.components.sprite2d.Sprite2D(self, sprite_file))

    def get_name(self):
        return self._name

    def get_description(self):
        description = f'<color rgb="(197, 152, 70)">Efeito de ativacao: </color>'
        description += f'{self._activation_effect.get_description()}<br>'

        return description
