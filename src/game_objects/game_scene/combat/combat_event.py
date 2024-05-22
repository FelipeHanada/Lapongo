from typing import Callable


class CombatEvent:
    def __init__(self, t, callback):
        self._t = t
        self._callback: Callable[['GameSceneCombatController'], None] = callback

    def __lt__(self, other: 'CombatEvent'):
        return self.get_t() < other.get_t()

    def get_t(self):
        return self._t

    def get_callback(self):
        return self._callback
