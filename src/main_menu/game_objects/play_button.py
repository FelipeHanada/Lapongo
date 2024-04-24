from pgframework import *


class MainMenuPlayButton(AbstractGameObject):
    _sprite_file_path = 'src/main_menu/assets/sprites/play_button.png'
    _sprite_size = (96, 24)
    _sprite_sheet = SpriteSheetGrid(_sprite_file_path, 1, 2, *_sprite_size)
    _flipbook = _sprite_sheet.get_flip_book_from_pack(2, True)
    _flipbook_timed = FlipBookTimed.get_from_flip_book(_flipbook, 0.4)
    _flipbook_timed.set_freeze(True)

    def __init__(self, game: Game, priority: int = 0):
        rect = pygame.Rect(0, 180, *self._sprite_size)
        rect.centerx = game.get_display_handler().get_render_display_data().center[0]

        AbstractGameObject.__init__(self, game, priority=priority, rect=rect)
        
        self.sprite_2d = Sprite2DAnimated(self, self._flipbook_timed, (0, 0))
        self.add_component(self.sprite_2d)

        self.mouse_listener = MouseListener(self, self.get_absolute_rect())
        self.mouse_listener.on_press(1, self.on_press)
        self.mouse_listener.on_release(1, self.on_release)
        self.add_component(self.mouse_listener)

    def on_press(self):
        self._flipbook_timed.go_to_frame(1)

    def on_release(self):
        self._flipbook_timed.go_to_frame(0)
