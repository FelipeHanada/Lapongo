from pgframework import *
import pygame
from src.game_objects.main_menu.background import MainMenuBackground
from src.game_objects.main_menu.title_sign import MainMenuTitleSign
from src.game_objects.main_menu.play_button import MainMenuPlayButton


class MainMenuScene(AbstractScene):
    def __init__(self, game: Game):
        AbstractScene.__init__(self, game, (255, 255, 255))

        self.add_event_callback(pygame.KEYUP, self.close, {'key': pygame.K_ESCAPE})

        self.add_game_object(MainMenuBackground.create__scene_game_object(self, priority=0))
        self.add_game_object(MainMenuTitleSign.create__scene_game_object(self, priority=1))
        self.add_game_object(MainMenuPlayButton.create__scene_game_object(self, priority=1))

    def close(self, event):
        self.get_parent_game().stop()
