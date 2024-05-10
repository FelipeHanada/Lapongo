from pgframework import *
import pygame
from src.game_objects.main_menu.background import MainMenuBackground
from src.game_objects.main_menu.title_sign import MainMenuTitleSign
from src.game_objects.main_menu.play_button import MainMenuPlayButton, MainMenuPlayButtonOnClick
from src.game_objects.main_menu.close_frame_black_filter import MainMenuCloseFrameBlackFilter
from src.game_objects.main_menu.close_frame import MainMenuCloseFrame


class MainMenuScene(AbstractScene):
    def __init__(self, game: Game):
        AbstractScene.__init__(self, game, (255, 255, 255))

        self.add_event_callback(pygame.KEYUP, self._on_escape, {'key': pygame.K_ESCAPE})

        self._background = self.add_scene_game_object(MainMenuBackground, priority=0)
        self._title_sign = self.add_scene_game_object(MainMenuTitleSign, priority=1)
        self._play_button = self.add_scene_game_object(MainMenuPlayButton, priority=1)

        self._close_frame_black_filter: 'AbstractGameObject' = self.add_scene_game_object(MainMenuCloseFrameBlackFilter, priority=2, enabled=False, visible=False)
        self._close_frame: 'AbstractGameObject' = self.add_scene_game_object(MainMenuCloseFrame, priority=3, enabled=False, visible=False)

        self.add_message_callback(MainMenuPlayButtonOnClick, self.on_play_button_pressed)

    def on_play_button_pressed(self, message: MainMenuPlayButtonOnClick):
        self.get_parent_game().change_scene('game')

    def set_open_close_frame(self, opened: bool):
        self.send_message(
            SetEnabledMessage(self.get_scene_graph_root(), not opened),
            SendMessageTargetEnum.DESCENDANTS,
            target_class=MainMenuCloseFrame,
            target_class_exclusion=True
        )

        self._close_frame.set_opened(opened)

        self._close_frame_black_filter.set_enabled(opened)
        self._close_frame_black_filter.set_visible(opened)

    def _on_escape(self, event: pygame.event.Event):
        self.set_open_close_frame(not self._close_frame.get_enabled())
