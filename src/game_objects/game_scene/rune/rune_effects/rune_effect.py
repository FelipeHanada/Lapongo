from typing import Callable


class RuneEffect:
    def __init__(self, description: str):
        self._on_combat_start: Callable[['CombatController', 'CombatAgent', 'CombatAgent'], None] = None
        self._on_combat_end: Callable[['CombatController', 'CombatAgent', 'CombatAgent'], None] = None
        self._on_activation: Callable[['CombatController', 'CombatAgent', 'CombatAgent'], None] = None
        #self._on_

        self._description: str = description

    def get_on_activation_callback(self) -> Callable[['CombatController', 'CombatAgent', 'CombatAgent'], None]:
        return self._on_activation

    def get_on_combat_start_callback(self) -> Callable[['CombatController', 'CombatAgent', 'CombatAgent'], None]:
        return self._on_combat_start
    
    def get_on_combat_end_callback(self) -> Callable[['CombatController', 'CombatAgent', 'CombatAgent'], None]:
        return self._on_combat_end
    
    def set_on_activation_callback(self, callback: Callable[['CombatController', 'CombatAgent', 'CombatAgent'], None]):
        self._on_activation = callback

    def set_on_combat_start_callback(self, callback: Callable[['CombatController', 'CombatAgent', 'CombatAgent'], None]):
        self._on_combat_start = callback
    
    def set_on_combat_end_callback(self, callback: Callable[['CombatController', 'CombatAgent', 'CombatAgent'], None]):
        self._on_combat_end = callback
    
    def get_description(self) -> str:
        return self._description

