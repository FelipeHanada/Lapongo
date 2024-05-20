import pgframework as pgf


class GameSceneStartCombatButtonOnClick(pgf.AbstractMessage):
    pass


class GameSceneStartCombatButton(pgf.GameObject):
    _sprite_file_path = 'src/assets/sprites/game_scene/start_combat_button.png'
    _sprite_size = (24, 24)
    _sprite_sheet = pgf.components.sprite2d.SpriteSheetGrid(_sprite_file_path, 1, 2, *_sprite_size)
    _button_released_sprite = _sprite_sheet.get_frame(0, 0)
    _button_pressed_sprite = _sprite_sheet.get_frame(0, 1)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        rect = pgf.PygameRectAdapter(0, 160, *self._sprite_size)
        rect.set_centerx(self.get_parent().get_rect().get_width() // 2)
        self.set_rect(rect)
        
        self.sprite_2d = self.add_child(pgf.components.sprite2d.Sprite2D(self, self._button_released_sprite, draw_debug_rect=True))

        self.mouse_listener = self.add_child(pgf.components.mouse_listener.MouseListener(self, rect=pgf.PygameRectAdapter(0, 0, *rect.get_size()), draw_debug_rect=True))
        self.mouse_listener.on_pressed_in_rect(1, self.on_pressed)
        self.mouse_listener.on_released_in_rect(1, self.on_released)
        self.mouse_listener.on_release_in_rect(1, self.on_release)

    def on_pressed(self):
        self.sprite_2d.set_image(self._button_pressed_sprite)

    def on_released(self):
        self.sprite_2d.set_image(self._button_released_sprite)

    def on_release(self):
        self.send_message(GameSceneStartCombatButtonOnClick(self), pgf.SendMessageTargetEnum.ROOT)
