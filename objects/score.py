import pygame.sprite
import assets
import configs
from layer import Layer


class Score(pygame.sprite.Sprite):
    def __init__(self, *groups):
        # Xác định lớp cho điểm số
        self._layer = Layer.UI

        # Khởi tạo giá trị điểm số ban đầu
        self.value = 0

        # Tạo một bề mặt trống cho điểm số
        self.image = pygame.surface.Surface((0, 0), pygame.SRCALPHA)

        # Gọi hàm tạo điểm số
        self.__create()

        # Khởi tạo đối tượng sprite và thêm nó vào các nhóm (groups) đã cho
        super().__init__(*groups)

    def __create(self):
        # Chuyển đổi giá trị điểm số thành chuỗi
        self.str_value = str(self.value)

        # Danh sách để chứa các hình ảnh tương ứng với từng ký tự của điểm số
        self.images = []
        self.width = 0  # Tổng chiều rộng của điểm số

        # Tạo hình ảnh cho từng ký tự của điểm số
        for str_value_char in self.str_value:
            img = assets.get_sprite(str_value_char)  # Lấy sprite cho ký tự
            self.images.append(img)  # Thêm hình ảnh vào danh sách
            self.width += img.get_width()  # Cộng chiều rộng của ký tự vào tổng

        # Chiều cao của điểm số sẽ là chiều cao của ký tự đầu tiên
        self.height = self.images[0].get_height()

        # Tạo một bề mặt mới cho điểm số với kích thước tổng
        self.image = pygame.surface.Surface((self.width, self.height), pygame.SRCALPHA)

        # Đặt vị trí cho hình chữ nhật (rect) của điểm số ở giữa màn hình
        self.rect = self.image.get_rect(center=(configs.SCREEN_WIDTH / 2, 50))

        # Vẽ từng hình ảnh ký tự lên bề mặt
        x = 0
        for img in self.images:
            self.image.blit(img, (x, 0))  # Vẽ hình ảnh ký tự lên bề mặt
            x += img.get_width()  # Cập nhật vị trí x để vẽ ký tự tiếp theo

    def update(self):
        # Cập nhật hình ảnh điểm số mỗi khi update được gọi
        self.__create()