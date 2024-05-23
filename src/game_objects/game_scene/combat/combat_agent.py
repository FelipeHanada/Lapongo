import pgframework as pgf
from .rune_frame import RuneFrame
from .combat_event import CombatEvent


class CombatAgent(pgf.GameObject):
    def __init__(self, parent: pgf.GameObject, rune_frame: RuneFrame, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self._rune_frame: RuneFrame = rune_frame

        self._base_max_health = 100
        self._max_health = self._base_max_health
        self._health = self._max_health

        self._base_max_energy = 100
        self._max_energy = self._base_max_energy
        self._energy = self._max_energy

        self._energy_depletion_rate = 1
        self._health_depletion_rate = 1

    def get_rune_frame(self):
        return self._rune_frame

    def get_base_max_health(self):
        return self._base_max_health

    def get_max_health(self):
        return self._max_health

    def get_health(self):
        return self._health

    def get_health_depletion_rate(self):
        return self._health_depletion_rate

    def get_base_max_energy(self):
        return self._base_max_energy

    def get_max_energy(self):
        return self._max_energy

    def get_energy(self):
        return self._energy
    
    def get_energy_depletion_rate(self):
        return self._energy_depletion_rate
    
    def set_health(self, health):
        self._health = health

    def set_max_health(self, max_health):
        self._max_health = max_health
    
    def set_energy(self, energy):
        self._energy = energy
    
    def set_max_energy(self, max_energy):
        self._max_energy = max_energy
    
    def restore_health(self, health):
        self._health += health
        if self._health > self._max_health:
            self._health = self._max_health
        
    def receive_damage(self, damage):
        self._health -= damage
        if self._health < 0:
            self._health = 0
        return self._health

    def restore_energy(self, energy):
        self._energy += energy
        if self._energy > self._max_energy:
            self._energy = self._max_energy
    
    def consume_energy(self, energy):
        self._energy -= energy
        if self._energy < 0:
            self._energy = 0
        return self._energy

    def start(self, combat_controller: 'CombatController', other_agent: 'CombatAgent'):
        self._max_health = self._base_max_health
        self._max_energy = self._base_max_energy

        for occupied_rune_slot in self._rune_frame.get_occupied_rune_slots():
            rune = occupied_rune_slot.get_rune()
            rune.start(combat_controller, self, other_agent)

        self._health = self._max_health
        self._energy = self._max_energy
    
    def end(self, combat_controller: 'CombatController', other_agent: 'CombatAgent'):
        for occupied_rune_slot in self._rune_frame.get_occupied_rune_slots():
            rune = occupied_rune_slot.get_rune()
            rune.end(combat_controller, self, other_agent)

    def get_rune_activation_event(self, enemy: 'CombatAgent', low_energy_recovery_time: int) -> CombatEvent:
        def event_activation_event_callback(combat_controller: 'CombatController'):
            recovery_time = low_energy_recovery_time

            slot = self.get_rune_frame().get_random_occupied_rune_slot()
            if slot is not None:
                rune = slot.get_rune()
                
                if rune.get_energy_cost() > self.get_energy():
                    print('Not enough energy')

                else:
                    self.consume_energy(rune.get_energy_cost())
                    activation_callback = rune.get_activation_effect().get_activation_effect().get_callback()
                    activation_callback(combat_controller, self, enemy)
                    recovery_time = rune.get_activation_time()

            combat_controller.add_event_after(recovery_time, event_activation_event_callback)

        return CombatEvent(0, event_activation_event_callback)
