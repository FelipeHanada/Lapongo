import heapq
from typing import Callable
import pgframework as pgf
from .player import Player
from .enemy import Enemy
from .combat_event import CombatEvent
from .combat_events.fatigue import Fatigue
from .combat_events.passive_energy_regeneration import PassiveEnergyRegeneration
from .combat_events.passive_health_regeneration import PassiveHealthRegeneration


class EndCombatMessage(pgf.AbstractMessage):
    def __init__(self, sender: pgf.Sender, winner: str, *args, **kwargs):
        super().__init__(sender, *args, **kwargs)
        self._winner = winner
    
    def get_winner(self):
        return self._winner


class CombatController(pgf.GameObject):
    _ticks_per_second = 5
    _base_gold_per_round: Callable[[int], int] = lambda round: 10 + round * 5

    def __init__(self, parent: pgf.GameObject, player: Player, enemy: Enemy, *args, **kwargs):
        super().__init__(parent, *args, **kwargs, visible=False, enabled=False)

        self._player: Player = player
        self._enemy: Enemy = enemy

        self._current_round = 1

        self._t: int = 0
        self._events: list = []

        self._elapsed_time: float = 0

    def get_t(self):
        return self._t
    
    def set_t(self, t):
        self._t = t

    def get_current_round(self):
        return self._current_round

    def set_current_round(self, current_round):
        self._current_round = current_round

    def add_event(self, event: CombatEvent):
        heapq.heappush(self._events, event)

    def add_event_at(self, t, callback):
        print('add event at', t)
        self.add_event(CombatEvent(t, callback))

    def add_event_after(self, dt, callback):
        print('add event after', dt, 'will happen at', self._t + dt)
        self.add_event(CombatEvent(self._t + dt, callback))

    def pop_next_event(self) -> CombatEvent:
        return heapq.heappop(self._events)
    
    def peek_next_event(self) -> CombatEvent:
        if self._events:
            return self._events[0]
        
        return None

    def start(self):
        print('combat controller start')
        self._t = 0
        self._events = []

        self._elapsed_time = 0

        self._player.start(self, self._enemy)
        self.add_event(self._player.get_rune_activation_event(self._enemy, 5))

        self._enemy.start(self, self._player)
        self.add_event(self._enemy.get_rune_activation_event(self._player, 5))

        self.add_event(Fatigue(self._player, self._enemy, 100, 5, lambda t: t, lambda t: t))
        self.add_event(PassiveEnergyRegeneration(self._player, self._enemy, 5))
        self.add_event(PassiveHealthRegeneration(self._player, self._enemy, 5))

        self.set_enabled(True)

    def end(self):
        print('combat controller end')
        self.set_enabled(False)

        self._player.add_leaves(CombatController._base_gold_per_round(self._current_round))

    def update_callback(self, delta_time: float, *args, **kwargs) -> None:
        self._elapsed_time += delta_time

        self.set_t(int(self._elapsed_time * self._ticks_per_second))

        while self.peek_next_event() and self.peek_next_event().get_t() <= self.get_t():
            event = self.pop_next_event()
            event.get_callback()(self)

            player_health = self._player.get_current_health()
            enemy_health = self._enemy.get_current_health()

            if player_health <= 0 or enemy_health <= 0:
                if player_health <= enemy_health:
                    self.send_message(EndCombatMessage(self, 'enemy'), pgf.SendMessageTargetEnum.PARENT)
                else:
                    self.send_message(EndCombatMessage(self, 'player'), pgf.SendMessageTargetEnum.PARENT)
                
                break
