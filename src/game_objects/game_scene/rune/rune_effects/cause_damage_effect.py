from .rune_effect import RuneEffect


class CauseDamageEffect(RuneEffect):
    def __init__(self, damage: int):
        super().__init__(f'Causa {damage} de dano.')
        self._damage = damage
        self.set_on_activation_callback(self.cause_damage)

    def cause_damage(self, combat_controller: 'CombatController', agent: 'CombatAgent', target: 'CombatAgent'):
        print(f'causou {self._damage} de dano.')
        target.receive_damage(self._damage)
