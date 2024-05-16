import pgframework as pgf


class MainMenuCloseFrameBlackFilter(pgf.GameObject):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs, rect=pgf.PygameRectAdapter(0, 0, 480, 270))

        image = pgf.PygameSurfaceAdapter((480, 270), pgf.surface_flags['SRCALPHA'])
        image.fill((0, 0, 0, 128))
        self.add_child(pgf.components.sprite2d.Sprite2D(self, image))
