from enum import IntEnum, auto

class Layer(IntEnum):
    BACKGROUND = auto()  # Lớp nền
    OBSTACLE = auto()    # Lớp chướng ngại vật
    FLOOR = auto()       # Lớp mặt đất
    PLAYER = auto()      # Lớp nhân vật
    UI = auto()          # Lớp giao diện người dùng