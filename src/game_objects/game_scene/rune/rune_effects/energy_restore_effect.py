from .rune_effect import RuneEffect


class EnergyRestoreEffect(RuneEffect):
    def __init__(self, energy: int):
        super().__init__(self.restore_energy, f'Recupera {energy} de energia.')
        self._energy = energy

    def restore_energy(self):
        print(f'recuperou {self._energy} de energia.')
