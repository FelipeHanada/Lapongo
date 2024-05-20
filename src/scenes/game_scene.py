import pgframework as pgf
from src.game_objects.game_scene.background import GameSceneBackground
from src.game_objects.game_scene.player import GameScenePlayer
from src.game_objects.game_scene.rune_frame import GameSceneRuneFrame
from src.game_objects.game_scene.inventory.rune_inventory_user import GameSceneRuneInventoryUser
from src.game_objects.game_scene.enemy import GameSceneEnemy
from src.game_objects.game_scene.inventory.inventory_frame import GameSceneInventoryFrame
from src.game_objects.game_scene.start_combat_button import GameSceneStartCombatButton, GameSceneStartCombatButtonOnClick


class GameScene(pgf.AbstractScene):
    BUY_PHASE = 0
    COMBAT_PHASE = 1

    def __init__(self, game: pgf.Game):
        super().__init__(game, (255, 255, 255))

        self.add_scene_game_object(GameSceneBackground, priority=0)
        self._rune_inventory_user = self.add_scene_game_object(GameSceneRuneInventoryUser, priority=10)
        self.add_scene_game_object(GameScenePlayer, priority=1)
        self._enemy = self.add_scene_game_object(GameSceneEnemy, priority=1, visible=False)
        self._rune_frame = self.add_scene_game_object(GameSceneRuneFrame, rune_inventory_user=self._rune_inventory_user, priority=1)
        self._inventory_frame = self.add_scene_game_object(GameSceneInventoryFrame, rune_inventory_user=self._rune_inventory_user, priority=1)
        self._start_combat_button = self.add_scene_game_object(GameSceneStartCombatButton, priority=1)

        self.keyboard_listener = self.add_child(pgf.components.keyboard_listener.KeyboardListener(self.get_scene_graph_root()))
        self.keyboard_listener.on_key_down(pgf.keys['space'], self.print_scene_tree)
        self.keyboard_listener.on_key_down(pgf.keys['b'], lambda: self.start_buy_phase())

        self._current_game_phase = GameScene.BUY_PHASE

        self.add_message_callback(GameSceneStartCombatButtonOnClick, lambda msg: self.start_combat_phase())

    def get_current_game_phase(self):
        return self._current_game_phase

    def set_current_game_phase(self, game_phase):
        self._current_game_phase = game_phase

    def start_combat_phase(self):
        self.set_current_game_phase(GameScene.COMBAT_PHASE)

        self._current_game_phase = 'combat'

        self._enemy.set_visible(True)
        self._enemy.set_enabled(True)

        self._rune_frame.set_locked(True)
        self._rune_inventory_user.set_enabled(False)

        self._inventory_frame.set_visible(False)
        self._inventory_frame.set_enabled(False)

        self._start_combat_button.set_visible(False)
        self._start_combat_button.set_enabled(False)

    def start_buy_phase(self):
        self.set_current_game_phase(GameScene.BUY_PHASE)

        self._enemy.set_visible(False)
        self._enemy.set_enabled(False)

        self._rune_frame.set_locked(False)
        self._rune_inventory_user.set_enabled(True)

        self._inventory_frame.set_visible(True)
        self._inventory_frame.set_enabled(True)

        self._start_combat_button.set_visible(True)
        self._start_combat_button.set_enabled(True)
