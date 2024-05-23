from .effect import Effect


class RuneEffect:
    def __init__(self, description: str):
        self._combat_start_effect: Effect = None
        self._combat_end_effect: Effect = None
        self._activation_effect: Effect = None

        self._description: str = description

    def get_activation_effect(self) -> Effect:
        return self._on_activation

    def get_combat_start_effect(self) -> Effect:
        return self._on_combat_start

    def get_combat_end_effect(self) -> Effect:
        return self._on_combat_end

    def set_activation_effect(self, rune_effect: Effect):
        self._on_activation = rune_effect

    def set_combat_start_effect(self, rune_effect: Effect):
        self._on_combat_start = rune_effect

    def set_combat_end_effect(self, rune_effect: Effect):
        self._on_combat_end = rune_effect

    def get_description(self) -> str:
        return self._description
