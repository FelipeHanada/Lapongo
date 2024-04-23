from pgframework import *


sprite_file_path = 'src/main_menu/assets/sprites/title_sign.png'
sprite_size = (352, 180)

class MainMenuTitleSign(AbstractGameObject):
    def __init__(self, game: Game, priority: int = 0):
        rect = pygame.Rect(0, 0, *sprite_size)
        rect.centerx = game.get_display_handler().get_render_display_data().center[0]

        AbstractGameObject.__init__(self, game, priority=priority, rect=rect)

sprite_sheet = SpriteSheetGrid(sprite_file_path, 2, 2, *sprite_size)
flipbook = sprite_sheet.get_flip_book_from_pack(4, True)
flipbook_timed = FlipBookTimed.get_from_flip_book(flipbook, 0.4)
MainMenuTitleSign.add_component_factory(Sprite2DAnimated.get_default_factory(flipbook_timed))

