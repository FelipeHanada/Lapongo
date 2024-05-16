import pgframework as pgf


class Rune(pgf.GameObject):
    def __init__(self, sprite_file, *args, **kwargs):
        super().__init__(*args, **kwargs, rect=pgf.PygameRectAdapter(0, 0, 16, 16))

        self.add_child(pgf.components.sprite2d.Sprite2D(self, sprite_file))
