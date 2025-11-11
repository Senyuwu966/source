import pygame
import random
import sys
from pygame.locals import *

# Khởi tạo Pygame
pygame.init()

# Thiết lập màn hình
screen_width = 400
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Flappy Bird")

# Màu sắc
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Tải hình ảnh và âm thanh
bird_image = pygame.image.load(r'D:\DATA\CreateGame\FlappyBird\bird.png')  # Thay 'bird.png' bằng đường dẫn hình ảnh của bạn
pipe_image = pygame.image.load(r'D:\DATA\CreateGame\FlappyBird\pipe.png')  # Thay 'pipe.png' bằng đường dẫn hình ảnh của bạn
background_image = pygame.image.load(r'D:\DATA\CreateGame\FlappyBird\background.png')  # Thay 'background.png' bằng đường dẫn hình ảnh của bạn

flap_sound = pygame.mixer.Sound(r'D:\DATA\CreateGame\FlappyBird\flap.wav')  # Thay 'flap.wav' bằng đường dẫn âm thanh của bạn
score_sound = pygame.mixer.Sound(r'D:\DATA\CreateGame\FlappyBird\score.wav')  # Thay 'score.wav' bằng đường dẫn âm thanh của bạn

# Biến trò chơi
bird_x = 50
bird_y = 300
bird_velocity = 0
gravity = 0.5
score = 0

# Tạo font để hiển thị điểm số
font = pygame.font.Font(None, 36)

# Hàm vẽ chim
def draw_bird(y):
    screen.blit(bird_image, (bird_x, y))

# Hàm tạo ống
def create_pipe():
    pipe_height = random.randint(150, 450)
    upper_pipe = pipe_image.get_rect(midbottom=(500, pipe_height))
    lower_pipe = pipe_image.get_rect(midtop=(500, pipe_height - 200))
    return upper_pipe, lower_pipe

# Hàm kiểm tra va chạm
def check_collision(bird_rect, pipes):
    for pipe in pipes:
        if bird_rect.colliderect(pipe):
            return True
    return False

# Hàm hiển thị điểm số
def display_score(score):
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

# Hàm game over
def game_over():
    global score
    # Hiển thị thông báo game over và điểm số
    game_over_text = font.render("Game Over!", True, WHITE)
    score_text = font.render(f"Final Score: {score}", True, WHITE)
    screen.blit(game_over_text, (screen_width // 2 - game_over_text.get_width() // 2, screen_height // 2 - 50))
    screen.blit(score_text, (screen_width // 2 - score_text.get_width() // 2, screen_height // 2))
    pygame.display.update()
    pygame.time.wait(2000)  # Chờ 2 giây
    reset_game()  # Khởi động lại trò chơi

# Hàm reset trò chơi
def reset_game():
    global bird_y, bird_velocity, score, pipes
    bird_y = 300
    bird_velocity = 0
    score = 0
    pipes = [create_pipe()]
    main_game()

# Hàm chính của trò chơi
def main_game():
    global bird_y, bird_velocity, score
    clock = pygame.time.Clock()
    pipes = [create_pipe()]
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
                bird_velocity = -10
                flap_sound.play()

        # Cập nhật vị trí chim
        bird_velocity += gravity
        bird_y += bird_velocity
pygame.QUIT
        # Di chuyen