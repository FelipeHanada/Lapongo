import pgframework as pgf


class CombatAgent(pgf.GameObject):
    def __init__(self, *args, **kwargs):
        pgf.GameObject.__init__(self, *args, **kwargs)

        self._life = 100
        self._max_life = 100

        self._energy = 100
        self._max_energy = 100
    
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
