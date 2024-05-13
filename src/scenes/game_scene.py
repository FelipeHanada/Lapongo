from pgframework import *
from src.game_objects.game_scene.background import GameSceneBackground
from src.game_objects.game_scene.player import GameScenePlayer

class GameScene(AbstractScene):
    def __init__(self, game: Game):
        AbstractScene.__init__(self, game, (255, 255, 255))

        self.add_scene_game_object(GameSceneBackground, priority=0)
        self.add_scene_game_object(GameScenePlayer, priority=1)
