from .rune_effect import RuneEffect


class CauseDamageEffect(RuneEffect):
    def __init__(self, damage: int):
        super().__init__(self.cause_damage, f'Causa {damage} de dano.')
        self._damage = damage

    def cause_damage(self):
        print(f'causou {self._damage} de dano.')
