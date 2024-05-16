import pgframework as pgf


class GameSceneRuneInventoryUser(pgf.AbstractGameObject):
    def __init__(self, *args, **kwargs):
        pgf.AbstractGameObject.__init__(self, *args, **kwargs)

        self._holding_rune = None
        self._last_rune_slot = None

        self._mouse_listener = self.add_component(pgf.components.mouse_listener.MouseListener(self, rect=pgf.PygameRectAdapter(0, 0, 480, 270)))
        self._mouse_listener.on_mouse_motion(self._on_mouse_motion)
        self._mouse_listener.on_release(1, self._on_release)

    def drop_rune(self):
        if self._holding_rune:
            self.remove_child_game_object(self._holding_rune)
            self._holding_rune = None
            
            pgf.set_mouse_visible(True)

    def pick_rune(self, rune_slot: 'RuneSlot'):
        self._last_rune_slot = rune_slot
        self._holding_rune = rune_slot.remove_item()

        if self._holding_rune:
            self.add_child_game_object(self._holding_rune)
            pgf.set_mouse_visible(False)
        
        self._on_mouse_motion(pgf.get_mouse_pos())

    def get_holding_rune(self):
        return self._holding_rune
    
    def get_last_rune_slot(self):
        return self._last_rune_slot

    def _on_mouse_motion(self, pos):
        if self._holding_rune:
            rect = self.get_display_handler().convert_rect_real_to_render(pgf.PygameRectAdapter(*pos, 0, 0))
            rect.move_ip(
                -self._holding_rune.get_rect().get_width() // 2,
                -self._holding_rune.get_rect().get_height() // 2
            )
            self.set_rect(rect)

    def _on_release(self):
        if self._holding_rune:
            self._last_rune_slot.set_item(self._holding_rune)
            self.drop_rune()
