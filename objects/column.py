import random
import pygame.sprite
import assets
import configs
from layer import Layer


class Column(pygame.sprite.Sprite):
    def __init__(self, *groups):
        # Xác định lớp cho chướng ngại vật, giúp quản lý thứ tự hiển thị
        self._layer = Layer.OBSTACLE

        # Khoảng cách giữa ống trên và ống dưới
        self.gap = 30

        # Tải sprite cho ống (pipe) từ tài nguyên
        self.sprite = assets.get_sprite("pipe")
        # Lấy kích thước của sprite (chiều rộng và chiều cao)
        self.sprite_rect = self.sprite.get_rect()

        # Đặt ống dưới bằng sprite đã tải
        self.pipe_bottom = self.sprite
        # Đặt vị trí cho ống dưới, nằm dưới ống trên với khoảng cách là self.gap
        self.pipe_bottom_rect = self.pipe_bottom.get_rect(topleft=(0, self.sprite_rect.height + self.gap))

        # Tạo ống trên bằng cách đảo ngược sprite
        self.pipe_top = pygame.transform.flip(self.sprite, False, True)
        # Đặt vị trí cho ống trên tại điểm (0, 0)
        self.pipe_top_rect = self.pipe_top.get_rect(topleft=(0, 0))

        # Tạo một bề mặt mới cho toàn bộ column, bao gồm cả ống trên và dưới
        self.image = pygame.surface.Surface(
            (self.sprite_rect.width, self.sprite_rect.height * 2 + self.gap),
            pygame.SRCALPHA
        )
        # Vẽ ống dưới lên bề mặt
        self.image.blit(self.pipe_bottom, self.pipe_bottom_rect)
        # Vẽ ống trên lên bề mặt
        self.image.blit(self.pipe_top, self.pipe_top_rect)

        # Lấy chiều cao của sprite mặt đất để xác định khoảng y hợp lệ cho column
        sprite_floor_height = assets.get_sprite("floor").get_rect().height
        # Thiết lập giới hạn tối thiểu và tối đa cho tọa độ y của column
        min_y = 100
        max_y = configs.SCREEN_HEIGHT - sprite_floor_height - 100

        # Đặt vị trí ban đầu cho column bên phải màn hình, chọn y ngẫu nhiên trong khoảng hợp lệ
        self.rect = self.image.get_rect(midleft=(configs.SCREEN_WIDTH, random.uniform(min_y, max_y)))

        # Tạo mặt nạ từ hình ảnh để xử lý va chạm
        self.mask = pygame.mask.from_surface(self.image)

        # Biến để theo dõi xem column đã được nhân vật vượt qua chưa
        self.passed = False

        # Khởi tạo đối tượng sprite và thêm nó vào các nhóm (groups) đã cho
        super().__init__(*groups)

    def update(self):
        # Di chuyển column sang trái với tốc độ 2 pixel mỗi khung hình
        self.rect.x -= 2

        # Kiểm tra nếu column ra ngoài màn hình bên trái
        if self.rect.right <= 0:
            # Nếu ra ngoài, xóa đối tượng này khỏi sprite group
            self.kill()

    def is_passed(self):
        # Kiểm tra xem column đã được nhân vật vượt qua chưa
        if self.rect.x < 50 and not self.passed:
            # Nếu nhân vật đã vượt qua column, đánh dấu là đã vượt qua
            self.passed = True
            return True  # Trả về True để cho biết đã vượt qua
        return False  # Nếu chưa vượt qua, trả về False