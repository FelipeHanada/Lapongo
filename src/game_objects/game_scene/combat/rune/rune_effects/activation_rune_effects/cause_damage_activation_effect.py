from ..rune_effect import RuneEffect
from ..effects.cause_damage_effect import CauseDamageEffect


class CauseDamageOnActivation(RuneEffect):
    def __init__(self, damage: int):
        super().__init__(f'Causa {damage} de dano ao ser ativada.')
        self.set_activation_effect(CauseDamageEffect(damage))
