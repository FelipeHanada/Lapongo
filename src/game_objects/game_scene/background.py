import pgframework as pgf


class GameSceneBackground(pgf.GameObject):
    _sprite_file_path = 'src/assets/sprites/game_scene/background.png'
    _sprite_sheet = pgf.components.sprite2d.SpriteSheetGrid(_sprite_file_path, 2, 2, 480, 270)
    _flipbook = _sprite_sheet.get_flip_book_from_pack(4, True)
    _flipbook_timed = pgf.components.sprite2d.FlipBookTimed.get_from_flip_book(_flipbook, 0.4)

    def __init__(self, *args, **kwargs):
        pgf.GameObject.__init__(self, *args, **kwargs, rect=pgf.PygameRectAdapter(0, 0, 480, 270))

        self.add_component(pgf.components.sprite2d.Sprite2DAnimated(self, self._flipbook_timed))
