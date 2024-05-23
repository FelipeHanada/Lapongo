from ..rune_effect import RuneEffect
from ..effects.restore_energy_effect import RestoreEnergyEffect


class RestoreLifeOnActivation(RuneEffect):
    def __init__(self, life: int):
        super().__init__(f'Recupera {life} de vida ao ser ativada.')
        self.set_activation_effect(RestoreEnergyEffect(life))
