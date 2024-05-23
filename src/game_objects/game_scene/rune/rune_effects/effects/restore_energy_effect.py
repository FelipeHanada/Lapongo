from ..effect import Effect


class RestoreEnergyEffect(Effect):
    def __init__(self, energy: int):
        super().__init__(self.restore_energy)
        self._energy = energy

    def restore_energy(self, combat_controller: 'CombatController', agent: 'CombatAgent', target: 'CombatAgent'):
        print(f'recuperou {self._energy} de energia.')
        agent.restore_energy(self._energy)