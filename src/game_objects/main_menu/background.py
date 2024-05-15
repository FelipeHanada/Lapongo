from pgframework import *


class MainMenuBackground(AbstractGameObject):
    _sprite_file_path = 'src/assets/sprites/main_menu/background.png'
    _sprite_sheet = SpriteSheetGrid(_sprite_file_path, 2, 2, 480, 270)
    _flipbook = _sprite_sheet.get_flip_book_from_pack(4, True)
    _flipbook_timed = FlipBookTimed.get_from_flip_book(_flipbook, 0.4)

    def __init__(self, *args, **kwargs):
        AbstractGameObject.__init__(self, *args, **kwargs, rect=PygameRectAdapter(0, 0, 480, 270))

        self.add_component(Sprite2DAnimated(self, self._flipbook_timed))
