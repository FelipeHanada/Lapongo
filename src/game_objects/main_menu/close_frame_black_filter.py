from pgframework import *


class MainMenuCloseFrameBlackFilter(AbstractGameObject):
    def __init__(self, *args, **kwargs):
        AbstractGameObject.__init__(self, *args, **kwargs, rect=PygameRectAdapter(0, 0, 480, 270))

        image = PygameSurfaceAdapter((480, 270), surface_flags['SRCALPHA'])
        image.fill((0, 0, 0, 128))
        self.add_component(Sprite2D(self, image))
