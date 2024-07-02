import pgframework as pgf
from .shop_slot import ShopSlot


class InventoryFrameShop(pgf.GameObject):
    _shop_slot_positions = ((50, 76), (72, 76), (94, 76))


    def __init__(self, *args, bag=None, rune_inventory_user=None, **kwargs):
        super().__init__(*args, **kwargs)

        self._shop_slots = [
            ShopSlot(self, rect=pgf.PygameRectAdapter(*pos, 16, 16), bag=bag, rune_inventory_user=rune_inventory_user)
            for pos in self._shop_slot_positions
        ]

        for slot in self._shop_slots:
            self.add_child(slot)
