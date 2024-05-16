import pgframework as pgf


class InventoryFrameWalletFrame(pgf.GameObject):
    _sprite_file_path = 'src/assets/sprites/game_scene/inventory/wallet_frame.png'
    _sprite = pgf.PygameSurfaceAdapter.from_image(_sprite_file_path)
    _font_file_path = 'src/assets/fonts/alagard.ttf'
    _font = pgf.FontAdapter(_font_file_path, 12)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs, rect=pgf.PygameRectAdapter(16, 96, 32, 16))

        self._sprite2d = self.add_child(pgf.components.sprite2d.Sprite2D(self, self._sprite))

    def get_coins(self):
        return 123

    def update_callback(self) -> None:
        sprite = self._sprite.copy()
        text = self._font.render(str(self.get_coins()), False, (197, 152, 70))
        sprite.blit(text, (12 - text.get_width() // 2, 4))
        self._sprite2d.set_image(sprite)
