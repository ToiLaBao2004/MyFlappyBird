import pygame.sprite
import assets
import configs
from layer import Layer
from objects.column import Column
from objects.floor import Floor


class Bird(pygame.sprite.Sprite):
    def __init__(self, *groups):
        # Xác định lớp cho chim
        self._layer = Layer.PLAYER

        # Tải các hình ảnh cho chim ở các trạng thái khác nhau
        self.images = [
            assets.get_sprite("redbird-upflap"),
            assets.get_sprite("redbird-midflap"),
            assets.get_sprite("redbird-downflap")
        ]

        # Đặt hình ảnh ban đầu cho chim
        self.image = self.images[0]

        # Đặt vị trí ban đầu cho chim
        self.rect = self.image.get_rect(topleft=(-50, 50))

        # Tạo mặt nạ từ hình ảnh để xử lý va chạm
        self.mask = pygame.mask.from_surface(self.image)

        # Khởi tạo biến để theo dõi tốc độ bay (flap)
        self.flap = 0

        # Khởi tạo đối tượng sprite và thêm nó vào các nhóm (groups) đã cho
        super().__init__(*groups)

    def update(self):
        # Thay đổi hình ảnh chim để tạo hiệu ứng vỗ cánh
        self.images.insert(0, self.images.pop())  # Đưa hình ảnh đầu tiên ra cuối danh sách
        self.image = self.images[0]  # Cập nhật hình ảnh hiện tại

        # Cập nhật tốc độ bay và vị trí y của chim
        self.flap += configs.GRAVITY  # Thêm trọng lực vào tốc độ bay
        self.rect.y += self.flap  # Cập nhật vị trí y của chim

        # Đưa chim vào màn hình nếu nó nằm ngoài lề trái
        if self.rect.x < 50:
            self.rect.x += 3  # Di chuyển chim về phía phải

    def handle_event(self, event):
        # Xử lý sự kiện khi người chơi nhấn phím cách
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            self.flap = 0  # Đặt tốc độ bay về 0
            self.flap -= 6  # Tăng tốc độ bay lên
            assets.play_audio("wing")  # Phát âm thanh vỗ cánh
        elif event.type == pygame.MOUSEBUTTONDOWN:  # Xử lý nhấn chuột
            self.flap = 0
            self.flap -= 6
            assets.play_audio("wing")

    def check_collision(self, sprites):
        # Kiểm tra va chạm giữa chim và các sprite khác
        for sprite in sprites:
            # Kiểm tra xem sprite có phải là Column hoặc Floor và có va chạm với chim không
            if ((type(sprite) is Column or type(sprite) is Floor) and
                    sprite.mask.overlap(self.mask, (self.rect.x - sprite.rect.x, self.rect.y - sprite.rect.y)) or
                    self.rect.bottom < 0):  # Kiểm tra nếu chim ra khỏi màn hình trên
                return True  # Có va chạm
        return False  # Không có va chạm