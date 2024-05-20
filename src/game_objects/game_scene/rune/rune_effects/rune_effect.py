from typing import Callable


class RuneEffect:
    def __init__(self, activate: Callable[[], None], description: str):
        self._activate: Callable[[], None] = activate
        self._description: str = description

    def get_activate_callback(self) -> Callable[[], None]:
        return self._activate

    def get_description(self) -> str:
        return self._description
