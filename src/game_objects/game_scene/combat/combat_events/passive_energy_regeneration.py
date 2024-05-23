from ..player import Player
from ..enemy import Enemy
from ..combat_event import CombatEvent


class PassiveEnergyRegeneration(CombatEvent):
    def __init__(self, player: Player, enemy: Enemy, t_between_ticks: int):
        def passive_energy_regeneration_callback(combat_controller: 'CombatController'):

            player.restore_energy(player.get_energy_regeneration_rate_attribute().get_value())
            enemy.restore_energy(enemy.get_energy_regeneration_rate_attribute().get_value())

            combat_controller.add_event_after(t_between_ticks, passive_energy_regeneration_callback)

        super().__init__(0, passive_energy_regeneration_callback)
