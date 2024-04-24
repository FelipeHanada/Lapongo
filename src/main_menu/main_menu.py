from pgframework import *
import pygame
from .game_objects.background import MainMenuBackground
from .game_objects.title_sign import MainMenuTitleSign
from .game_objects.play_button import MainMenuPlayButton

class MainMenuScene(AbstractScene):
    def __init__(self, game: Game):
        AbstractScene.__init__(self, game, (255, 255, 255))
        self.add_event_callback(pygame.KEYUP, self.close, {'key': pygame.K_ESCAPE})

    def close(self, event):
        self.get_parent_game().stop()


MainMenuScene.add_game_object_factory(MainMenuBackground.get_default_factory(priority=0))
MainMenuScene.add_game_object_factory(MainMenuTitleSign.get_default_factory(priority=1))
MainMenuScene.add_game_object_factory(MainMenuPlayButton.get_default_factory(priority=1))
