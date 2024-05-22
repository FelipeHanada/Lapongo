import pgframework as pgf
from src.game_objects.game_scene.background import GameSceneBackground
from src.game_objects.game_scene.combat.player import GameScenePlayer
from src.game_objects.game_scene.combat.enemy import GameSceneEnemy
from src.game_objects.game_scene.combat.player_rune_frame import PlayerRuneFrame
from src.game_objects.game_scene.combat.enemy_rune_frame import EnemyRuneFrame
from src.game_objects.game_scene.inventory.rune_inventory_user import GameSceneRuneInventoryUser
from src.game_objects.game_scene.inventory.inventory_frame import GameSceneInventoryFrame
from src.game_objects.game_scene.start_combat_button import GameSceneStartCombatButton, GameSceneStartCombatButtonOnClick
from src.game_objects.game_scene.phase_label import PhaseLabel
from src.game_objects.game_scene.combat.combat_controller import CombatController
from src.game_objects.game_scene.combat.stats_frame.player_stats_frame import PlayerStatsFrame


class GameScene(pgf.AbstractScene):
    BUY_PHASE = 0
    COMBAT_PHASE = 1

    def __init__(self, game: pgf.Game):
        super().__init__(game)

        self._current_game_phase = GameScene.BUY_PHASE
        self._current_round = 1

        self.add_scene_game_object(GameSceneBackground, priority=0)
        self._rune_inventory_user = self.add_scene_game_object(GameSceneRuneInventoryUser, priority=10)

        self._player_rune_frame = self.add_scene_game_object(PlayerRuneFrame, self._rune_inventory_user, priority=1)
        self._player = self.add_scene_game_object(GameScenePlayer, self._player_rune_frame, priority=1)
        self._player_stats_frame = self.add_scene_game_object(PlayerStatsFrame, self._player, priority=1, visible=False)

        self._enemy_rune_frame = self.add_scene_game_object(EnemyRuneFrame, self._rune_inventory_user, priority=1, visible=False, enabled=False)
        self._enemy = self.add_scene_game_object(GameSceneEnemy, self._enemy_rune_frame, priority=1, visible=False, enabled=False)

        self._inventory_frame = self.add_scene_game_object(GameSceneInventoryFrame, rune_inventory_user=self._rune_inventory_user, priority=1)
        self._start_combat_button = self.add_scene_game_object(GameSceneStartCombatButton, priority=1)

        self._combat_controller = self.add_scene_game_object(CombatController, self._player, self._enemy, priority=1)

        self._phase_label = self.add_scene_game_object(PhaseLabel, priority=1, rect=pgf.PygameRectAdapter(0, 138, 480, 20))

        self.keyboard_listener = self.add_child(pgf.components.keyboard_listener.KeyboardListener(self.get_scene_graph_root()))
        self.keyboard_listener.on_key_down(pgf.keys['space'], self.print_scene_tree)
        self.keyboard_listener.on_key_down(pgf.keys['b'], lambda: self.start_buy_phase())

        self.add_message_callback(GameSceneStartCombatButtonOnClick, lambda msg: self.start_combat_phase())

    def get_current_game_phase(self):
        return self._current_game_phase

    def set_current_game_phase(self, game_phase):
        self._current_game_phase = game_phase

    def start_combat_phase(self):
        if self._player_rune_frame.get_occupied_rune_slots() == []:
            return

        self.set_current_game_phase(GameScene.COMBAT_PHASE)

        self._current_game_phase = 'combat'


        self._rune_inventory_user.set_enabled(False)
        self._inventory_frame.set_visible(False)
        self._inventory_frame.set_enabled(False)

        self._player_rune_frame.set_locked(True)
        self._player_stats_frame.set_visible(True)

        self._enemy.set_visible(True)
        self._enemy.set_enabled(True)
        self._enemy_rune_frame.set_visible(True)
        self._enemy_rune_frame.set_enabled(True)

        self._start_combat_button.set_visible(False)
        self._start_combat_button.set_enabled(False)

        self._phase_label.set_phase('combate')

        self._combat_controller.start()

    def start_buy_phase(self):
        self.set_current_game_phase(GameScene.BUY_PHASE)

        self._rune_inventory_user.set_enabled(True)
        self._inventory_frame.set_visible(True)
        self._inventory_frame.set_enabled(True)

        self._player_rune_frame.set_locked(False)
        self._player_stats_frame.set_visible(False)

        self._enemy.set_visible(False)
        self._enemy.set_enabled(False)
        self._enemy_rune_frame.set_visible(False)
        self._enemy_rune_frame.set_enabled(False)

        self._start_combat_button.set_visible(True)
        self._start_combat_button.set_enabled(True)

        self._current_round += 1
        self._phase_label.set_round(self._current_round)
        self._phase_label.set_phase('compras')

        self._combat_controller.end()
