from ..player import Player
from ..enemy import Enemy
from ..combat_event import CombatEvent


class PassiveHealthRegeneration(CombatEvent):
    def __init__(self, player: Player, enemy: Enemy, t_between_ticks: int):
        def passive_health_regeneration_callback(combat_controller: 'CombatController'):

            player.restore_health(player.get_health_depletion_rate())
            enemy.restore_health(enemy.get_health_depletion_rate())

            combat_controller.add_event_after(t_between_ticks, passive_health_regeneration_callback)

        super().__init__(0, passive_health_regeneration_callback)
