from pgframework import *
from src.game_objects.game_scene.background import GameSceneBackground
from src.game_objects.game_scene.player import GameScenePlayer
from src.game_objects.game_scene.rune_frame import GameSceneRuneFrame
from src.game_objects.game_scene.inventory.rune_inventory_user import GameSceneRuneInventoryUser
from src.game_objects.game_scene.enemy import GameSceneEnemy
from src.game_objects.game_scene.inventory.shop.shop import GameSceneShop

class GameScene(AbstractScene):
    def __init__(self, game: Game):
        AbstractScene.__init__(self, game, (255, 255, 255))

        self.add_scene_game_object(GameSceneBackground, priority=0)
        rune_inventory_user = self.add_scene_game_object(GameSceneRuneInventoryUser, priority=10)
        self.add_scene_game_object(GameScenePlayer, priority=1)
        self.add_scene_game_object(GameSceneEnemy, priority=1)
        self.add_scene_game_object(GameSceneRuneFrame, rune_inventory_user=rune_inventory_user, priority=1)
        self.add_scene_game_object(GameSceneShop, rune_inventory_user=rune_inventory_user, priority=1)
