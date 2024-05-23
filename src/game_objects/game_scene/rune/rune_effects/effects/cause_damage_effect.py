from ..effect import Effect


class CauseDamageEffect(Effect):
    def __init__(self, damage: int):
        self._damage = damage
        super().__init__(self.cause_damage)

    def cause_damage(self, combat_controller: 'CombatController', agent: 'CombatAgent', target: 'CombatAgent'):
        print(f'causou {self._damage} de dano.')
        target.receive_damage(self._damage)
