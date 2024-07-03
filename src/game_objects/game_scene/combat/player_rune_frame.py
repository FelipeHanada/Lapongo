from .rune_frame import RuneFrame
from .rune.rune_factory import RuneFactory


class PlayerRuneFrame(RuneFrame):
    sprite_file_path = 'src/assets/sprites/game_scene/rune_frame.png'

    def __init__(self, parent, rune_inventory_user, *args, **kwargs):
        super().__init__(parent, self.sprite_file_path, rune_inventory_user, *args, **kwargs)
        self.set_rect(self.get_rect().move(64, 8))

        self.get_rune_slots()[0].set_item(RuneFactory.create_random_rune(1))
        self.get_rune_slots()[1].set_item(RuneFactory.create_random_rune(2))
        self.get_rune_slots()[2].set_item(RuneFactory.create_random_rune(3))
