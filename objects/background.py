import pygame.sprite
import assets
import configs
from layer import Layer


class Background(pygame.sprite.Sprite):
    def __init__(self, index, *groups):
        # Xác định lớp cho background
        self._layer = Layer.BACKGROUND

        # Lấy hình ảnh background từ assets
        self.image = assets.get_sprite("background")

        # Đặt vị trí ban đầu cho background dựa trên chỉ số index
        self.rect = self.image.get_rect(topleft=(configs.SCREEN_WIDTH * index, 0))

        # Khởi tạo lớp Sprite và thêm đối tượng vào các nhóm (groups) đã cho
        super().__init__(*groups)

    def update(self):
        # Di chuyển background sang trái
        self.rect.x -= 1

        # Nếu background ra ngoài màn hình bên trái, đặt lại vị trí sang bên phải màn hình
        if self.rect.right <= 0:
            self.rect.x = configs.SCREEN_WIDTH