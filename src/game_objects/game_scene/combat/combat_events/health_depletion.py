from ..player import Player
from ..enemy import Enemy
from ..combat_event import CombatEvent


class HealthDepletion(CombatEvent):
    def __init__(self, player: Player, enemy: Enemy, t_between_ticks: int):
        def health_depletion_callback(combat_controller: 'CombatController'):

            player.restore_health(player.get_health_depletion_rate())
            enemy.restore_health(enemy.get_health_depletion_rate())

            combat_controller.add_event_after(t_between_ticks, health_depletion_callback)

        super().__init__(0, health_depletion_callback)
