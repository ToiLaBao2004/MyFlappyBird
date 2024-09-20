import pygame

import assets
import configs
from objects.background import Background
from objects.bird import Bird
from objects.column import Column
from objects.floor import Floor
from objects.gameover_message import GameOverMessage
from objects.gamestart_message import GameStartMessage
from objects.score import Score

# Khởi tạo Pygame
pygame.init()

# Tạo cửa sổ trò chơi với kích thước được chỉ định
screen = pygame.display.set_mode((configs.SCREEN_WIDTH, configs.SCREEN_HEIGHT))

# Đặt tiêu đề cho cửa sổ trò chơi
pygame.display.set_caption("Flappy Bird Game v1.0.2")

# Tải biểu tượng cho cửa sổ trò chơi
img = pygame.image.load('assets/icons/red_bird.png')
pygame.display.set_icon(img)

# Thiết lập đồng hồ để điều chỉnh tốc độ khung hình
clock = pygame.time.Clock()

# Tạo sự kiện tùy chỉnh cho việc tạo cột
column_create_event = pygame.USEREVENT

# Biến trạng thái cho trò chơi
running = True
gameover = False
gamestarted = False

# Tải các sprite và âm thanh từ tài nguyên
assets.load_sprites()
assets.load_audios()

# Tạo một nhóm sprite để quản lý các đối tượng
sprites = pygame.sprite.LayeredUpdates()


def create_sprites():
    # Tạo các đối tượng nền, mặt đất, chim, và thông điệp bắt đầu
    Background(0, sprites)
    Background(1, sprites)
    Floor(0, sprites)
    Floor(1, sprites)

    return Bird(sprites), GameStartMessage(sprites), Score(sprites)


# Khởi tạo các đối tượng chim, thông điệp bắt đầu, và điểm số
bird, game_start_message, score = create_sprites()

# Vòng lặp chính của trò chơi
while running:
    for event in pygame.event.get():
        # Kiểm tra xem có yêu cầu thoát không
        if event.type == pygame.QUIT:
            running = False

        # Kiểm tra sự kiện tạo cột
        if event.type == column_create_event:
            Column(sprites)

        # Xử lý sự kiện nhấn phím và nhấn chuột
        if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
            # Bắt đầu trò chơi khi nhấn phím cách hoặc click chuột, nếu chưa bắt đầu
            if not gamestarted and not gameover:
                gamestarted = True
                game_start_message.kill()  # Xóa thông điệp bắt đầu
                pygame.time.set_timer(column_create_event, 1500)  # Tạo cột mới mỗi 1500ms

            # Đặt lại trò chơi khi nhấn phím ESC hoặc click chuột trong trạng thái game over
            if gameover:
                gameover = False
                gamestarted = False
                sprites.empty()  # Xóa tất cả sprite
                bird, game_start_message, score = create_sprites()  # Tạo lại các đối tượng

            # Nếu trò chơi đang chạy, xử lý sự kiện cho chim
            if gamestarted and not gameover:
                bird.handle_event(event)

    # Làm sạch màn hình
    screen.fill(0)

    # Vẽ tất cả các sprite lên màn hình
    sprites.draw(screen)

    # Cập nhật các sprite nếu trò chơi đã bắt đầu và chưa kết thúc
    if gamestarted and not gameover:
        sprites.update()

    # Kiểm tra va chạm giữa chim và các đối tượng khác
    if bird.check_collision(sprites) and not gameover:
        gameover = True  # Đánh dấu trò chơi đã kết thúc
        gamestarted = False
        GameOverMessage(sprites)  # Hiển thị thông điệp kết thúc
        pygame.time.set_timer(column_create_event, 0)  # Dừng việc tạo cột mới
        assets.play_audio("hit")  # Phát âm thanh va chạm

    # Cập nhật điểm số khi chim đã vượt qua cột
    for sprite in sprites:
        if type(sprite) is Column and sprite.is_passed():
            score.value += 1  # Tăng điểm
            assets.play_audio("point")  # Phát âm thanh ghi điểm

    # Cập nhật màn hình
    pygame.display.flip()

    # Điều chỉnh tốc độ khung hình theo FPS
    clock.tick(configs.FPS)

# Thoát Pygame khi trò chơi kết thúc
pygame.quit()