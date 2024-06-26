import pgframework as pgf
from ..combat.player import Player


class InventoryFrameWalletFrame(pgf.GameObject):
    _sprite_file_path = 'src/assets/sprites/game_scene/inventory/wallet_frame.png'
    _sprite = pgf.PygameSurfaceAdapter.from_image(_sprite_file_path)
    _font_file_path = 'src/assets/fonts/alagard.ttf'

    def __init__(self, parent: pgf.GameObject, player: Player, *args, **kwargs):
        super().__init__(parent, *args, **kwargs, rect=pgf.PygameRectAdapter(16, 96, 32, 16))

        self._player = player

        self._sprite2d = self.add_child(pgf.components.sprite2d.Sprite2D(self, self._sprite))

        label_rect = pgf.PygameRectAdapter(2, 0, 18, self.get_rect().get_height())
        label = pgf.game_objects.label.Label(self, '0', self._font_file_path, 12, (197, 152, 70), align='right', align_vertical='center', rect=label_rect)
        self._label: pgf.game_objects.label.Label = self.add_child(label)

    def get_coins(self):
        return self._player.get_leaves()

    def update_callback(self, *args, **kwargs) -> None:
        self._label.set_text(str(self.get_coins()))
