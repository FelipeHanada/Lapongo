import pgframework as pgf
from .slot import Slot
from ..rune.rune import Rune


class RuneSlot(Slot):
    def __init__(self, *args, rune_inventory_user, **kwargs):
        super().__init__(*args, **kwargs)
        self._rune_inventory_user = rune_inventory_user

        self._description_frame = self.add_child(RuneDescriptionFrame(self, visible=False))

        self.mouse_listener = self.add_child(pgf.components.mouse_listener.MouseListener(self, rect=pgf.PygameRectAdapter(0, 0, *self.get_rect().get_size()), draw_debug_rect=True))
        self.mouse_listener.on_press_in_rect(1, self.on_press)
        self.mouse_listener.on_hover(self.on_hover)
        self.mouse_listener.on_unhover(self.on_mouse_unhover)

    def get_rune(self) -> Rune:
        return self.get_item()

    def place_rune_from_hand(self):
        self.set_item(self._rune_inventory_user.get_holding_rune())
        self._rune_inventory_user.drop_rune()

    def swap_rune_with_hand(self):
        self._rune_inventory_user.get_last_rune_slot().set_item(self.get_item())
        self.place_rune_from_hand()

    def on_press(self):
        if not self._rune_inventory_user.get_holding_rune():
            self._rune_inventory_user.pick_rune(self)

    def on_hover(self):
        if self._rune_inventory_user.get_holding_rune():
            self._description_frame.set_visible(False)

            if not self.mouse_listener.get_pressed(1):
                if self.get_item() is not None:
                    self.swap_rune_with_hand()

                else:
                    self.place_rune_from_hand()

        else:
            self._description_frame.set_visible(True)

    def on_mouse_unhover(self):
        self._description_frame.set_visible(False)

class RuneDescriptionFrame(pgf.GameObject):
    _sprite_file_path = 'src/assets/sprites/game_scene/rune_description_frame.png'
    _font_file_path = 'src/assets/fonts/alagard.ttf'
    
    def __init__(self, rune_slot: RuneSlot, *args, **kwargs):
        super().__init__(rune_slot, *args, **kwargs, rect=pgf.PygameRectAdapter(0, 0, 96, 72))

        self._rune_slot = rune_slot
        self._sprite2d = self.add_child(pgf.components.sprite2d.Sprite2D(self, self._sprite_file_path, draw_absolute=True))
        self._name_label = self.add_child(pgf.game_objects.label.Label(self, '', self._font_file_path, 8, (197, 152, 70), visible=False, draw_absolute=True, rect=pgf.PygameRectAdapter(8, 8, 80, 8), draw_debug_rect=False))
        self._description_text = self.add_child(pgf.game_objects.text.Text(self, '', self._font_file_path, 6, (255, 255, 255), align='justify', align_vertical='center', visible=False, draw_absolute=True, rect=pgf.PygameRectAdapter(8, 20, 80, 44), draw_debug_rect=False))

    def draw_callback(self, renderer: pgf.Renderer) -> None:
        rune = self._rune_slot.get_rune()

        if rune is None:
            self._sprite2d.set_visible(False)
            self._name_label.set_visible(False)
            self._description_text.set_visible(False)
            return

        self._sprite2d.set_visible(True)

        self._name_label.set_visible(True)
        self._name_label.set_text(rune.get_name())

        self._description_text.set_visible(True)
        self._description_text.set_text(rune.get_description())

        rune_absolute_rect = self.get_parent().get_absolute_rect()
        absolute_rect = self.get_absolute_rect().copy()
        render_size = renderer.get_render_size()
        
        if rune_absolute_rect.get_centerx() >= render_size[0] / 2:
            absolute_rect.set_right(rune_absolute_rect.get_left())
        else:
            absolute_rect.set_left(rune_absolute_rect.get_right())

        absolute_rect.set_y((render_size[1] - absolute_rect.get_height()) / (render_size[1] - rune_absolute_rect.get_height()) * rune_absolute_rect.get_y())

        self.set_absolute_rect(absolute_rect)
