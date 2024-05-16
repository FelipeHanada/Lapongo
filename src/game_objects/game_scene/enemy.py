import pgframework as pgf


class GameSceneEnemy(pgf.GameObject):
    _sprite_file_paths = {
        'frog': 'src/assets/sprites/characters/frog/frog_idle.png',
    }

    def __init__(self, *args, **kwargs):
        pgf.GameObject.__init__(self, *args, **kwargs, rect=pgf.PygameRectAdapter(336, 180, 32, 32))

        self.add_component(pgf.components.sprite2d.Sprite2DAnimated(self, self.get_idle_timed_flipbook('frog')))

    def get_idle_timed_flipbook(self, enemy_type):
        _sprite_sheet = pgf.components.sprite2d.SpriteSheetGrid(self._sprite_file_paths[enemy_type], 2, 2, 32, 32)
        _flipbook = _sprite_sheet.get_flip_book_from_pack(4, True)
        return pgf.components.sprite2d.FlipBookTimed.get_from_flip_book(_flipbook, 0.4)
