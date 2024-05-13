from pgframework import *
from .slot import Slot

class GameSceneRuneFrame(AbstractGameObject):
    _sprite_file_path = 'src/assets/sprites/game_scene/rune_frame.png'

    def __init__(self, *args, **kwargs):
        AbstractGameObject.__init__(self, *args, **kwargs, rect=pygame.Rect(64, 8, 128, 128))

        self.add_component(Sprite2D(self, self._sprite_file_path))

        self._rune_slots = [
            Slot(self, rect=pygame.Rect(32, 16, 16, 16)),
            Slot(self, rect=pygame.Rect(80, 16, 16, 16)),
            Slot(self, rect=pygame.Rect(40, 40, 16, 16)),
            Slot(self, rect=pygame.Rect(72, 40, 16, 16)),
            Slot(self, rect=pygame.Rect(16, 56, 16, 16)),
            Slot(self, rect=pygame.Rect(56, 56, 16, 16)),
            Slot(self, rect=pygame.Rect(96, 56, 16, 16)),
            Slot(self, rect=pygame.Rect(56, 76, 16, 16)),
            Slot(self, rect=pygame.Rect(32, 96, 16, 16)),
            Slot(self, rect=pygame.Rect(80, 96, 16, 16)),
        ]

        from .runes.water_rune import WaterRune
        a = WaterRune()
        self._rune_slots[0].set_item(a)

        for slot in self._rune_slots:
            self.add_child_game_object(slot)
