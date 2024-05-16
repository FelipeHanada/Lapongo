import pgframework as pgf
from src.game_objects.game_scene.background import GameSceneBackground
from src.game_objects.game_scene.player import GameScenePlayer
from src.game_objects.game_scene.rune_frame import GameSceneRuneFrame
from src.game_objects.game_scene.inventory.rune_inventory_user import GameSceneRuneInventoryUser
from src.game_objects.game_scene.enemy import GameSceneEnemy
from src.game_objects.game_scene.inventory.inventory_frame import GameSceneInventoryFrame


class GameScene(pgf.AbstractScene):
    def __init__(self, game: pgf.Game):
        super().__init__(game, (255, 255, 255))

        self.add_scene_game_object(GameSceneBackground, priority=0)
        rune_inventory_user = self.add_scene_game_object(GameSceneRuneInventoryUser, priority=10)
        self.add_scene_game_object(GameScenePlayer, priority=1)
        self.add_scene_game_object(GameSceneEnemy, priority=1)
        self.add_scene_game_object(GameSceneRuneFrame, rune_inventory_user=rune_inventory_user, priority=1)
        self.add_scene_game_object(GameSceneInventoryFrame, rune_inventory_user=rune_inventory_user, priority=1)

        self.keyboard_listener = self.add_child(pgf.components.keyboard_listener.KeyboardListener(self.get_scene_graph_root()))
        self.keyboard_listener.on_key_down(pgf.keys['space'], self.print_scene_tree)
