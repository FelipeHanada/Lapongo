from pgframework import *


class MainMenuTitleSign(AbstractGameObject):
    _sprite_file_path = 'src/main_menu/assets/sprites/title_sign.png'
    _sprite_size = (352, 180)
    _sprite_sheet = SpriteSheetGrid(_sprite_file_path, 2, 2, *_sprite_size)
    _flipbook = _sprite_sheet.get_flip_book_from_pack(4, True)
    _flipbook_timed = FlipBookTimed.get_from_flip_book(_flipbook, 0.4)

    def __init__(self, parent: AbstractGameObject, scene: AbstractScene, priority: int = 0):
        rect = pygame.Rect(0, 0, *self._sprite_size)
        rect.centerx = scene.get_parent_game().get_display_handler().get_render_display_data().center[0]
        AbstractGameObject.__init__(self, parent, scene, priority=priority, rect=rect)

        self.add_component(Sprite2DAnimated(self, self._flipbook_timed, (0, 0)))
