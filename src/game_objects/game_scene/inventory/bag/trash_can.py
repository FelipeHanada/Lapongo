import pgframework as pgf
from ..rune_slot import RuneSlot


class BagTrashCan(RuneSlot):
    _sprite_file_path = 'src/assets/sprites/game_scene/inventory/trashcan.png'
    _sprite_sheet = pgf.components.sprite2d.SpriteSheetGrid(_sprite_file_path, 1, 2, 16, 16)

    def __init__(self, *args, rune_inventory_user=None, **kwargs):
        RuneSlot.__init__(self, *args, rune_inventory_user=rune_inventory_user, rect=pgf.PygameRectAdapter(32, 40, 16, 16), **kwargs)

        self._sprite2d_go = pgf.GameObject()
        self._sprite2d = self.add_child(pgf.components.sprite2d.Sprite2D(self, self._sprite_sheet.get_frame(0, 0), priority=1))

        self.mouse_listener.on_leave(self._on_leave)

    def on_hover(self):
        super().on_hover()

        if self._rune_inventory_user is None:
            return
        
        if self._rune_inventory_user.get_holding_rune() is not None:
            self._sprite2d.set_image(self._sprite_sheet.get_frame(0, 1))
        
        else:
            self._sprite2d.set_image(self._sprite_sheet.get_frame(0, 0))
    
    def _on_leave(self):
        self._sprite2d.set_image(self._sprite_sheet.get_frame(0, 0))
