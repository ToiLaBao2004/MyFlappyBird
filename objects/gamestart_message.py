import pygame.sprite
import assets
import configs
from layer import Layer


class GameStartMessage(pygame.sprite.Sprite):
    def __init__(self, *groups):
        # Xác định lớp cho thông điệp "Game Start"
        self._layer = Layer.UI

        # Tải sprite cho thông điệp "Game Start" từ tài nguyên
        self.image = assets.get_sprite("message")

        # Đặt vị trí cho thông điệp ở giữa màn hình
        self.rect = self.image.get_rect(center=(configs.SCREEN_WIDTH / 2, configs.SCREEN_HEIGHT / 2))

        # Khởi tạo đối tượng sprite và thêm nó vào các nhóm (groups) đã cho
        super().__init__(*groups)