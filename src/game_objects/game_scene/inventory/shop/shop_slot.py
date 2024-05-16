import pgframework as pgf
from ..slot import Slot


class ShopSlot(Slot):
    _sprite_file_path = 'src/assets/sprites/game_scene/inventory/shop_slot.png'

    def __init__(self, *args, rune_inventory_user=None, **kwargs):
        Slot.__init__(self, *args, **kwargs)

        self._rune_inventory_user = rune_inventory_user

        self.add_component(pgf.components.sprite2d.Sprite2D(self, self._sprite_file_path, offset=(-2, -2)))

        self.mouse_listener = self.add_component(pgf.components.mouse_listener.MouseListener(self, show_debug=True))
        self.mouse_listener.on_release_in_rect(1, self.buy)

    def buy(self):
        print('buy')
