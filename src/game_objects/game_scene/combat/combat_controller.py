import heapq
import pgframework as pgf
from .combat_agent import CombatAgent
from .rune_frame import RuneFrame


class CombatEvent:
    def __init__(self, t, callback):
        self._t = t
        self._callback = callback

    def get_t(self):
        return self._t

    def get_callback(self):
        return self._callback

class GameSceneCombatController(pgf.GameObject):
    def __init__(self, player: CombatAgent, player_rune_frame, enemy: CombatAgent, enemy_rune_frame, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._player: CombatAgent = player
        self._player_rune_frame: RuneFrame = player_rune_frame
        self._enemy: CombatAgent = enemy
        self._enemy_rune_frame: RuneFrame = enemy_rune_frame

        self._t = 0
        self._events = []

    def get_t(self):
        return self._t
    
    def set_t(self, t):
        self._t = t

    def add_event(self, event: CombatEvent):
        heapq.heappush(self._events, (event.get_t(), event))

    def add_event_at(self, t, callback):
        self.add_event(CombatEvent(t, callback))

    def add_event_after(self, dt, callback):
        self.add_event(CombatEvent(self._t + dt, callback))

    def get_next_event(self):
        return heapq.heappop(self._events)[1] if self._events else None

    def start(self):
        print('combat controller start')
        self._t = 0
        self._events = []

        self.add_event_at(0, self._player_rune_frame.get_random_occupied_rune_slot().get_rune().get_activation_effect())

        pass

    def end(self):
        print('combat controller end')

        pass

    def update_callback(self) -> None:
        pass
