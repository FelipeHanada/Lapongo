import pgframework as pgf
from .bag_slot import BagSlot


class GameSceneShop(pgf.AbstractGameObject):
    _sprite_file_path = 'src/assets/sprites/game_scene/shop/shop_frame.png'

    def __init__(self, *args, rune_inventory_user=None, **kwargs):
        pgf.AbstractGameObject.__init__(self, *args, **kwargs, rect=pgf.PygameRectAdapter(240, 10, 192, 128))

        self.rune_inventory_user = rune_inventory_user

        self.add_component(pgf.components.sprite2d.Sprite2D(self, self._sprite_file_path))

        slot_positions = (
            (68, 18), (90, 18), (112, 18), (134, 18), (156, 18),
            (68, 40), (90, 40), (112, 40), (134, 40), (156, 40),
        )
        self._rune_slots = [
            BagSlot(self, rect=pgf.PygameRectAdapter(*pos, 16, 16), rune_inventory_user=rune_inventory_user)
            for pos in slot_positions
        ]
        for slot in self._rune_slots:
            self.add_child_game_object(slot)
