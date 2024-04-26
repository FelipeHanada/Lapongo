from pgframework import *
import pygame
from src.game_objects.main_menu.background import MainMenuBackground
from src.game_objects.main_menu.title_sign import MainMenuTitleSign
from src.game_objects.main_menu.play_button import MainMenuPlayButton, MainMenuPlayButtonOnClick
from src.game_objects.main_menu.close_frame import MainMenuCloseFrame

class MainMenuScene(AbstractScene):
    def __init__(self, game: Game):
        AbstractScene.__init__(self, game, (255, 255, 255))

        self.add_event_callback(pygame.KEYUP, self._on_escape, {'key': pygame.K_ESCAPE})

        self.add_game_object(MainMenuBackground.create_scene_game_object(self, priority=0))
        self.add_game_object(MainMenuTitleSign.create_scene_game_object(self, priority=1))
        self.add_game_object(MainMenuPlayButton.create_scene_game_object(self, priority=1))

        self._close_frame = MainMenuCloseFrame.create_scene_game_object(self, priority=2, enabled=False, visible=False)
        self.add_game_object(self._close_frame)

        self.add_message_callback(MainMenuPlayButtonOnClick, self.on_play_button_pressed)

    def on_play_button_pressed(self, message: MainMenuPlayButtonOnClick):
        self.get_parent_game().change_scene('game')

    def _on_escape(self, event: pygame.event.Event):
        self._close_frame.set_enabled(not self._close_frame.get_enabled())
        self._close_frame.set_visible(not self._close_frame.get_visible())
