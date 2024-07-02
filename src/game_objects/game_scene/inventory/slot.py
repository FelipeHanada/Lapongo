import pgframework as pgf


class Slot(pgf.GameObject):
    def __init__(self, *args, show_debug=False, **kwargs):
        super().__init__(*args, **kwargs)
        self._item = None
        self._show_debug = show_debug

    def draw_callback(self, renderer: pgf.Renderer) -> None:
        if self._show_debug:
            rect = self.get_absolute_rect()
            surface = pgf.PygameSurfaceAdapter(rect.size, pgf.surface_flags['SRCALPHA'])
            surface.fill((255, 0, 0))
            surface.set_alpha(128)
            renderer.draw_surface(surface, rect.get_position())

    def set_item(self, item: pgf.GameObject):
        self._item = item
        item.set_parent(self)

    def get_item(self):
        return self._item
    
    def is_empty(self):
        return self._item is None
    
    def remove_item(self):
        if self._item is not None:
            self.remove_child(self._item)

        self._item = None
