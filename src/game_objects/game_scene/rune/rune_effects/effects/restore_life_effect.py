from ..effect import Effect


class RestoreLifeEffect(Effect):
    def __init__(self, life: int):
        super().__init__(self.restore_life)
        self._life = life

    def restore_life(self, combat_controller: 'CombatController', agent: 'CombatAgent', target: 'CombatAgent'):
        print(f'recuperou {self._life} de vida.')
        agent.restore_life(self._life)
