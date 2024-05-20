from ..rune import Rune
from ..rune_effects.rune_effect import RuneEffect
from ..rune_effects.cause_damage_effect import CauseDamageEffect


class WaterRune(Rune):
    _sprite_file_path = 'src/assets/sprites/game_scene/runes/water_rune.png'

    def __init__(self, *args, **kwargs):
        super().__init__(self._sprite_file_path, 'Runa de Agua I', 'descricao.', CauseDamageEffect(5), *args, **kwargs)
