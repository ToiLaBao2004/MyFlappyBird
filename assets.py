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
        # Thêm vào dictionary sprites với key là tên, loại bỏ extension
        sprites[file.split('.')[0]] = pygame.image.load(os.path.join(path, file))

def get_sprite(name):
    return sprites[name]

# Load toàn bộ âm thanh từ assets//audios
def load_audios():
    path = os.path.join("assets", "audios")
    for file in os.listdir(path):
        # Thêm vào dictionary audios với key là tên, loại bỏ extension
        audios[file.split('.')[0]] = pygame.mixer.Sound(os.path.join(path, file))

def play_audio(name):
    audios[name].play()