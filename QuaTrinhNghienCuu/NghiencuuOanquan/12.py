import pygame
import sys

pygame.init()

screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()

hole_position = None
direction = None

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key in [pygame.K_0, pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5]:
                hole_position = int(chr(event.key))
                print(f"Vị trí lỗ: {hole_position}")
            elif event.key in [pygame.K_t, pygame.K_p]:
                direction = 't' if event.key == pygame.K_t else 'p'
                print(f"Chiều: {direction}")

    pygame.display.flip()
    clock.tick(60)

    # Kiểm tra nếu đã nhấn cả hai nút lệnh
    if hole_position is not None and direction is not None:
        print("Đã nhấn cả hai nút lệnh!")
        # Thực hiện công việc cần thiết với hole_position và direction ở đây

        # Đặt lại giá trị của hole_position và direction để chuẩn bị cho lần nhấn tiếp theo
        hole_position = None
        direction = None
