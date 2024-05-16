import pgframework as pgf
from ..rune_slot import RuneSlot


class BagTrashCan(RuneSlot):
    _sprite_file_path = 'src/assets/sprites/game_scene/inventory/trashcan.png'
    _sprite_sheet = pgf.components.sprite2d.SpriteSheetGrid(_sprite_file_path, 1, 2, 16, 16)

    def __init__(self, *args, rune_inventory_user, **kwargs):
        super().__init__(*args, rune_inventory_user=rune_inventory_user, rect=pgf.PygameRectAdapter(32, 40, 16, 16), **kwargs)

        self._sprite2d_go = pgf.GameObject()
        self._sprite2d = self.add_child(pgf.components.sprite2d.Sprite2D(self, self._sprite_sheet.get_frame(0, 0)))

        self.mouse_listener.on_leave(self._on_leave)

    def swap_rune_with_hand(self):
        self.remove_item()
        self.place_rune_from_hand()

    def on_hover(self):
        super().on_hover()

        self._sprite2d.set_image(self._sprite_sheet.get_frame(0, 1))

        if self.get_item() is not None:
            self.get_item().set_visible(True)

    def _on_leave(self):
        self._sprite2d.set_image(self._sprite_sheet.get_frame(0, 0))

        if self.get_item() is not None:
            self.get_item().set_visible(False)
