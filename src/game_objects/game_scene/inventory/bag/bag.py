import pgframework as pgf
from .bag_slot import BagSlot
from .trash_can import BagTrashCan


class InventoryFrameBag(pgf.AbstractGameObject):
    _bag_slot_positions = (
        (68, 18), (90, 18), (112, 18), (134, 18), (156, 18),
        (68, 40), (90, 40), (112, 40), (134, 40), (156, 40),
    )

    def __init__(self, *args, rune_inventory_user=None, **kwargs):
        pgf.AbstractGameObject.__init__(self, *args, **kwargs)

        self._bag_slots = [
            BagSlot(self, rect=pgf.PygameRectAdapter(*pos, 16, 16), rune_inventory_user=rune_inventory_user)
            for pos in self._bag_slot_positions
        ]

        for slot in self._bag_slots:
            self.add_child_game_object(slot)

        self._trash_can = self.add_child_game_object(BagTrashCan(self, rune_inventory_user=rune_inventory_user))
