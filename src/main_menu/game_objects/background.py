from pgframework import *


class MainMenuBackground(AbstractGameObject):
    _sprite_file_path = 'src/main_menu/assets/sprites/background.png'
    _sprite_sheet = SpriteSheetGrid(_sprite_file_path, 2, 2, 480, 270)
    _flipbook = _sprite_sheet.get_flip_book_from_pack(4, True)
    _flipbook_timed = FlipBookTimed.get_from_flip_book(_flipbook, 0.4)

    def __init__(self, parent: AbstractGameObject, scene: AbstractScene, priority: int = 0):
        AbstractGameObject.__init__(self, parent, scene, priority=priority)

        self.add_component(Sprite2DAnimated(self, self._flipbook_timed))
