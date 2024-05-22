import pgframework as pgf
from .combat_agent import CombatAgent
from .rune_frame import RuneFrame


class Enemy(CombatAgent):
    _sprite_file_paths = {
        'frog': 'src/assets/sprites/characters/frog/frog_idle.png',
    }

    def __init__(self, parent: pgf.GameObject, rune_frame: RuneFrame, *args, **kwargs):
        super().__init__(parent, rune_frame, *args, **kwargs, rect=pgf.PygameRectAdapter(336, 180, 32, 32))

        self.add_child(pgf.components.sprite2d.Sprite2DAnimated(self, self.get_idle_timed_flipbook('frog')))

    def get_idle_timed_flipbook(self, enemy_type):
        _sprite_sheet = pgf.components.sprite2d.SpriteSheetGrid(self._sprite_file_paths[enemy_type], 2, 2, 32, 32)
        _flipbook = _sprite_sheet.get_flip_book_from_pack(4, True)
        return pgf.components.sprite2d.FlipBookTimed.get_from_flip_book(_flipbook, 0.4)
