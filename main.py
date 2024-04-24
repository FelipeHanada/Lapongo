from pgframework import *
import pygame
from src.scenes.main_menu_scene import MainMenuScene
from src.scenes.game_scene import GameScene


class MainGame(Game):
    def __init__(self):
        self.display = pygame.display.set_mode((1920, 1080))

        super().__init__(
            DisplayHandler(
                display=self.display,
                aspect_ratio=(16, 9),
                render_size=(480, 270)
            ),
            tick_rate=60
        )

        self.add_scene('main_menu', MainMenuScene.get_default_factory(self))
        self.add_scene('game', GameScene.get_default_factory(self))

if __name__ == '__main__':
    MainGame().run(first_scene='main_menu')
