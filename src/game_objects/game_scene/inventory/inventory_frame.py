import pgframework as pgf
from .bag.bag import InventoryFrameBag
from .shop.shop import InventoryFrameShop
from .wallet_frame import InventoryFrameWalletFrame


class InventoryFrame(pgf.GameObject):
    _sprite_file_path = 'src/assets/sprites/game_scene/inventory/shop_frame.png'

    def __init__(self, parent: pgf.GameObject, player, *args, rune_inventory_user=None, **kwargs):
        super().__init__(parent, *args, **kwargs, rect=pgf.PygameRectAdapter(240, 10, 192, 128))

        self.rune_inventory_user = rune_inventory_user

        self.add_child(pgf.components.sprite2d.Sprite2D(self, self._sprite_file_path))

        self._bag = self.add_child(InventoryFrameBag(self, rune_inventory_user=rune_inventory_user))
        self._shop = self.add_child(InventoryFrameShop(self, player=player, bag=self._bag, rune_inventory_user=rune_inventory_user))
        self._wallet_frame = self.add_child(InventoryFrameWalletFrame(self, player))

    def get_bag(self):
        return self._bag
    
    def get_shop(self):
        return self._shop
    
    def get_wallet_frame(self):
        return self._wallet_frame
