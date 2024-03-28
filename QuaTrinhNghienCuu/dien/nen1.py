import pygame
import sys

pygame.init()

#tieude
pygame.display.set_caption("Ô Ăn Quan")
icon = pygame.image.load(r'image\icon.png')

#Khung chế độ chơi
# toa do o chon
toado_chedongang = 815
khung2 = pygame.image.load(r'giaodien\ochonchedo1or2.png')
khung2_rect = khung2.get_rect(center=(toado_chedongang, 414))
khung_02 = pygame.transform.scale(khung2, (504, 256))

#chế độ chơi
chedo1 = pygame.image.load(r'giaodien\CHEDO1.png')
chedo_01_rect = chedo1.get_rect(center= (275, 350))
chedo_01 = pygame.transform.scale(chedo1, (400, 80))

chedo2 = pygame.image.load(r'giaodien\CHEDO2.png')
chedo_02_rect = chedo2.get_rect(center= (800, 350))
chedo_02 = pygame.transform.scale(chedo2, (400, 80))


# Tạo font và đối tượng văn bản
font = pygame.font.Font(r'font\UTM Akashi.ttf', 80)  
text = font.render("Ô ĂN QUAN", True, (181, 82, 4))
font = pygame.font.Font(r'font\UTM Akashi.ttf', 40)  
text_2nguoichoi = font.render("2 người chơi", True, (22, 147, 249)) 
text_choivoimay = font.render("Chơi với máy", True, (22, 147, 249))

# hình nền
background_image = pygame.image.load(r'giaodien\nenn.jpg')  
background_image = pygame.transform.scale(background_image, (1000, 750))
pygame.display.set_icon(icon)
#fps=pygame.time.Clock()


# Tạo một cửa sổ
window = pygame.display.set_mode((1000, 750))
# Ô chọn
ochon = pygame.image.load(r'image\controovuong.png')


# Vòng lặp chính của game
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        #di chuyển ô chọn chế độ
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                toado_chedongang = toado_chedongang + 480
            if event.key == pygame.K_RIGHT:
                toado_chedongang = toado_chedongang - 480
    
        pygame.display.update()

                

        # Vẽ hình nền lên màn hình
        window.blit(background_image, (0, 0))

        # Vẽ khung , tiêu đề trên màn hình
        window.blit(chedo_01, chedo_01_rect)
        window.blit(chedo_02, chedo_02_rect)

        window.blit(khung_02, khung2_rect)

        window.blit(text, (310, 100))
        window.blit(text_2nguoichoi, (100,300))
        window.blit(text_choivoimay, (630, 300))


    # Cập nhật màn hình
    pygame.display.update()

# Kết thúc Pygame khi thoát
pygame.quit()
sys.exit()
