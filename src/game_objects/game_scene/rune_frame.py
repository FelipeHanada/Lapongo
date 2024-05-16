import pgframework as pgf
from .inventory.rune_slot import RuneSlot

class GameSceneRuneFrame(pgf.GameObject):
    _sprite_file_path = 'src/assets/sprites/game_scene/rune_frame.png'

    def __init__(self, *args, rune_inventory_user, **kwargs):
        pgf.GameObject.__init__(self, *args, **kwargs, rect=pgf.PygameRectAdapter(64, 8, 128, 128))

        self.rune_inventory_user = rune_inventory_user

        self.add_child(pgf.components.sprite2d.Sprite2D(self, self._sprite_file_path))

        slot_positions = ((32, 16), (80, 16), (40, 40), (72, 40), (16, 56), (56, 56), (96, 56), (56, 76), (32, 96), (80, 96))

        self._rune_slots = [
            RuneSlot(self, rect=pgf.PygameRectAdapter(*pos, 16, 16), rune_inventory_user=rune_inventory_user)
            for pos in slot_positions
        ]
        for slot in self._rune_slots:
            self.add_child(slot)

        from .runes.water_rune import WaterRune
        from .runes.air_rune import AirRune
        from .runes.fire_rune import FireRune
        from .runes.earth_rune import EarthRune
        self._rune_slots[0].set_item(WaterRune())
        self._rune_slots[1].set_item(AirRune())
        self._rune_slots[2].set_item(FireRune())
        self._rune_slots[3].set_item(EarthRune())
