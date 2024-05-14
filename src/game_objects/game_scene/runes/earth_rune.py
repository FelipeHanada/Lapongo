from pgframework import *
from .rune import Rune


class EarthRune(Rune):
    _sprite_file_path = 'src/assets/sprites/game_scene/runes/earth_rune.png'

    def __init__(self, *args, **kwargs):
        super().__init__(self._sprite_file_path, *args, **kwargs)
