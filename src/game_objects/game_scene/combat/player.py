import pgframework as pgf
from .combat_agent import CombatAgent
from .rune_frame import RuneFrame


class GameScenePlayer(CombatAgent):
    _sprite_file_path = 'src/assets/sprites/characters/calango/calango_idle.png'
    _sprite_sheet = pgf.components.sprite2d.SpriteSheetGrid(_sprite_file_path, 2, 2, 32, 32)
    _flipbook = _sprite_sheet.get_flip_book_from_pack(4, True)
    _flipbook_timed = pgf.components.sprite2d.FlipBookTimed.get_from_flip_book(_flipbook, 0.4)

    def __init__(self, parent: pgf.GameObject, rune_frame: RuneFrame, *args, **kwargs):
        super().__init__(parent, rune_frame, *args, **kwargs, rect=pgf.PygameRectAdapter(112, 180, 32, 32))

        self._rune_frame = rune_frame

        self.add_child(pgf.components.sprite2d.Sprite2DAnimated(self, self._flipbook_timed))
