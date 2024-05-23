import pgframework as pgf
from .rune_frame import RuneFrame
from .combat_event import CombatEvent


class CombatAgent(pgf.GameObject):
    def __init__(self, parent: pgf.GameObject, rune_frame: RuneFrame, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self._rune_frame: RuneFrame = rune_frame

        self._life = 100
        self._max_life = 100

        self._energy = 100
        self._max_energy = 100
    
    def get_rune_frame(self):
        return self._rune_frame

    def get_life(self):
        return self._life
    
    def get_max_life(self):
        return self._max_life
    
    def get_energy(self):
        return self._energy
    
    def get_max_energy(self):
        return self._max_energy
    
    def set_life(self, life):
        self._life = life

    def set_max_life(self, max_life):
        self._max_life = max_life
    
    def set_energy(self, energy):
        self._energy = energy
    
    def set_max_energy(self, max_energy):
        self._max_energy = max_energy
    
    def restore_life(self, life):
        self._life += life
        if self._life > self._max_life:
            self._life = self._max_life
        
    def receive_damage(self, damage):
        self._life -= damage
        if self._life < 0:
            self._life = 0
        return self._life

    def restore_energy(self, energy):
        self._energy += energy
        if self._energy > self._max_energy:
            self._energy = self._max_energy
    
    def consume_energy(self, energy):
        self._energy -= energy
        if self._energy < 0:
            self._energy = 0
        return self._energy

    def start(self):
        self._life = self._max_life
        self._energy = self._max_energy

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
