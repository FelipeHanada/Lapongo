from pgframework import *


class MainMenuCloseFrame(AbstractGameObject):
    _sprite_file_path = 'src/assets/sprites/main_menu/close_frame/frame.png'
    _sprite_size = (128, 64)

    def __init__(self, *args, **kwargs):
        AbstractGameObject.__init__(self, *args, **kwargs, rect=pygame.Rect(0, 0, *self._sprite_size))
        
        rect = self.get_rect()
        rect.centerx = self.get_parent_game_object().get_rect().width // 2
        rect.centery = self.get_parent_game_object().get_rect().height // 2
        self.set_rect(rect)

        self.add_component(Sprite2D(self, self._sprite_file_path))

        self.add_child_game_object(CloseFrameButton(self, kwargs['parent_scene'], priority=1))

        self._mouse_listener: 'MouseListener' = self.add_component(MouseListener(self, self.get_absolute_rect()))
        self._mouse_listener.on_blur(self.on_blur)

    def set_opened(self, opened: bool):
        self.set_enabled(opened)
        self.set_visible(opened)
        self._mouse_listener.set_focused(opened)

    def on_blur(self):
        self.get_parent_scene().set_open_close_frame(False)

class CloseFrameButton(AbstractGameObject):
    _sprite_file_path = 'src/assets/sprites/main_menu/close_frame/confirm_button.png'
    _sprite_size = (96, 14)
    _sprite_sheet = SpriteSheetGrid(_sprite_file_path, 1, 2, *_sprite_size)
    _button_released_sprite = _sprite_sheet.get_frame(0, 0)
    _button_pressed_sprite = _sprite_sheet.get_frame(0, 1)

    def __init__(self, parent: AbstractGameObject, scene: AbstractScene, priority: int = 0):
        AbstractGameObject.__init__(self, parent, scene, priority=priority, rect=pygame.Rect(0, 0, *self._sprite_size))
        
        rect = self.get_rect()
        rect.centerx = self.get_parent_game_object().get_rect().width // 2
        rect.bottom = self.get_parent_game_object().get_rect().height - 13
        self.set_rect(rect)

        self.sprite_2d = self.add_component(Sprite2D(self, self._sprite_file_path))

        self._mouse_listener = MouseListener(self.sprite_2d, self.get_absolute_rect())
        self._mouse_listener.on_pressed(1, self.on_pressed)
        self._mouse_listener.on_released(1, self.on_released)
        self._mouse_listener.on_release(1, self.on_release)
        self.add_component(self._mouse_listener)

    def on_pressed(self):
        self.sprite_2d.set_image(self._button_pressed_sprite)

    def on_released(self):
        self.sprite_2d.set_image(self._button_released_sprite)

    def on_release(self):
        self.get_game().stop()

    def on_mouse_button_down(self, event: pygame.event.Event):
        self.get_parent_game_object().get_parent_scene().get_parent_game().stop()
