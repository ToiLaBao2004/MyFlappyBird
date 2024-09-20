import pygame.sprite
import assets
import configs
from layer import Layer


class Floor(pygame.sprite.Sprite):
    def __init__(self, index, *groups):
        # Xác định lớp cho mặt đất
        self._layer = Layer.FLOOR

        # Tải sprite cho mặt đất từ tài nguyên
        self.image = assets.get_sprite("floor")

        # Đặt vị trí cho mặt đất dựa trên chỉ số index
        # bottomleft: căn chỉnh cạnh dưới bên trái của mặt đất với màn hình
        self.rect = self.image.get_rect(bottomleft=(configs.SCREEN_WIDTH * index, configs.SCREEN_HEIGHT))

        # Tạo mặt nạ từ hình ảnh để xử lý va chạm
        self.mask = pygame.mask.from_surface(self.image)

        # Khởi tạo đối tượng sprite và thêm nó vào các nhóm (groups) đã cho
        super().__init__(*groups)

    def update(self):
        # Di chuyển mặt đất sang trái với tốc độ 2 pixel mỗi khung hình
        self.rect.x -= 2

        # Kiểm tra nếu mặt đất ra ngoài màn hình bên trái
        if self.rect.right <= 0:
            # Nếu ra ngoài, đặt lại vị trí sang bên phải màn hình
            self.rect.x = configs.SCREEN_WIDTH