import pgframework as pgf
from .shop_slot import ShopSlot


class InventoryFrameShop(pgf.GameObject):
    _shop_slot_positions = ((58, 76), (80, 76), (102, 76))


    def __init__(self, *args, player=None, bag=None, rune_inventory_user=None, **kwargs):
        super().__init__(*args, **kwargs)

        self._shop_slots = [
            ShopSlot(self, rect=pgf.PygameRectAdapter(*pos, 16, 16), player=player, bag=bag, rune_inventory_user=rune_inventory_user)
            for pos in self._shop_slot_positions
        ]

        for slot in self._shop_slots:
            self.add_child(slot)

    def on_buy_phase_start(self):
        for slot in self._shop_slots:
            slot.refresh()
