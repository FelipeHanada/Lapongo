from ..rune_effect import RuneEffect


class LeavesPathEffect(RuneEffect):
    description = '1 runa(s) - ganha 5% a mais de folhas ao final do combate<br>'
    description += '2 runa(s) - ganha 10% a mais de folhas ao final do combate<br>'
    description += '3 runa(s) - ganha 15% a mais de folhas ao final do combate'

    def __init__(self):
        super().__init__(self.description)
