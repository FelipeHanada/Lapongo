from pgframework import *
import pygame
from src.main_menu.game_objects.background import MainMenuBackground
from src.main_menu.game_objects.title_sign import MainMenuTitleSign


class MainMenuScene(AbstractScene):
    def __init__(self, game: Game):
        AbstractScene.__init__(self, game, (255, 255, 255))

        self.add_event_callback(pygame.KEYUP, self.close, {'key': pygame.K_ESCAPE})

    def close(self, event):
        self.get_parent_game().stop()


MainMenuScene.add_game_object_factory(MainMenuBackground.get_default_factory(priority=0))
MainMenuScene.add_game_object_factory(MainMenuTitleSign.get_default_factory(priority=1))
