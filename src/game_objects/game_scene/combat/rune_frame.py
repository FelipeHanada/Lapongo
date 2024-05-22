import random
import pgframework as pgf
from ..inventory.rune_slot import RuneSlot


class RuneFrame(pgf.GameObject):
    _slot_positions = ((32, 16), (80, 16), (40, 40), (72, 40), (16, 56), (56, 56), (96, 56), (56, 76), (32, 96), (80, 96))
    _rune_adjacencies = {
        0: (1, 3, 4),
        1: (0, 2, 6),
        2: (1, 5, 8),
        3: (0, 5, 9),
        4: (0, 7, 8),
        5: (2, 3, 7),
        6: (1, 7, 9),
        7: (4, 5, 6),
        8: (2, 4, 9),
        9: (3, 6, 8),
    }

    def __init__(self, parent, sprite_file_path, rune_inventory_user, *args, **kwargs):
        super().__init__(parent, *args, **kwargs, rect=pgf.PygameRectAdapter(0, 0, 128, 128))

        self.rune_inventory_user = rune_inventory_user

        self.add_child(pgf.components.sprite2d.Sprite2D(self, sprite_file_path))

        self._rune_slots = [
            RuneSlot(self, rect=pgf.PygameRectAdapter(*pos, 16, 16), rune_inventory_user=rune_inventory_user)
            for pos in self._slot_positions
        ]
        for slot in self._rune_slots:
            self.add_child(slot)

        self._adjacency_list = {
            self._rune_slots[slot]: [self._rune_slots[adj] for adj in adjacencies]
            for slot, adjacencies in self._rune_adjacencies.items()
        }

    def get_rune_slots(self):
        return self._rune_slots
    
    def set_locked(self, locked: bool):
        for slot in self._rune_slots:
            slot.set_locked(locked)

    def get_occupied_rune_slots(self):
        return [slot for slot in self._rune_slots if slot.get_item() is not None]
    
    def get_random_occupied_rune_slot(self):
        occupied_slots = self.get_occupied_rune_slots()
        
        if occupied_slots:
            return random.choice(occupied_slots)
        
        return None

    def get_adjacent_rune_slots(self, rune_slot):
        return self._adjacency_list[rune_slot]

    def get_adjacent_runes(self, rune_slot):
        return [slot.get_item() for slot in self._adjacency_list[rune_slot] if slot.get_item() is not None]
