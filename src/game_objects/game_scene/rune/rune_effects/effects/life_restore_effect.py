from ..effect import Effect


class LifeRestoreEffect(Effect):
    def __init__(self, life: int):
        super().__init__(self.restore_life, f'Recupera {life} de vida.')
        self._life = life

    def restore_life(self):
        print(f'recuperou {self._life} de vida.')
