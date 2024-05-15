from typing import Any
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
        AbstractGameObject.__init__(self, *args, **kwargs, rect=rect)
        rect.centerx = self.get_parent_scene().get_game().get_display_handler().get_render_display_data().center[0]
        
        self.sprite_2d = self.add_component(Sprite2D(self, self._button_released_sprite))

        self.mouse_listener = self.add_component(MouseListener2(parent=self.sprite_2d, rect=self.get_absolute_rect()))
        self.mouse_listener.on_pressed_in_rect(1, self.on_pressed)
        self.mouse_listener.on_released_in_rect(1, self.on_released)
        self.mouse_listener.on_release_in_rect(1, self.on_release)

        print('SPRITE2D:', self.sprite_2d, self.sprite_2d.get_parent(), self.sprite_2d.get_parent_scene())
        print(self.sprite_2d.get_children())
        print('MOUSE LISTENER:', self.mouse_listener, self.mouse_listener.get_parent(), self.mouse_listener.get_parent_scene())

    def on_pressed(self):
        self.sprite_2d.set_image(self._button_pressed_sprite)

    def on_released(self):
        self.sprite_2d.set_image(self._button_released_sprite)

    def on_release(self):
        self.send_message(MainMenuPlayButtonOnClick(self), SendMessageTargetEnum.ROOT)


class MouseListener2(MouseListener):
    def __init__(self, *args, **kwargs):
        print('MOUSE LISTENER 2:', args, kwargs)
        MouseListener.__init__(self, *args, **kwargs)
        
        print(self.get_parent(), self.get_parent_scene())