def taobang():
    global board, so1, so2, so3, so4, so5, so_quanR, so6, so7, so8, so9, so10, so_quanL, \
        current_player, scored_01, scored_02
    board = [5] * 12
    board[5] = board[11] = 10
    current_player = 0
    scored_01 = 0
    scored_02 = 0

    board[0] = 0
    board[1] = 1
    board[2] = 0
    board[3] = 1
    board[4] = 0
    board[5] = 1
    board[6] = 0
    board[7] = 1
    board[8] = 0
    board[9] = 1
    board[10] = 1
    board[11] = 1


taobang()

def print_board():
    print("     ", end="")
    for k in range(10, 5, -1):
        print(board[k], " ", end="")
    print()
    print(board[11], "                 ", board[5])
    print("     ", end="")
    for k in range(5):
        print(board[k], " ", end="")
    print("\n")
print_board()
def play_game():
    global current_player, scored_01, scored_02
    count = 0
    while True:

        if current_player == 2:
            current_player = 0
        #self.print_board()
        if board[5] == 0 and board[11] == 0:

            scored_01 += sum(board[0:5])
            scored_02 += sum(board[6:11])

            if scored_01 < scored_02:
                print("scored 01: ", scored_01)
                print("scored 02: ", scored_02)
                print("Player 2: Win!")
            elif scored_02 < scored_01:
                print("scored 01: ", scored_01)
                print("scored 02: ", scored_02)
                print("Player 1: Win!")
            else:
                print("scored 01: ", scored_01)
                print("scored 02: ", scored_02)
                print("Hòa")
            break

        if current_player == 0:
            print("Player 1")
            hole = int(input("Chọn lỗ (0-4) <=> (1-5): "))
            count += 1
            if hole == 5 or hole == 11 or board[hole] == 0:
                print(" lựa chọn không hợp lệ. vui lòng chọn lại !")
                continue
        if current_player == 1:
            print("Player 2")
            hole = int(input("Chọn lỗ (6-11) <=> (1-5): "))
            if hole == 5 or hole == 11 or board[hole] == 0:
                print(" lựa chọn không hợp lệ. vui lòng chọn lại !")
                continue

        global stones, i
        stones = board[hole]
        board[hole] = 0

        # rẽ nhánh, chọn chiều rải đá
        chieu = input("Chieu p/t: ")
        if chieu == "t":
            i = hole - 1
        elif chieu == "p":
            i = hole + 1
        def phanphoi():
            global stones, i,scored_01, scored_02
            # Rải quân về bên trái
            if chieu == "t":
                while stones > 0:
                    if i < 0:
                        i = 11
                    board[i] += 1
                    stones -= 1
                    i = i - 1  # vị trí ô tiếp theo theo chiều trái
                    print_board()
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
                        i = 11
                    print_board()


                # ăn quân
                diem_cong = 0
                while board[i] == 0:
                    if i - 1 == -1:
                        i = 12
                    if board[i - 1] > 0 and count == 1 and (i - 1 == 5 or i - 1 == 11):
                        diem_cong = diem_cong + (board[i - 1] - 10)
                        if current_player == 0:
                            scored_01 += diem_cong
                        if current_player == 1:
                            scored_02 += diem_cong
                        board[i - 1] = board[i - 1] - diem_cong
                        break
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
                if current_player == 0:
                    print("Người chơi 1 nhận được: ", diem_cong)
                    print("Scored 01: ", scored_01)
                if current_player == 1:
                    print("Người chơi 2 nhận được: ", diem_cong)
                    print("Scored 02: ", scored_02)

            # Rải quân về bên phải
            elif chieu == "p":
                while stones > 0:
                    if i > 11:
                        i = 0
                    board[i] += 1
                    stones -= 1
                    i = i + 1  # vị trí ô tiếp theo theo chiều phải
                    print_board()
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

                    print_board()

                # ăn đá
                diem_cong = 0
                while board[i] == 0:
                    if i + 1 == 12:
                         i = -1
                    if board[i + 1] > 0 and count == 1 and (i + 1 == 5 or i + 1 == 11):
                        diem_cong = diem_cong + (board[i + 1] - 10)
                        if current_player == 0:
                            scored_01 += diem_cong
                        if current_player == 1:
                            scored_02 += diem_cong
                        board[i + 1] = board[i + 1] - diem_cong
                        break

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

                if current_player == 0:
                    print("Người chơi 1 nhận được: ", diem_cong)
                    print("Scored 01: ", scored_01)
                if current_player == 1:
                    print("Người chơi 2 nhận được: ", diem_cong)
                    print("Scored 02: ", scored_02)

        phanphoi()
        current_player += 1
        def raithhem():
            global current_player, scored_01, scored_02
            if current_player == 0 or current_player == 2:
                if sum(board[0:5]) == 0:

                    if 0 <= scored_01 < 5:
                        new_stones = scored_01
                        scored_01 = 0
                        for z in range(0, new_stones):
                            board[z] += 1

                        new_stones = 0
                    if scored_01 >= 5:
                        scored_01 -= 5
                        board[0] = board[1] = board[2] = board[3] = board[4] = 1


            if current_player == 1:
                if sum(board[6:11]) == 0:

                    if 0 <= scored_02 < 5:
                        new_stones = scored_02
                        scored_02 = 0
                        for z in range(6, 6 + new_stones):
                            board[z] += 1

                        new_stones = 0
                    if scored_02 >= 5:
                        scored_02 -= 5
                        board[6] = board[7] = board[8] = board[9] = board[10] = 1

        raithhem()
        print_board()

        # stones = self.board[hole]
play_game()
# Gọi hàm trò chơi và bắt đầu chơi


