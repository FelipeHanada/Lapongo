from ..rune_effect import RuneEffect
from ..effects.restore_energy_effect import RestoreEnergyEffect


class RestoreEnergyOnActivation(RuneEffect):
    def __init__(self, energy: int):
        super().__init__(f'Recupera {energy} de energia ao ser ativada.')
        self.set_activation_effect(RestoreEnergyEffect(energy))
