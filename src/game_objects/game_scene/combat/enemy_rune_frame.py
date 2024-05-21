from .rune_frame import RuneFrame


class EnemyRuneFrame(RuneFrame):
    sprite_file_path='src/assets/sprites/characters/frog/frog_rune_frame.png'

    def __init__(self, parent, rune_inventory_user, *args, **kwargs):
        super().__init__(parent, self.sprite_file_path, rune_inventory_user, *args, **kwargs)
        self.set_rect(self.get_rect().move(288, 8))
        self.set_locked(True)
