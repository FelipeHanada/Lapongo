from ..rune import Rune
from ..rune_effects.activation_rune_effects.cause_damage_rune_effect import CauseDamageOnActivation


class WaterRune(Rune):
    _sprite_file_path = 'src/assets/sprites/game_scene/runes/water_rune.png'

    def __init__(self, *args, **kwargs):
        super().__init__(self._sprite_file_path, 'Runa de Agua I', 'descricao.', 10, 10, CauseDamageOnActivation(5), *args, **kwargs)
