from ..rune import Rune


class FireRune(Rune):
    _sprite_file_path = 'src/assets/sprites/game_scene/runes/fire_rune.png'

    def __init__(self, *args, **kwargs):
        super().__init__(self._sprite_file_path, *args, **kwargs)
