from typing import Callable


class RuneEffect:
    def __init__(self, activate: Callable[[], None], description: str):
        self._activate: Callable[[], None] = activate
        self._description: str = description

    def get_activate_callback(self) -> Callable[[], None]:
        return self._activate

    def get_description(self) -> str:
        return self._description


class RuneEffect2:
    def __init__(self, description: str):
        self._on_combat_start: Callable[[], None] = None
        self._on_combat_end: Callable[[], None] = None
        self._on_activation: Callable[[], None] = None
        #self._on_

        self._description: str = description

    def get_activate_callback(self) -> Callable[[], None]:
        return self._activate

    def get_description(self) -> str:
        return self._description

