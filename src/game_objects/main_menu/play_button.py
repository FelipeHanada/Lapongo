import pgframework as pgf


class MainMenuPlayButtonOnClick(pgf.AbstractMessage):
    pass


class MainMenuPlayButton(pgf.AbstractGameObject):
    _sprite_file_path = 'src/assets/sprites/main_menu/play_button.png'
    _sprite_size = (96, 24)
    _sprite_sheet = pgf.components.sprite2d.SpriteSheetGrid(_sprite_file_path, 1, 2, *_sprite_size)
    _button_released_sprite = _sprite_sheet.get_frame(0, 0)
    _button_pressed_sprite = _sprite_sheet.get_frame(0, 1)

    def __init__(self, *args, **kwargs):
        rect = pgf.PygameRectAdapter(0, 180, *self._sprite_size)
        pgf.AbstractGameObject.__init__(self, *args, **kwargs, rect=rect)
        rect.set_centerx(self.get_parent().get_rect().get_width() // 2)
        
        self.sprite_2d = self.add_component(pgf.components.sprite2d.Sprite2D(self, self._button_released_sprite))

        self.mouse_listener = self.add_component(pgf.components.mouse_listener.MouseListener(self.sprite_2d, rect=self.get_absolute_rect()))
        self.mouse_listener.on_pressed_in_rect(1, self.on_pressed)
        self.mouse_listener.on_released_in_rect(1, self.on_released)
        self.mouse_listener.on_release_in_rect(1, self.on_release)

    def on_pressed(self):
        self.sprite_2d.set_image(self._button_pressed_sprite)

    def on_released(self):
        self.sprite_2d.set_image(self._button_released_sprite)

    def on_release(self):
        self.send_message(MainMenuPlayButtonOnClick(self), pgf.SendMessageTargetEnum.ROOT)
