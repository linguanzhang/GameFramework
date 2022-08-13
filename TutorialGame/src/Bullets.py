import pygame
from mlgame.view.view_model import create_rect_view_data


class Bullets(pygame.sprite.Sprite):
    # 初始化
    def __init__(self, is_player: bool, init_pos: tuple):
        super().__init__()
        self._init_pos = init_pos

        self.rect = pygame.Rect(init_pos, (5, 8))
        self._is_player = is_player
        self._y_speed = 10
        if self._is_player:
            self.color ="#00FFFF"
        else:
            self.color ="#FFA500"

    def update(self, *args, **kwargs) -> None:
        if self._is_player:
            self.rect.centery -= self._y_speed
        else:
            self.rect.centery += self._y_speed

    @property
    def game_object_data(self):
        return create_rect_view_data(name="bullets"
                                     , x=self.rect.x
                                     , y=self.rect.y
                                     , width=self.rect.width
                                     , height=self.rect.height
                                     , color=self.color
                                     , angle=0)
