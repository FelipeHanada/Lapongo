from .combat_stats_frame import StatsFrame


class EnemyStatsFrame(StatsFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs, flipped=True)
        self.set_rect(self.get_rect().move(380, 136))
        