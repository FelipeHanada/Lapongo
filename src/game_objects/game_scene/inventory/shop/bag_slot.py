from pgframework import *
from ..rune_slot import RuneSlot


class BagSlot(RuneSlot):
    _sprite_file_path = 'src/assets/sprites/game_scene/shop/bag_slot.png'

    def __init__(self, *args, **kwargs):
        RuneSlot.__init__(self, *args, **kwargs)

        self.add_component(Sprite2D(self, self._sprite_file_path, offset=(-2, -2)))
