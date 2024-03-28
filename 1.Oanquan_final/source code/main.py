import pygame, sys
from button import Button


pygame.init()

SCREEN = pygame.display.set_mode((1000, 700))
pygame.display.set_caption("Menu")

BG = pygame.image.load("assets/Background.png")
pygame.display.set_caption("Ô Ăn Quan")
icon = pygame.image.load(r'image\icon.png')


def get_font(size):  # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/font.ttf", size)

class Hienthi():
    def __init__(self):
        def play():

            so = 0
            game_font = pygame.sysfont.Font(r'font\Pokemon-Solid.ttf', 40)

            def so_display():
                global so_surface, so_rect8, so_rect7, so_rect5, so_rect6, so_rect4, so_rect3, so_rect2, so_rect1, so_rect9, so_rect10
                so_surface = game_font.render(str(so), True, (0, 100, 255))
                so2_surface = game_font.render("1", True, (0, 100, 255))
                so_rect8 = so_surface.get_rect(center=(500, 330))
                so_rect7 = so_surface.get_rect(center=(596, 330))
                so_rect6 = so_surface.get_rect(center=(692, 330))
                so_rect5 = so_surface.get_rect(center=(692, 426))
                so_rect4 = so_surface.get_rect(center=(596, 426))
                so_rect3 = so_surface.get_rect(center=(500, 426))
                so_rect2 = so2_surface.get_rect(center=(404, 426))
                so_rect1 = so_surface.get_rect(center=(308, 426))
                so_rect9 = so_surface.get_rect(center=(404, 330))
                so_rect10 = so_surface.get_rect(center=(308, 330))

            so_display()

            soquan = 10
            def soquan_display():
                global soquan_surface, quanR_rect, quanL_rect
                soquan_surface = game_font.render(str(soquan), True, (213, 108, 177))
                quanR_rect = soquan_surface.get_rect(center = (788,378))
                quanL_rect = soquan_surface.get_rect(center = (212,378))

            soquan_display()

            #background
            soquan_display()

            # background
            background = pygame.image.load(r'image\background0.png')
            pygame.display.set_icon(icon)
            # fps=pygame.time.Clock()

            # Tạo một cửa sổ
            window = pygame.display.set_mode((1000, 750))
            # Ô chọn
            ochon = pygame.image.load(r'image\controovuong.png')
            ochon_scaleforback = pygame.transform.scale(ochon, (50,50))
            ochon_scaleforback_rect = ochon_scaleforback.get_rect()
            # toa do o chon
            ochon_dichuyen_doc = 378
            ochon_dichuyen_ngang = 457

            # ochon_rect = ochon.get_rect(center=(500,421))
            # ochon_rect = ochon.get_rect(center=(500,421))
            # Ô Vuông
            ovuong8 = pygame.image.load(r'image\ovuong.png')
            ovuong8_rect = ovuong8.get_rect(center=(500, 325))
            ovuong7 = pygame.image.load(r'image\ovuong.png')
            ovuong7_rect = ovuong7.get_rect(center=(596, 325))
            ovuong6 = pygame.image.load(r'image\ovuong.png')
            ovuong6_rect = ovuong8.get_rect(center=(692, 325))
            ovuong5 = pygame.image.load(r'image\ovuong.png')
            ovuong5_rect = ovuong8.get_rect(center=(692, 421))
            ovuong4 = pygame.image.load(r'image\ovuong.png')
            ovuong4_rect = ovuong8.get_rect(center=(596, 421))
            ovuong3 = pygame.image.load(r'image\ovuong.png')
            ovuong3_rect = ovuong8.get_rect(center=(500, 421))
            ovuong2 = pygame.image.load(r'image\ovuong.png')
            ovuong2_rect = ovuong8.get_rect(center=(404, 421))
            ovuong1 = pygame.image.load(r'image\ovuong.png')
            ovuong1_rect = ovuong8.get_rect(center=(308, 421))
            ovuong9 = pygame.image.load(r'image\ovuong.png')
            ovuong9_rect = ovuong8.get_rect(center=(404, 325))
            ovuong10 = pygame.image.load(r'image\ovuong.png')
            ovuong10_rect = ovuong8.get_rect(center=(308, 325))
            # Ô quan
            oquanR = pygame.image.load(r'image\quanR.png')
            oquanR_rect = oquanR.get_rect(center=(788, 373))
            oquanL = pygame.image.load(r'image\quanL.png')
            oquanL_rect = oquanL.get_rect(center=(212, 373))
            #Back Button
            Back = (1, 1)
            back_button = pygame.image.load(r'assets\Back.png')
            back_button_scale = pygame.transform.scale(back_button, (40,40))
            back_button_rect = back_button_scale.get_rect()
            # Loop chính
            click=True
            while True:
                # Lấy vị trí chuột
                mouse_position = pygame.mouse.get_pos()
                # Nhận trạng thái nút chuột
                mouse_pressed = pygame.mouse.get_pressed()

                # Thoát game
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()

                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_LEFT:
                            ochon_dichuyen_ngang = ochon_dichuyen_ngang - 96
                        if event.key == pygame.K_RIGHT:
                            ochon_dichuyen_ngang = ochon_dichuyen_ngang + 96
                        if event.key == pygame.K_UP:
                            ochon_dichuyen_doc = ochon_dichuyen_doc - 96
                        if event.key == pygame.K_DOWN:
                            ochon_dichuyen_doc = ochon_dichuyen_doc + 96
                        '''
                        if event.key == pygame.K_SPACE:
                            Back = (0, 0)
                            if Back == (0, 0) and event.key == pygame.K_KP_ENTER:
                                start_menu()
                        '''
                        if event.key == pygame.K_KP_ENTER:
                            ochon = pygame.image.load(r'image\controovuongdo.png')
                            if event.key == pygame.K_RIGHT:
                                chieu = "p"
                            if event.key == pygame.K_LEFT:
                                chieu = "t"

                        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                            ochon = pygame.image.load(r'image\controovuong.png')






                    #pygame.display.update()



                    window.blit(background, (0, 0))
                    if Back == (0,0):
                        window.blit(ochon_scaleforback, (0,0))


                    window.blit(so_surface, so_rect8)
                    window.blit(so_surface, so_rect7)
                    window.blit(so_surface, so_rect6)
                    window.blit(so_surface, so_rect5)
                    window.blit(so_surface, so_rect4)
                    window.blit(so_surface, so_rect3)
                    window.blit(so_surface, so_rect2)
                    window.blit(so_surface, so_rect1)
                    window.blit(so_surface, so_rect9)
                    window.blit(so_surface, so_rect10)

                    window.blit(soquan_surface, quanR_rect)
                    window.blit(soquan_surface, quanL_rect)

                # Ovuong
                window.blit(ovuong1, ovuong1_rect)
                window.blit(ovuong2, ovuong2_rect)
                window.blit(ovuong3, ovuong3_rect)
                window.blit(ovuong4, ovuong4_rect)
                window.blit(ovuong5, ovuong5_rect)
                window.blit(ovuong6, ovuong6_rect)
                window.blit(ovuong7, ovuong7_rect)
                window.blit(ovuong8, ovuong8_rect)
                window.blit(ovuong9, ovuong9_rect)
                window.blit(ovuong10, ovuong10_rect)
                # Ochon
                if ochon_dichuyen_ngang == 745:
                    ochon_dichuyen_ngang = 265
                if ochon_dichuyen_ngang == 169:
                    ochon_dichuyen_ngang = 649
                if ochon_dichuyen_doc == 474:
                    ochon_dichuyen_doc = 282
                if ochon_dichuyen_doc == 186:
                    ochon_dichuyen_doc = 378
                window.blit(ochon, (ochon_dichuyen_ngang, ochon_dichuyen_doc))

                # Oquan
                window.blit(oquanR, oquanR_rect)
                window.blit(oquanL, oquanL_rect)
                window.blit(back_button_scale, back_button_rect)

                # Vẽ hình tròn khi nhấn chuột
                if mouse_pressed[0] == 1:
                    pygame.draw.circle(window, (255, 0, 0), mouse_position, 10)

                    # Update d



                # Cập nhật màn hình
                pygame.display.update()

        def start_menu():
            #toa do o chon che do choi
            toado_chedongang = 508
            khung2 = pygame.image.load(r'giaodien\ochonchedo1or2.png')
            #khung2_rect = khung2.get_rect(center=(toado_chedongang, 414))
            khung_02 = pygame.transform.scale(khung2, (504, 256))

            #chế độ chơi
            chedo1 = pygame.image.load(r'giaodien\CHEDO1.png')
            chedo_01_rect = chedo1.get_rect(center= (275, 350))
            chedo_01 = pygame.transform.scale(chedo1, (400, 80))
            chedo2 = pygame.image.load(r'giaodien\CHEDO2.png')
            chedo_02_rect = chedo2.get_rect(center= (800, 350))
            chedo_02 = pygame.transform.scale(chedo2, (400, 80))

            # Tạo font và đối tượng văn bản
            font = pygame.font.Font(r'font\UTM Akashi.ttf', 40)
            text_2nguoichoi = font.render("2 người chơi", True, (22, 147, 249))
            text_choivoimay = font.render("Chơi với máy", True, (22, 147, 249))

            #hình nền
            background_image = pygame.image.load(r'giaodien\nenn.jpg')
            background_image = pygame.transform.scale(background_image, (1000, 750))
            text_oanquan = pygame.image.load(r'giaodien\text_oanquan.png')
            text_oanquan = pygame.transform.scale(text_oanquan, (600, 150))
            pygame.display.set_icon(icon)

            # Tạo một cửa sổ
            window = pygame.display.set_mode((1000, 750))
            # Ô chọn
            ochon = pygame.image.load(r'image\controovuong.png')

            # Vòng lặp chính của game
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                    #di chuyển ô chọn chế độ
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_LEFT or event.key == pygame.K_d:
                            toado_chedongang = toado_chedongang - 533
                            if toado_chedongang == 508:
                                chedo = "chedo2"
                            if toado_chedongang == -25:
                                chedo = "chedo1"
                            if toado_chedongang == 508:
                                chedo = "chedo2"
                            if toado_chedongang > 508:
                                toado_chedongang = -25
                            if toado_chedongang < -25:
                                toado_chedongang = 508

                        if event.key == pygame.K_RIGHT or event.key == pygame.K_a:
                            toado_chedongang = toado_chedongang + 533
                            if toado_chedongang == 508:
                                chedo = "chedo2"
                            if toado_chedongang == -25:
                                chedo = "chedo1"
                            if toado_chedongang > 508:
                                toado_chedongang = -25
                            if toado_chedongang < -25:
                                toado_chedongang = 508
                        if event.key == pygame.K_KP_ENTER:
                            if toado_chedongang == -25:
                                chedo = "chedo1"
                            if toado_chedongang > 508:
                                toado_chedongang = -25
                            if toado_chedongang < -25:
                                toado_chedongang = 508
                            if chedo == "chedo1":
                                play()

                    pygame.display.update()

                    # Vẽ hình nền lên màn hình
                    window.blit(background_image, (0, 0))

                    # Vẽ khung , tiêu đề trên màn hình
                    window.blit(chedo_01, chedo_01_rect)
                    window.blit(chedo_02, chedo_02_rect)
                    window.blit(khung_02,(toado_chedongang,199))
                    window.blit(text_oanquan, (220, 75))
                    window.blit(text_2nguoichoi, (100,300))
                    window.blit(text_choivoimay, (630, 300))


                # Cập nhật màn hình
                pygame.display.update()
        start_menu()
Hienthi()