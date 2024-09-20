import os
import pygame

# Dictionary chứa các hình ảnh (sprites)
sprites = {}

# Dictionary chứa các bản âm thanh
audios = {}

# Load toàn bộ hình ảnh (sprites) từ assets//sprites
def load_sprites():
    path = os.path.join("assets", "sprites")
    for file in os.listdir(path):
        try:
            # Thêm vào dictionary sprites với key là tên, loại bỏ extension
            sprite_name = os.path.splitext(file)[0]  # Tách tên và phần mở rộng
            sprites[sprite_name] = pygame.image.load(os.path.join(path, file))
        except pygame.error as e:
            print(f"Không thể tải hình ảnh {file}: {e}")

def get_sprite(name):
    return sprites.get(name)

# Load toàn bộ âm thanh từ assets//audios
def load_audios():
    path = os.path.join("assets", "audios")
    for file in os.listdir(path):
        try:
            # Thêm vào dictionary audios với key là tên, loại bỏ extension
            audio_name = os.path.splitext(file)[0]  # Tách tên và phần mở rộng
            audios[audio_name] = pygame.mixer.Sound(os.path.join(path, file))
        except pygame.error as e:
            print(f"Không thể tải âm thanh {file}: {e}")

def play_audio(name):
    if name in audios:
        audios[name].play()
    else:
        print(f"Âm thanh {name} không tồn tại.")