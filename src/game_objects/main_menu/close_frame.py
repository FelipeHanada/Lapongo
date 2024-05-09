from pgframework import *


class MainMenuCloseFrame(AbstractGameObject):
    _sprite_file_path = 'src/assets/sprites/main_menu/close_frame/frame.png'
    _sprite_size = (128, 64)

    def __init__(self, *args, **kwargs):
        AbstractGameObject.__init__(self, *args, **kwargs, rect=pygame.Rect(0, 0, *self._sprite_size))
        
        rect = self.get_rect()
        rect.centerx = self.get_parent_game_object().get_rect().width // 2
        rect.centery = self.get_parent_game_object().get_rect().height // 2
        self.set_rect(rect)

        self.add_component(Sprite2D(self, self._sprite_file_path))

        self.add_child_game_object(CloseFrameButton(self, kwargs['parent_scene'], priority=1))
        

class CloseFrameButton(AbstractGameObject):
    _sprite_file_path = 'src/assets/sprites/main_menu/close_frame/confirm_button.png'
    _sprite_size = (96, 14)

    def __init__(self, parent: AbstractGameObject, scene: AbstractScene, priority: int = 0):
        AbstractGameObject.__init__(self, parent, scene, priority=priority, rect=pygame.Rect(0, 0, *self._sprite_size))
        
        rect = self.get_rect()
        rect.centerx = self.get_parent_game_object().get_rect().width // 2
        rect.bottom = self.get_parent_game_object().get_rect().height - 13
        self.set_rect(rect)

        self.add_component(Sprite2D(self, self._sprite_file_path))

        #self.add_component(MouseListener(self))

    def on_mouse_button_down(self, event: pygame.event.Event):
        self.get_parent_game_object().get_parent_scene().get_parent_game().stop()
