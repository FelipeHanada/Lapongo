from .effect import Effect


class RuneEffect:
    def __init__(self, description: str):
        self._combat_start_effect: Effect = None
        self._combat_end_effect: Effect = None
        self._activation_effect: Effect = None
        self._on_deal_damage_effect: Effect = None
        self._on_receive_damage_effect: Effect = None
        self._on_heal_effect: Effect = None
        self._on_energy_restore_effect: Effect = None
        self._on_energy_depletion_effect: Effect = None

        self._description: str = description

    def get_activation_effect(self) -> Effect:
        return self._activation_effect

    def get_combat_start_effect(self) -> Effect:
        return self._combat_start_effect

    def get_combat_end_effect(self) -> Effect:
        return self._combat_end_effect

    def set_activation_effect(self, rune_effect: Effect):
        self._activation_effect = rune_effect

    def set_combat_start_effect(self, rune_effect: Effect):
        self._combat_start_effect = rune_effect

    def set_combat_end_effect(self, rune_effect: Effect):
        self._combat_end_effect = rune_effect

    def get_description(self) -> str:
        return self._description
