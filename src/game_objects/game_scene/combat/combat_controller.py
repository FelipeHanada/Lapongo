import heapq
from typing import Callable
import pgframework as pgf
from .combat_agent import CombatAgent
from .combat_event import CombatEvent


class EndCombatMessage(pgf.AbstractMessage):
    def __init__(self, sender: pgf.Sender, winner: str, *args, **kwargs):
        super().__init__(sender, *args, **kwargs)
        self._winner = winner
    
    def get_winner(self):
        return self._winner


class Fatigue(CombatEvent):
    def __init__(self, player: CombatAgent, enemy: CombatAgent, start_t: int, t_between_ticks: int, fatigue_damage: Callable[[int], int], fatigue_energy_loss: Callable[[int], int]):
        def fatigue_callback(combat_controller: 'CombatController'):

            delta_t = combat_controller.get_t() - start_t

            player.receive_damage(fatigue_damage(delta_t))
            player.consume_energy(fatigue_energy_loss(delta_t))

            enemy.receive_damage(fatigue_damage(delta_t))
            enemy.consume_energy(fatigue_energy_loss(delta_t))

            combat_controller.add_event_after(t_between_ticks, fatigue_callback)

        super().__init__(start_t, fatigue_callback)


class CombatController(pgf.GameObject):
    _ticks_per_second = 5

    def __init__(self, parent: pgf.GameObject, player: CombatAgent, enemy: CombatAgent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs, visible=False, enabled=False)

        self._player: CombatAgent = player
        self._enemy: CombatAgent = enemy

        self._t: int = 0
        self._events: list = []

        self._elapsed_time: float = 0

    def get_t(self):
        return self._t
    
    def set_t(self, t):
        self._t = t

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

        self._player.start()
        self.add_event(self._player.get_rune_activation_event(self._enemy, 5))

        self._enemy.start()
        self.add_event(self._enemy.get_rune_activation_event(self._player, 5))

        self.add_event(Fatigue(self._player, self._enemy, 100, 5, lambda t: t, lambda t: t))

        self.set_enabled(True)

    def end(self):
        print('combat controller end')
        self.set_enabled(False)

    def update_callback(self, delta_time: float, *args, **kwargs) -> None:
        self._elapsed_time += delta_time

        self.set_t(int(self._elapsed_time * self._ticks_per_second))

        while self.peek_next_event() and self.peek_next_event().get_t() <= self.get_t():
            event = self.pop_next_event()
            event.get_callback()(self)

        if self._player.get_life() <= 0:
            self.send_message(EndCombatMessage(self, 'enemy'), pgf.SendMessageTargetEnum.PARENT)

        if self._enemy.get_life() <= 0:
            self.send_message(EndCombatMessage(self, 'player'), pgf.SendMessageTargetEnum.PARENT)
