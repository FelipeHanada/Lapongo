from pgframework import *


class Rune(AbstractGameObject):
    def __init__(self, sprite_file, *args, **kwargs):
        AbstractGameObject.__init__(self, *args, **kwargs, rect=pygame.Rect(0, 0, 16, 16))

        self.add_component(Sprite2D(self, sprite_file))
