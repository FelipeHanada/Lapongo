from typing import Callable


class Effect:
    def __init__(self, callback: Callable[['CombatController', 'CombatAgent', 'CombatAgent'], None]):
        self._callback: Callable[['CombatController', 'CombatAgent', 'CombatAgent'], None] = callback

    def get_callback(self) -> Callable[['CombatController', 'CombatAgent', 'CombatAgent'], None]:
        return self._callback
