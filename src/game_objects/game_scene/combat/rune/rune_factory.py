from .rune import Rune
from .runes.water_rune import WaterRune
from .runes.fire_rune import FireRune
from .runes.earth_rune import EarthRune
from .runes.air_rune import AirRune
from .rune_effects.activation_rune_effects.cause_damage_rune_effect import CauseDamageOnActivation
from .rune_effects.activation_rune_effects.restore_life_rune_effect import RestoreLifeOnActivation
from .rune_effects.activation_rune_effects.restore_energy_rune_effect import RestoreEnergyOnActivation


class RuneFactory:
    def __init__(self):
        pass

    def create_random_rune(self):
        pass

    def create_water_rune(self, level: int):
        pass
