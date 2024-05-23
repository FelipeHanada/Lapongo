from typing import Callable
from ..player import Player
from ..enemy import Enemy
from ..combat_event import CombatEvent


class Fatigue(CombatEvent):
    def __init__(self, player: Player, enemy: Enemy, start_t: int, t_between_ticks: int, fatigue_damage: Callable[[int], int], fatigue_energy_loss: Callable[[int], int]):
        def fatigue_callback(combat_controller: 'CombatController'):
            delta_t = combat_controller.get_t() - start_t

            player.receive_damage(fatigue_damage(delta_t))
            player.consume_energy(fatigue_energy_loss(delta_t))

            enemy.receive_damage(fatigue_damage(delta_t))
            enemy.consume_energy(fatigue_energy_loss(delta_t))

            combat_controller.add_event_after(t_between_ticks, fatigue_callback)

        super().__init__(start_t, fatigue_callback)
