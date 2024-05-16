import pgframework as pgf


class MainMenuCloseFrameBlackFilter(pgf.AbstractGameObject):
    def __init__(self, *args, **kwargs):
        pgf.AbstractGameObject.__init__(self, *args, **kwargs, rect=pgf.PygameRectAdapter(0, 0, 480, 270))

        image = pgf.PygameSurfaceAdapter((480, 270), pgf.surface_flags['SRCALPHA'])
        image.fill((0, 0, 0, 128))
        self.add_component(pgf.components.sprite2d.Sprite2D(self, image))
