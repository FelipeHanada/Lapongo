import pgframework as pgf
from .slot import Slot


class RuneSlot(Slot):
    def __init__(self, *args, rune_inventory_user=None, **kwargs):
        Slot.__init__(self, *args, **kwargs)
        self._rune_inventory_user = rune_inventory_user

        self.mouse_listener = self.add_component(pgf.components.mouse_listener.MouseListener(self, show_debug=True))
        self.mouse_listener.on_press_in_rect(1, self._on_press)
        self.mouse_listener.on_hover(self._on_hover)

    def _on_press(self):
        if self._rune_inventory_user is None:
            return

        if not self._rune_inventory_user.get_holding_rune():
            self._rune_inventory_user.pick_rune(self)

    def _on_hover(self):
        if self._rune_inventory_user is None:
            return

        if self._rune_inventory_user.get_holding_rune() and not self.mouse_listener.get_pressed(1):
            if self.get_item() is not None:
                self._rune_inventory_user.get_last_rune_slot().set_item(self.get_item())
            
            self.set_item(self._rune_inventory_user.get_holding_rune())
            self._rune_inventory_user.drop_rune()
