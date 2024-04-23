from pgframework import *


class MainMenuBackground(AbstractGameObject):
    def __init__(self, game: Game, priority: int = 0):
        AbstractGameObject.__init__(self, game, priority=priority)

sprite_file_path = 'src/main_menu/assets/sprites/background.png'
sprite_sheet = SpriteSheetGrid(sprite_file_path, 2, 2, 480, 270)
flipbook = sprite_sheet.get_flip_book_from_pack(4, True)
flipbook_timed = FlipBookTimed.get_from_flip_book(flipbook, 0.4)
MainMenuBackground.add_component_factory(Sprite2DAnimated.get_default_factory(flipbook_timed))