import pgframework as pgf
from .rune_frame import RuneFrame
from .combat_event import CombatEvent
from .attributes.numeric_attribute import NumericAttribute


class CombatAgent(pgf.GameObject):
    def __init__(self, parent: pgf.GameObject, rune_frame: RuneFrame, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self._rune_frame: RuneFrame = rune_frame

        self._max_health = NumericAttribute(100)
        self._current_health = self._max_health.get_value()

        self._max_energy = NumericAttribute(100)
        self._current_energy = self._max_energy.get_value()

        self._energy_regeneration_rate = NumericAttribute(1)
        self._health_regeneration_rate = NumericAttribute(1)

    def get_rune_frame(self):
        return self._rune_frame

    def get_current_health(self) -> float:
        return self._current_health

    def set_current_health(self, health):
        self._current_health = health

    def restore_health(self, health):
        self._current_health += health
        max_health = self._max_health.get_value()
        if self._current_health > max_health:
            self._current_health = max_health
        
    def receive_damage(self, damage):
        self._current_health -= damage
        if self._current_health < 0:
            self._current_health = 0
        return self._current_health

    def get_max_health_attribute(self) -> NumericAttribute:
        return self._max_health

    def get_health_regeneration_rate_attribute(self) -> NumericAttribute:
        return self._health_regeneration_rate

    def get_current_energy(self):
        return self._current_energy
    
    def set_current_energy(self, energy):
        self._current_energy = energy
    
    def restore_energy(self, energy):
        self._current_energy += energy
        max_energy = self._max_energy.get_value()
        if self._current_energy > max_energy:
            self._current_energy = max_energy
    
    def consume_energy(self, energy):
        self._current_energy -= energy
        if self._current_energy < 0:
            self._current_energy = 0
        return self._current_energy
    
    def get_max_energy_attribute(self) -> NumericAttribute:
        return self._max_energy
    
    def get_energy_regeneration_rate_attribute(self) -> NumericAttribute:
        return self._energy_regeneration_rate

    def start(self, combat_controller: 'CombatController', other_agent: 'CombatAgent'):
        self._max_health.reset_bonuses()
        self._max_energy.reset_bonuses()
        self._health_regeneration_rate.reset_bonuses()
        self._energy_regeneration_rate.reset_bonuses()

        for occupied_rune_slot in self._rune_frame.get_occupied_rune_slots():
            rune = occupied_rune_slot.get_rune()
            rune.start(combat_controller, self, other_agent)

        self._current_health = self._max_health.get_value()
        self._current_energy = self._max_energy.get_value()
    
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
                
                if rune.get_energy_cost() > self.get_current_energy():
                    print('Not enough energy')

                else:
                    self.consume_energy(rune.get_energy_cost())
                    activation_callback = rune.get_activation_effect().get_activation_effect().get_callback()
                    activation_callback(combat_controller, self, enemy)
                    recovery_time = rune.get_activation_time()

            combat_controller.add_event_after(recovery_time, event_activation_event_callback)

        return CombatEvent(0, event_activation_event_callback)
