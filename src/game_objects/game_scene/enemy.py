from pgframework import *


class GameSceneEnemy(AbstractGameObject):
    _sprite_file_paths = {
        'frog': 'src/assets/sprites/characters/frog/frog_idle.png',
    }

    def __init__(self, *args, **kwargs):
        AbstractGameObject.__init__(self, *args, **kwargs, rect=pygame.Rect(336, 180, 32, 32))

        self.add_component(Sprite2DAnimated(self, self.get_idle_timed_flipbook('frog')))

    def get_idle_timed_flipbook(self, enemy_type):
        _sprite_sheet = SpriteSheetGrid(self._sprite_file_paths[enemy_type], 2, 2, 32, 32)
        _flipbook = _sprite_sheet.get_flip_book_from_pack(4, True)
        return FlipBookTimed.get_from_flip_book(_flipbook, 0.4)
