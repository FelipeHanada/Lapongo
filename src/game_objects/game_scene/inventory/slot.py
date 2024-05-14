from pgframework import *


class Slot(AbstractGameObject):
    def __init__(self, *args, show_debug=False, **kwargs):
        AbstractGameObject.__init__(self, *args, **kwargs)
        self._item = None
        self._show_debug = show_debug

    def draw_callback(self) -> None:
        if self._show_debug:
            rect = self.get_absolute_rect()
            surface = pygame.Surface(rect.size)
            surface.fill((255, 0, 0))
            surface.set_alpha(128)
            self.get_display_handler().draw(surface, rect.topleft)

    def set_item(self, item: AbstractGameObject):
        self._item = item
        self.add_child_game_object(item)
    
    def get_item(self):
        return self._item
    
    def remove_item(self):
        item = self._item
        self._item = None
        self.remove_child_game_object(self._item)
        return item
