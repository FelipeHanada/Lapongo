import pgframework as pgf
from src.game_objects.game_scene.background import GameSceneBackground
from src.game_objects.game_scene.combat.player import Player
from src.game_objects.game_scene.combat.enemy import Enemy
from src.game_objects.game_scene.combat.player_rune_frame import PlayerRuneFrame
from src.game_objects.game_scene.combat.enemy_rune_frame import EnemyRuneFrame
from src.game_objects.game_scene.inventory.rune_inventory_user import RuneInventoryUser
from src.game_objects.game_scene.inventory.inventory_frame import InventoryFrame
from src.game_objects.game_scene.start_combat_button import StartCombatButton, StartCombatButtonOnClick
from src.game_objects.game_scene.phase_label import PhaseLabel
from src.game_objects.game_scene.combat.combat_controller import CombatController, EndCombatMessage
from src.game_objects.game_scene.combat.stats_frame.player_stats_frame import PlayerStatsFrame
from src.game_objects.game_scene.combat.stats_frame.enemy_stats_frame import EnemyStatsFrame
import pygame


class GameScene(pgf.AbstractScene):
    BUY_PHASE = 0
    COMBAT_PHASE = 1

    def __init__(self, game: pgf.Game):
        super().__init__(game)

        self._current_game_phase = GameScene.BUY_PHASE
        self._current_round = 1

        self.add_scene_game_object(GameSceneBackground, priority=0)
        self._rune_inventory_user = self.add_scene_game_object(RuneInventoryUser, priority=10)

        self._player_rune_frame = self.add_scene_game_object(PlayerRuneFrame, self._rune_inventory_user, priority=1)
        self._player = self.add_scene_game_object(Player, self._player_rune_frame, priority=1)
        self._player_stats_frame = self.add_scene_game_object(PlayerStatsFrame, self._player, priority=1, visible=False)

        self._enemy_rune_frame = self.add_scene_game_object(EnemyRuneFrame, self._rune_inventory_user, priority=1, visible=False, enabled=False)
        self._enemy = self.add_scene_game_object(Enemy, self._enemy_rune_frame, priority=1, visible=False, enabled=False)
        self._enemy_stats_frame = self.add_scene_game_object(EnemyStatsFrame, self._enemy, priority=1, visible=False)

        self._inventory_frame = self.add_scene_game_object(InventoryFrame, self._player, rune_inventory_user=self._rune_inventory_user, priority=1)
        self._start_combat_button = self.add_scene_game_object(StartCombatButton, priority=1)

        self._combat_controller = self.add_scene_game_object(CombatController, self._player, self._enemy, priority=1)

        self._phase_label = self.add_scene_game_object(PhaseLabel, priority=1, rect=pgf.PygameRectAdapter(0, 138, 480, 20))

        self.keyboard_listener = self.add_child(pgf.components.keyboard_listener.KeyboardListener(self.get_scene_graph_root()))
        self.keyboard_listener.on_key_down(pgf.keys['space'], self.print_scene_tree)
        self.keyboard_listener.on_key_down(pgf.keys['b'], lambda: self.start_buy_phase())

        self.add_message_callback(StartCombatButtonOnClick, self.on_start_combat_message)
        self.add_message_callback(EndCombatMessage, self.on_end_combat_message)

        self.start_buy_phase()

    def get_current_game_phase(self):
        return self._current_game_phase

    def set_current_game_phase(self, game_phase):
        self._current_game_phase = game_phase

    def on_start_combat_message(self, msg):
        if self._player_rune_frame.get_occupied_rune_slots() == []:
            return

        self.start_combat_phase()
        self._combat_controller.set_current_round(self._current_round)
        self._combat_controller.start()

    def on_end_combat_message(self, msg: EndCombatMessage):
        self._combat_controller.end()
        
        print('Combat ended')
        print('winner:', msg.get_winner())

        self.start_buy_phase()

    def start_combat_phase(self):
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
        self._enemy_stats_frame.set_visible(True)

        self._start_combat_button.set_visible(False)
        self._start_combat_button.set_enabled(False)

        self._phase_label.set_phase('combate')

        pygame.mixer.init()
        pygame.mixer.music.get_volume()
        pygame.mixer.music.set_volume(0.5)
        musica = pygame.mixer.music.load("musicaRodada.mp3")
        pygame.mixer.music.play(-1)

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
        self._enemy_stats_frame.set_visible(False)

        shop = self._inventory_frame.get_shop()
        shop.on_buy_phase_start()

        self._start_combat_button.set_visible(True)
        self._start_combat_button.set_enabled(True)

        self._current_round += 1
        self._phase_label.set_current_round(self._current_round)
        self._phase_label.set_phase('compras')
