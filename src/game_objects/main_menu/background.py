from pgframework import *


class MainMenuBackground(GameObject):
    _sprite_file_path = 'src/assets/sprites/main_menu/background.png'
    _sprite_sheet = components.sprite2d.SpriteSheetGrid(_sprite_file_path, 2, 2, 480, 270)
    _flipbook = _sprite_sheet.get_flip_book_from_pack(4, True)
    _flipbook_timed = components.sprite2d.FlipBookTimed.get_from_flip_book(_flipbook, 0.4)

    def __init__(self, *args, **kwargs):
        GameObject.__init__(self, *args, **kwargs, rect=PygameRectAdapter(0, 0, 480, 270))

        self.add_child(components.sprite2d.Sprite2DAnimated(self, self._flipbook_timed))
