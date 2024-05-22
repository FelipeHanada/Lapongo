import pgframework as pgf
from ..combat_agent import CombatAgent


class StatsFrame(pgf.GameObject):
    _stats_frame_sprite_file_path = 'src/assets/sprites/game_scene/combat/stats_frame.png'
    _health_bar_sprite_file_path = 'src/assets/sprites/game_scene/combat/health_bar.png'
    _energy_bar_sprite_file_path = 'src/assets/sprites/game_scene/combat/energy_bar.png'

    _health_bar_rect = pgf.PygameRectAdapter(3, 5, 64, 8)
    _health_bar_label_rect = pgf.PygameRectAdapter(69, 5, 16, 8)

    _energy_bar_rect = pgf.PygameRectAdapter(3, 19, 64, 8)
    _energy_bar_label_rect = pgf.PygameRectAdapter(69, 19, 16, 8)

    def __init__(self, parent: pgf.GameObject, combat_agent: CombatAgent, *args, fliped: bool = False, **kwargs):
        super().__init__(parent, *args, **kwargs, rect=pgf.PygameRectAdapter(0, 0, 88, 32))

        self._combat_agent = combat_agent

        self._stats_frame_surface = pgf.PygameSurfaceAdapter.from_image(self._stats_frame_sprite_file_path)

        self._health_bar_surface = pgf.PygameSurfaceAdapter.from_image(self._health_bar_sprite_file_path)
        self._energy_bar_surface = pgf.PygameSurfaceAdapter.from_image(self._energy_bar_sprite_file_path)

        self._sprite2d = self.add_child(pgf.components.sprite2d.Sprite2D(self, self._stats_frame_surface))

    def update_callback(self, delta_time: float) -> None:
        surface = self._stats_frame_surface.copy()

        health_percentage = self._combat_agent.get_life() / self._combat_agent.get_max_life()
        health_bar_width = 2 + round((self._health_bar_surface.get_width() - 2) * health_percentage)
        health_bar = pgf.PygameSurfaceAdapter((health_bar_width, self._health_bar_surface.get_height()), pgf.surface_flags['SRCALPHA'])
        health_bar.blit(self._health_bar_surface, (0, 0))

        energy_percentage = self._combat_agent.get_energy() / self._combat_agent.get_max_energy()
        energy_bar_width = 2 + round((self._energy_bar_surface.get_width() - 2) * energy_percentage)
        energy_bar = pgf.PygameSurfaceAdapter((energy_bar_width, self._energy_bar_surface.get_height()), pgf.surface_flags['SRCALPHA'])
        energy_bar.blit(self._energy_bar_surface, (0, 0))

        surface.blit(health_bar, self._health_bar_rect)
        surface.blit(energy_bar, self._energy_bar_rect)
        self._sprite2d.set_image(surface)