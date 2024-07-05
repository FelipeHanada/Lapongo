from .rune_frame import RuneFrame
from .rune.rune_factory import RuneFactory
import pgframework as pgf
import random


class EnemyRuneFrame(RuneFrame):
    _sprite_file_paths = {
        'frog': 'src/assets/sprites/characters/frog/frog_rune_frame.png',
        'turtle': 'src/assets/sprites/characters/turtle/turtle_rune_frame.png',
    }

    def __init__(self, parent, rune_inventory_user, *args, **kwargs):
        super().__init__(parent, self._sprite_file_paths['frog'], rune_inventory_user, *args, **kwargs)
        self.set_rect(self.get_rect().move(288, 8))
        self.set_locked(True)

    def set_enemy_type(self, enemy_type):
        image = pgf.PygameSurfaceAdapter.from_image(self._sprite_file_paths[enemy_type])
        self.get_sprite2d().set_image(image)

    def on_combat_start(self):
        for slot in self.get_rune_slots():
            slot.remove_item()

        slots = list(range(9))
        random.shuffle(slots)

        for i, slot in enumerate(self.get_rune_slots()[:3]):
            slot.set_item(RuneFactory.create_random_rune(1))
