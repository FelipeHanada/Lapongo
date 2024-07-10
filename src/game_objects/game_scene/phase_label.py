import pgframework as pgf


class PhaseLabel(pgf.game_objects.text.Text):
    def __init__(self, parent: 'GameObject', *args, **kwargs):
        super().__init__(parent, '', 'src/assets/fonts/alagard.ttf', 10, (255, 255, 255), *args, **kwargs, align='center')
        rect = self.get_rect()
        rect.set_centerx(self.get_parent().get_rect().get_width() // 2)
        self.set_rect(rect)

        self._current_round = 0
        self._current_phase = 'compras'
        self.set_text(self.get_label(1, 'compras'))

    @staticmethod
    def get_label(round, phase):
        return f'<color rgb="(187, 152, 70)">Rodada {round}</color><br>Fase de {phase.capitalize()}'

    def set_current_round(self, round):
        self._current_round = round
        self.set_text(self.get_label(self._current_round, self._current_phase))

    def set_phase(self, phase):
        self._current_phase = phase
        self.set_text(self.get_label(self._current_round, self._current_phase))
