import pgframework as pgf


class MainMenuCloseFrame(pgf.AbstractGameObject):
    _sprite_file_path = 'src/assets/sprites/main_menu/close_frame/frame.png'
    _sprite_size = (128, 64)

    def __init__(self, *args, **kwargs):
        pgf.AbstractGameObject.__init__(self, *args, **kwargs, rect=pgf.PygameRectAdapter(0, 0, *self._sprite_size))
        
        rect = self.get_rect()

        rect.set_center((
            self.get_parent().get_rect().get_width() // 2,
            self.get_parent().get_rect().get_height() // 2
        ))
        self.set_rect(rect)

        self.add_component(pgf.components.sprite2d.Sprite2D(self, self._sprite_file_path))

        self.add_child_game_object(CloseFrameButton(self, priority=1))

    def set_opened(self, opened: bool):
        self.set_enabled(opened)
        self.set_visible(opened)


class CloseFrameButton(pgf.AbstractGameObject):
    _sprite_file_path = 'src/assets/sprites/main_menu/close_frame/confirm_button.png'
    _sprite_size = (96, 14)
    _sprite_sheet = pgf.components.sprite2d.SpriteSheetGrid(_sprite_file_path, 1, 2, *_sprite_size)
    _button_released_sprite = _sprite_sheet.get_frame(0, 0)
    _button_pressed_sprite = _sprite_sheet.get_frame(0, 1)

    def __init__(self, parent: pgf.AbstractGameObject, priority: int = 0):
        pgf.AbstractGameObject.__init__(self, parent, priority=priority, rect=pgf.PygameRectAdapter(0, 0, *self._sprite_size))
        
        rect = self.get_rect()
        rect.set_centerx(self.get_parent().get_rect().get_width() // 2)
        rect.set_bottom(self.get_parent().get_rect().get_height() - 13)
        self.set_rect(rect)

        self.sprite_2d = self.add_component(pgf.components.sprite2d.Sprite2D(self, self._sprite_file_path))

        self._mouse_listener = pgf.components.mouse_listener.MouseListener(self.sprite_2d, rect=self.get_absolute_rect())
        self._mouse_listener.on_pressed_in_rect(1, self.on_pressed)
        self._mouse_listener.on_released_in_rect(1, self.on_released)
        self._mouse_listener.on_release_in_rect(1, self.on_release)
        self.add_component(self._mouse_listener)

    def on_pressed(self):
        self.sprite_2d.set_image(self._button_pressed_sprite)

    def on_released(self):
        self.sprite_2d.set_image(self._button_released_sprite)

    def on_release(self):
        self.get_game().stop()

    def on_mouse_button_down(self, event: pgf.PygameEventAdapter):
        self.get_parent_game_object().get_parent_scene().get_parent_game().stop()
