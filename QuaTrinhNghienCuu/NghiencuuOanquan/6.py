import pygame, sys
from button import Button

pygame.init()

SCREEN = pygame.display.set_mode((1000, 700))
pygame.display.set_caption("Menu")

BG = pygame.image.load("assets/Background.png")
pygame.display.set_caption("Ô Ăn Quan")
icon = pygame.image.load(r'image\icon.png')


def get_font(size):
    return pygame.font.Font("assets/font.ttf", size)


def taobang():
    global board, so1, so2, so3, so4, so5, so_quanR, so6, so7, so8, so9, so10, so_quanL, \
        current_player, scored_01, scored_02, current_player
    board = [5] * 12
    board[5] = board[11] = 10
    current_player = 0
    scored_01 = 0
    scored_02 = 0
    so1 = board[0]
    so2 = board[1]
    so3 = board[2]
    so4 = board[3]
    so5 = board[4]
    so_quanR = board[5]
    so6 = board[6]
    so7 = board[7]
    so8 = board[8]
    so9 = board[9]
    so10 = board[10]
    so_quanL = board[11]
taobang()


def play_game():
    global current_player, scored_01, scored_02
    while True:
        if current_player == 2:
            current_player = 0
        #self.print_board()
        if board[5] == 0 and board[11] == 0:

            scored_01 += sum(board[0:5])
            scored_02 += sum(board[6:11])

            '''
            if scored_01 < scored_02:
                print("Player 2: Win!")
            elif scored_02 < scored_01:
                print("Player 1: Win!")
            else:
                print("Hòa")
            break
            '''





        def raithhem():
            global current_player, scored_01, scored_02
            if current_player == 0 or current_player == 2:
                if sum(board[0:5]) == 0:
                    if scored_01 == 0:
                        '''
                        if scored_01 < scored_02:
                            print("Player 2: Win!")
                        elif scored_02 < scored_01:
                            print("Player 1: Win!")
                        else:
                            print("Hòa")
                        '''
                    if 0 < scored_01 < 5:
                        new_stones = scored_01
                        scored_01 = 0
                        for z in range(0, 5):
                            while new_stones > 0:
                                board[z] += 1
                                new_stones -= 1

                        new_stones = 0
                    if scored_01 > 5:
                        scored_01 -= 5
                        board[0] = board[1] = board[2] = board[3] = board[4] = 1

            if current_player == 1:
                if sum(board[6:11]) == 0:
                    if scored_02 == 0:
                        '''
                        if scored_01 < scored_02:
                            print("Player 2: Win!")
                        elif scored_02 < scored_01:
                            print("Player 1: Win!")
                        else:
                            print("Hòa")
                        '''
                    if 0 < scored_02 <= 5:
                        new_stones = scored_02
                        scored_02 = 0
                        for z in range(6, 11):
                            while new_stones > 0:
                                board[z] += 1
                                new_stones -= 1

                        new_stones = 0
                    if scored_02 > 5:
                        scored_02 -= 5
                    board[6] = board[7] = board[8] = board[9] = board[10] = 1

        #raithhem()
        #print_board()

        # stones = self.board[hole]
#play_game()
# Gọi hàm trò chơi và bắt đầu chơi






def play():
    game_font = pygame.sysfont.Font(r'font\Pokemon-Solid.ttf', 40)

    def so_display():
        global so1_surface,so2_surface,so3_surface,so4_surface,so_quanR_surface,so6_surface,so7_surface,so8_surface,so9_surface,so10_surface,so5_surface,so_quanL_surface,\
            so_rect8, so_rect7, so_rect5, so_rect6, so_rect4, so_rect3, so_rect2, so_rect1, so_rect9, so_rect10, quanR_rect, quanL_rect

        so1_surface = game_font.render(str(so1), True, (0, 100, 255))
        so2_surface = game_font.render(str(so2), True, (0, 100, 255))
        so3_surface = game_font.render(str(so3), True, (0, 100, 255))
        so4_surface = game_font.render(str(so4), True, (0, 100, 255))
        so5_surface = game_font.render(str(so5), True, (0, 100, 255))
        so6_surface = game_font.render(str(so6), True, (0, 100, 255))
        so7_surface = game_font.render(str(so7), True, (0, 100, 255))
        so8_surface = game_font.render(str(so8), True, (0, 100, 255))
        so9_surface = game_font.render(str(so9), True, (0, 100, 255))
        so10_surface = game_font.render(str(so10), True, (0, 100, 255))

        so_rect10 = so10_surface.get_rect(center=(404, 330))
        so_rect9 = so9_surface.get_rect(center=(308, 330))
        so_rect8 = so8_surface.get_rect(center=(500, 330))
        so_rect7 = so7_surface.get_rect(center=(596, 330))
        so_rect6 = so6_surface.get_rect(center=(692, 330))
        so_rect5 = so5_surface.get_rect(center=(692, 426))
        so_rect4 = so4_surface.get_rect(center=(596, 426))
        so_rect3 = so3_surface.get_rect(center=(500, 426))
        so_rect2 = so2_surface.get_rect(center=(404, 426))
        so_rect1 = so1_surface.get_rect(center=(308, 426))

        so_quanR_surface = game_font.render(str(so_quanR), True, (213, 108, 177))
        so_quanL_surface = game_font.render(str(so_quanL), True, (213, 108, 177))

        quanR_rect = so_quanR_surface.get_rect(center = (788,378))
        quanL_rect = so_quanL_surface.get_rect(center = (212,378))

    so_display()
    pygame.display.update()

    #background


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

    pygame.display.update()

    # Loop chính
    while True:
        window.blit(background, (0, 0))

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

                global hole,current_player
                if ochon_dichuyen_doc == 378 and ochon_dichuyen_ngang == 457:
                    hole = 2

                if current_player == 0:
                    if hole == 5 or hole == 11 or board[hole] == 0:
                        continue
                if current_player == 1:
                    if hole == 5 or hole == 11 or board[hole] == 0:
                        continue

                global stones, i
                stones = board[hole]
                board[hole] = 0

                if event.key == pygame.K_KP_ENTER:
                    ochon = pygame.image.load(r'image\controovuongdo.png')
                    if event.key == pygame.K_RIGHT:
                        chieu = "p"
                        def chonchieu():
                            if chieu == "p":
                                i = hole + 1
                        chonchieu()

                        def phanphoi():
                            global stones, i, scored_01, scored_02

                            # Rải quân về bên phải
                            if chieu == "p":
                                while stones > 0:
                                    if i > 11:
                                        i = 0
                                    board[i] += 1
                                    stones -= 1
                                    i = i + 1  # vị trí ô tiếp theo theo chiều phải
                                    # print_board()
                                if i > 11:
                                    i = 0
                                while board[i] > 0:
                                    if i == 5 or i == 11:
                                        break
                                    stones2 = board[i]
                                    board[i] = 0
                                    i = i + 1
                                    while stones2 > 0:
                                        if i > 11:
                                            i = 0
                                        board[i] += 1
                                        stones2 -= 1
                                        i = i + 1
                                    if stones2 == 0 and i == 12:
                                        i = 0

                                    # print_board()

                                # ăn đá
                                diem_cong = 0
                                while board[i] == 0:
                                    if board[i + 1] > 0:
                                        if current_player == 0:
                                            scored_01 += board[i + 1]
                                        if current_player == 1:
                                            scored_02 += board[i + 1]
                                        diem_cong += board[i + 1]
                                        board[i + 1] = 0
                                        i = i + 1
                                    elif board[i + 1] == 0:
                                        break
                                    if i == 11:
                                        i = -1
                                    i = i + 1

                                '''
                                if current_player == 0:
                                    print("Người chơi 1 nhận được: ", diem_cong)
                                    print("Scored 01: ", scored_01)
                                if current_player == 1:
                                    print("Người chơi 2 nhận được: ", diem_cong)
                                    print("Scored 02: ", scored_02)
                                '''

                        phanphoi()
                        current_player += 1

                    if event.key == pygame.K_LEFT:
                        chieu = "t"

                        def chonchieu():
                            global chieu
                            if chieu == "t":
                                i = hole - 1
                        chonchieu()

                        def phanphoi():
                            global stones, i, scored_01, scored_02
                            # Rải quân về bên trái
                            if chieu == "t":
                                while stones > 0:
                                    if i < 0:
                                        i = 11
                                    board[i] += 1
                                    stones -= 1
                                    i = i - 1  # vị trí ô tiếp theo theo chiều trái
                                    # print_board()
                                if i < 0:
                                    i = 11
                                while board[i] > 0:

                                    if i == 5 or i == 11:
                                        break
                                    stones2 = board[i]
                                    board[i] = 0
                                    i = i - 1
                                    while stones2 > 0:
                                        if i < 0:
                                            i = 11
                                        board[i] += 1
                                        stones2 -= 1
                                        i = i - 1
                                    if stones2 == 0 and i == -1:
                                        i = 0
                                    #print_board()

                                # ăn quân
                                diem_cong = 0
                                while board[i] == 0:
                                    if board[i - 1] > 0:
                                        if current_player == 0:
                                            scored_01 += board[i - 1]
                                        if current_player == 1:
                                            scored_02 += board[i - 1]
                                        diem_cong += board[i - 1]
                                        board[i - 1] = 0
                                        i = i - 1
                                    elif board[i - 1] == 0:
                                        break
                                    if i == 0:
                                        i = 12
                                    i = i - 1
                                '''
                                if current_player == 0:
                                    print("Người chơi 1 nhận được: ", diem_cong)
                                    print("Scored 01: ", scored_01)
                                if current_player == 1:
                                    print("Người chơi 2 nhận được: ", diem_cong)
                                    print("Scored 02: ", scored_02)
                                '''

                        phanphoi()
                        current_player += 1

            if Back == (0,0):
                window.blit(ochon_scaleforback, (0,0))


            window.blit(so1_surface, so_rect1)
            window.blit(so2_surface, so_rect2)
            window.blit(so3_surface, so_rect3)
            window.blit(so4_surface, so_rect4)
            window.blit(so5_surface, so_rect5)
            window.blit(so6_surface, so_rect6)
            window.blit(so7_surface, so_rect7)
            window.blit(so8_surface, so_rect8)
            window.blit(so9_surface, so_rect9)
            window.blit(so10_surface, so_rect10)

            window.blit(so_quanR_surface, quanR_rect)
            window.blit(so_quanL_surface, quanL_rect)



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



start_menu()
# Cập nhật màn hình
pygame.display.update()


