import pygame
from pgframework import *


class MainMenuCloseFrameBlackFilter(AbstractGameObject):
    def __init__(self, *args, **kwargs):
        AbstractGameObject.__init__(self, *args, **kwargs, rect=pygame.Rect(0, 0, 480, 270))

        image = pygame.Surface((480, 270), pygame.SRCALPHA)
        image.fill((0, 0, 0, 128))
        self.add_component(Sprite2D(self, image))
