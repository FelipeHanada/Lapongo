from pgframework import *


class GameScenePlayer(AbstractGameObject):
    _sprite_file_path = 'src/assets/sprites/characters/calango/calango_idle.png'
    _sprite_sheet = SpriteSheetGrid(_sprite_file_path, 2, 2, 32, 32)
    _flipbook = _sprite_sheet.get_flip_book_from_pack(4, True)
    _flipbook_timed = FlipBookTimed.get_from_flip_book(_flipbook, 0.4)

    def __init__(self, *args, **kwargs):
        AbstractGameObject.__init__(self, *args, **kwargs, rect=PygameRectAdapter(112, 180, 32, 32))

        self.add_component(Sprite2DAnimated(self, self._flipbook_timed))
