import pgframework as pgf


class MainMenuTitleSign(pgf.GameObject):
    _sprite_file_path = 'src/assets/sprites/main_menu/title_sign.png'
    _sprite_size = (352, 180)
    _sprite_sheet = pgf.components.sprite2d.SpriteSheetGrid(_sprite_file_path, 2, 2, *_sprite_size)
    _flipbook = _sprite_sheet.get_flip_book_from_pack(4, True)
    _flipbook_timed = pgf.components.sprite2d.FlipBookTimed.get_from_flip_book(_flipbook, 0.4)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        rect = pgf.PygameRectAdapter(0, 0, *self._sprite_size)
        rect.set_centerx(self.get_parent().get_rect().get_width() // 2)
        self.set_rect(rect)

        self.add_child(pgf.components.sprite2d.Sprite2DAnimated(self, self._flipbook_timed, offset=(0, 0)))

    def draw_callback(self, renderer: pgf.Renderer) -> None:
        return super().draw_callback(renderer)
