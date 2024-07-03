import json
import random
from .rune import Rune
from .runes.water_rune import WaterRune
from .runes.fire_rune import FireRune
from .runes.earth_rune import EarthRune
from .runes.air_rune import AirRune
from .rune_effects.activation_rune_effects.cause_damage_activation_effect import CauseDamageOnActivation
from .rune_effects.activation_rune_effects.restore_life_activation_effect import RestoreLifeOnActivation
from .rune_effects.activation_rune_effects.restore_energy_activation_effect import RestoreEnergyOnActivation

from .rune_effects.induction_rune_effects.leaves_path_effect import LeavesPathEffect


class RuneFactory:
    with open('src/game_objects/game_scene/combat/rune/runes.json', 'r') as runes_data_file:
        runes_data = json.load(runes_data_file)

    with open('src/game_objects/game_scene/combat/rune/rune_effects_level_scaling.json', 'r') as rune_effects_level_scaling_file:
        rune_effects_level_scaling = json.load(rune_effects_level_scaling_file)

    __cost_function = lambda level: 10 + 5 * level

    runes_class_map = {
        'water_rune': WaterRune,
        'fire_rune': FireRune,
        'earth_rune': EarthRune,
        'air_rune': AirRune
    }

    def __init__(self):
        pass

    @staticmethod
    def create_random_rune(level: int, activation_rune_effect_name: str = None):
        rune_type = random.choice(list(RuneFactory.runes_class_map.keys()))
        rune_class = RuneFactory.runes_class_map[rune_type]

        data = RuneFactory.runes_data[rune_type]

        cost = RuneFactory.__cost_function(level)
        max_energy_bonus_level_scaling = data['max_energy_bonus_level_scaling']
        max_energy_bonus = max_energy_bonus_level_scaling[level - 1]

        if activation_rune_effect_name is None:
            activation_rune_effect_appearance_rate = data['activation_rune_effect_appearance_rate']
            activation_rune_effect_name = RuneFactory.get_random_activation_rune_effect(activation_rune_effect_appearance_rate)

        activation_rune_effect, activation_time, energy_cost = RuneFactory.create_rune_effect(activation_rune_effect_name, level)

        return rune_class(level, cost, max_energy_bonus, activation_time, energy_cost, activation_rune_effect)

    activation_rune_effect_map = {
        'cause_damage_on_activation': CauseDamageOnActivation,
        'restore_life_on_activation': RestoreLifeOnActivation,
        'restore_energy_on_activation': RestoreEnergyOnActivation
    }

    @staticmethod
    def create_rune_effect(rune_effect: str, level):
        rune_effect_data = RuneFactory.rune_effects_level_scaling[rune_effect][level - 1]
        energy_cost = rune_effect_data['energy_cost']
        activation_time = rune_effect_data['activation_time']

        match rune_effect:
            case 'cause_damage_on_activation':
                damage_range = rune_effect_data['damage_range']
                effect = CauseDamageOnActivation(random.randint(*damage_range))

            case 'restore_life_on_activation':
                life_restored_range = rune_effect_data['life_restored_range']
                effect = RestoreLifeOnActivation(random.randint(*life_restored_range))

            case 'restore_energy_on_activation':
                energy_restored_range = rune_effect_data['energy_restored_range']
                effect = RestoreEnergyOnActivation(random.randint(*energy_restored_range))

        return effect, activation_time, energy_cost

    @staticmethod
    def get_random_activation_rune_effect(activation_rune_effect_appearance_rate):
        effects = list(activation_rune_effect_appearance_rate.keys())
        weights = list(activation_rune_effect_appearance_rate.values())
        
        chosen_effect = random.choices(effects, weights, k=1)[0]
        
        return chosen_effect
