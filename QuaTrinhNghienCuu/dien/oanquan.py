class OAnQuan:
    def __init__(self):
        self.board = [5] * 12
        self.board[5] = self.board[11] = 0
        self.current_player = 0
        self.board[0] = 0
        self.board[1] = 0
        self.board[2] = 1
        self.board[3] = 1
        self.board[4] = 1
        self.board[5] = 1
        self.scored_01 = 0
        self.scored_02 = 0
        self.board[6] = 1
        self.board[7] = 5
        self.board[8] = 1
        self.board[9] = 5
        self.board[10] = 1
    def print_board(self):
        print("     ", end="")
        for k in range(10, 5, -1):
            print(self.board[k], " ", end="")
        print()
        print(self.board[11], "                 ", self.board[5])
        print("     ", end="")
        for k in range(5):
            print(self.board[k], " ", end="")
        print("\n")

    def play_game(self):
        while True:
            self.print_board()
            print("Player", self.current_player + 1)

            if self.board[5] == 0 and self.board[11] == 0:
                break
            hole = int(input("Chọn lỗ (0-5): "))
            if hole == 5 or hole == 11:
                print(" lựa chọn không hợp lệ. vui lòng chọn lại !")
                continue

            global stones, i
            stones = self.board[hole]
            self.board[hole] = 0

            #rẽ nhánh, chọn chiều rải đá
            chieu = input("Chieu p/t: ")
            if chieu == "t":
                i = hole - 1
            elif chieu == "p":
                i = hole + 1

            def phanphoi(self):
                global stones, i
                if chieu == "t":
                    while stones > 0:
                        if i < 0:
                            i = 11
                        self.board[i] += 1
                        stones -= 1
                        i = i - 1

                    while self.board[i] > 0:
                        if i == 5 or i == 11:
                            break
                        stones2 = self.board[i]
                        self.board[i] = 0
                        i = i - 1
                        while stones2 > 0:
                            if i < 0:
                                i = 11
                            self.board[i] += 1
                            stones2 -= 1
                            i = i - 1
                        if stones2 == 0 and i == 12:
                            i = 0
                    diem_cong = 0
                    diem_cong = 0
                    while self.board[i] == 0:
                        if self.board[i - 1] > 0:
                            self.scored_01 += self.board[i - 1]
                            print("scored 1 bên trái: ", self.scored_01)

                            diem_cong += self.board[i - 1]
                            self.board[i - 1] = 0
                            i = i - 1
                        elif self.board[i - 1] == 0:
                            break
                        if i <= 0:
                            i = 0
                        i = i - 1
                    print(" người t1 nhận được: ",diem_cong)
                    print("scored 1 bên trái: ", self.scored_01)

                elif chieu == "p":
                    while stones > 0:
                        if i > 11:
                            i = 0
                        self.board[i] += 1
                        stones -= 1
                        i = i + 1
                    if stones == 0 and i == 12:
                        i = 0
                    while self.board[i] > 0:
                        if i == 5 or i == 11:
                            break
                        stones2 = self.board[i]
                        self.board[i] = 0
                        i = i + 1
                        while stones2 > 0:
                            if i > 11:
                                i = 0
                            self.board[i] += 1
                            stones2 -= 1
                            i = i + 1
                        if stones2 == 0 and i == 12:
                            i = 0
                    diem_cong = 0
                    while self.board[i] == 0:
                        if self.board[i + 1] > 0:
                            self.scored_02 += self.board[i + 1]
                            print("scored 1 bên phải: ", self.scored_02)

                            diem_cong += self.board[i + 1]
                            self.board[i + 1] = 0
                            i = i + 1
                        elif self.board[i + 1] == 0:
                            break
                        if i >= 11:
                            i = 0
                        i = i + 1

                    print(" người t2 nhận được: ", diem_cong)

            phanphoi(self)
            stones = self.board[hole]



# Tạo trò chơi và bắt đầu chơi
game = OAnQuan()
game.play_game()