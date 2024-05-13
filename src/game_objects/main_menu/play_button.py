from pgframework import *

class MainMenuPlayButtonOnClick(AbstractMessage):
    pass


class MainMenuPlayButton(AbstractGameObject):
    _sprite_file_path = 'src/assets/sprites/main_menu/play_button.png'
    _sprite_size = (96, 24)
    _sprite_sheet = SpriteSheetGrid(_sprite_file_path, 1, 2, *_sprite_size)
    _button_released_sprite = _sprite_sheet.get_frame(0, 0)
    _button_pressed_sprite = _sprite_sheet.get_frame(0, 1)

    def __init__(self, *args, **kwargs):
        rect = pygame.Rect(0, 180, *self._sprite_size)
        
        rect.centerx = kwargs['parent_scene'].get_game().get_display_handler().get_render_display_data().center[0]

        AbstractGameObject.__init__(self, *args, **kwargs, rect=rect)
        
        self.sprite_2d = self.add_component(Sprite2D(self, self._button_released_sprite))

        self.mouse_listener = self.add_component(MouseListener(self.sprite_2d, self.get_absolute_rect()))
        self.mouse_listener.on_pressed(1, self.on_pressed)
        self.mouse_listener.on_released(1, self.on_released)
        self.mouse_listener.on_release(1, self.on_release)

    def on_pressed(self):
        self.sprite_2d.set_image(self._button_pressed_sprite)

    def on_released(self):
        self.sprite_2d.set_image(self._button_released_sprite)

    def on_release(self):
        self.send_message(MainMenuPlayButtonOnClick(self), SendMessageTargetEnum.ROOT)

