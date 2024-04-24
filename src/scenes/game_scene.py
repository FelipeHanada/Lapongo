from pgframework import *


class GameScene(AbstractScene):
    def __init__(self, game: Game):
        AbstractScene.__init__(self, game, (255, 255, 255))
