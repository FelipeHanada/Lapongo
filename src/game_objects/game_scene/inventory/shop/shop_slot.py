import pgframework as pgf
from ..rune_slot import RuneSlot
from ...combat.rune.rune_factory import RuneFactory


class ShopSlot(RuneSlot):
    _sprite_file_path = 'src/assets/sprites/game_scene/inventory/shop_slot.png'

    def __init__(self, *args, bag=None, rune_inventory_user=None, **kwargs):
        super().__init__(*args, rune_inventory_user=rune_inventory_user, **kwargs)
        self.set_locked(True)

        self._bag = bag
        self._rune_inventory_user = rune_inventory_user

        self.add_child(pgf.components.sprite2d.Sprite2D(self, self._sprite_file_path, offset=(-2, -2)))

        self.mouse_listener = self.add_child(pgf.components.mouse_listener.MouseListener(self, rect=pgf.PygameRectAdapter(0, 0, *self.get_rect().get_size()), draw_debug_rect=True))
        self.mouse_listener.on_release_in_rect(1, self.buy)

        self.refresh()

    def buy(self):
        empty_slot = self._bag.get_empty_slot()

        if empty_slot is None or self.get_item() is None:
            return
        
        print('buy')
        empty_slot.set_item(self.get_item())
        self.refresh()

    def refresh(self):
        rune = RuneFactory().create_random_rune(1)
        self.set_item(rune)
