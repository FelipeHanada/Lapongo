import pgframework as pgf
from .bag.bag import InventoryFrameBag
from .shop.shop import InventoryFrameShop
from .wallet_frame import InventoryFrameWalletFrame


class GameSceneInventoryFrame(pgf.GameObject):
    _sprite_file_path = 'src/assets/sprites/game_scene/inventory/shop_frame.png'

    def __init__(self, *args, rune_inventory_user=None, **kwargs):
        pgf.GameObject.__init__(self, *args, **kwargs, rect=pgf.PygameRectAdapter(240, 10, 192, 128))

        self.rune_inventory_user = rune_inventory_user

        self.add_child(pgf.components.sprite2d.Sprite2D(self, self._sprite_file_path))

        self._bag = self.add_child(InventoryFrameBag(self, rune_inventory_user=rune_inventory_user))
        self._shop = self.add_child(InventoryFrameShop(self, rune_inventory_user=rune_inventory_user))
        self._wallet_frame = self.add_child(InventoryFrameWalletFrame(self))
