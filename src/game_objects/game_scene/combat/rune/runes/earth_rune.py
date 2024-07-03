from ..rune import Rune
from ..rune_effects.rune_effect import RuneEffect


class EarthRune(Rune):
    _sprite_file_path = 'src/assets/sprites/game_scene/runes/earth_rune.png'

    def __init__(self, level: int, cost: int, max_energy_bonus: int, activation_time: int, energy_cost: float, activation_effect: RuneEffect, *args, **kwargs):
        super().__init__(self._sprite_file_path, f'Runa de Terra {level}', 'isso e uma runa de terra.', cost, max_energy_bonus, activation_time, energy_cost, activation_effect, *args, **kwargs)
