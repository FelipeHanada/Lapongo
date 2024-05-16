import pgframework as pgf
from src.scenes.main_menu_scene import MainMenuScene
from src.scenes.game_scene import GameScene


class MainGame(pgf.Game):
    def __init__(self):
        display = pgf.display_adapter.create_display((1440, 810), 'Lapongo')
        #display = pgf.display_adapter.create_display(None, 'Lapongo', flags=pgf.display_flags['FULLSCREEN'])

        super().__init__(
            pgf.display_handler.DisplayHandler(
                display=display,
                aspect_ratio=(16, 9),
                render_size=(480, 270)
            ),
            tick_rate=60
        )

        self.add_scene('main_menu', pgf.DefaultSceneFactory(MainMenuScene, self))
        self.add_scene('game', pgf.DefaultSceneFactory(GameScene, self))


if __name__ == '__main__':
    MainGame().run(first_scene='main_menu')
