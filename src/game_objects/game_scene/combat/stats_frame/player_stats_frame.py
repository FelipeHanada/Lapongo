from .combat_stats_frame import StatsFrame


class PlayerStatsFrame(StatsFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_rect(self.get_rect().move(12, 136))
        