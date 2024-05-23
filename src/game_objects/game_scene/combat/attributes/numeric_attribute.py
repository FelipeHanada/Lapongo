class NumericAttribute:
    def __init__(self, base_value: float):
        self._base_value: float = base_value
        self._flat_bonus: float = 0
        self._percent_bonus: float = 0

    def get_base_value(self) -> float:
        return self._base_value

    def set_base_value(self, base_value: float):
        self._base_value = base_value

    def get_value(self, apply_flat_bonus: bool = True, apply_percent_bonus: bool = True) -> float:
        value = self._base_value + (self._flat_bonus if apply_flat_bonus else 0)
        return  value + (value * self._percent_bonus / 100 if apply_percent_bonus else 0)
    
    def get_flat_bonus(self) -> float:
        return self._flat_bonus
    
    def add_flat_bonus(self, flat_bonus: float):
        self._flat_bonus += flat_bonus
    
    def get_percent_bonus(self) -> float:
        return self._percent_bonus
    
    def add_percent_bonus(self, percent_bonus: float):
        self._percent_bonus += percent_bonus

    def reset_bonuses(self):
        self._flat_bonus = 0
        self._percent_bonus = 0
