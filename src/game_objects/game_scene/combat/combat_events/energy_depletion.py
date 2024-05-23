from ..player import Player
from ..enemy import Enemy
from ..combat_event import CombatEvent


class EnergyDepletion(CombatEvent):
    def __init__(self, player: Player, enemy: Enemy, t_between_ticks: int):
        def energy_depletion_callback(combat_controller: 'CombatController'):

            player.restore_energy(player.get_energy_depletion_rate())
            enemy.restore_energy(enemy.get_energy_depletion_rate())

            combat_controller.add_event_after(t_between_ticks, energy_depletion_callback)

        super().__init__(0, energy_depletion_callback)
