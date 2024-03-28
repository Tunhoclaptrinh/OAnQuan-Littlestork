
class OAnQuan:
    def __init__(self):
        self.board = [5] * 12
        self.board[5] = self.board[11] = 10
        self.current_player = 0
        self.scored_01 = 0
        self.scored_02 = 0

        '''
        self.board[8] = self.board[10] = self.board[6] = self.board[4] = 1
        self.board[0] = 0
        self.board[1] =1
        self.board[11] = self.board[3] = 0
        self.board[2] = 0
        '''

        self.board[0] = 0
        self.board[1] = 1
        self.board[2] = 1
        self.board[3] = 1
        self.board[4] = 0
        self.board[5] = 10
        self.board[6] = 0
        self.board[7] = 2
        self.board[8] = 0
        self.board[9] = 5
        self.board[10] = 0
        self.board[11] = 10

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
    count = 0
    def play_game(self):
        global count
        count = 0
        while True:
            count += 1
            if self.current_player == 2:
                self.current_player = 0
            self.print_board()
            if self.board[5] == 0 and self.board[11] == 0:

                self.scored_01 += sum(self.board[0:5])
                self.scored_02 += sum(self.board[6:11])

                if self.scored_01 < self.scored_02:
                    print("Player 2: Win!")
                elif self.scored_02 < self.scored_01:
                    print("Player 1: Win!")
                else:
                    print("Hòa")
                break
            if self.current_player == 0:
                print("Player 1")
                hole = int(input("Chọn lỗ (0-4) <=> (1-5): "))
                if hole == 5 or hole == 11 or self.board[hole] == 0:
                    print(" lựa chọn không hợp lệ. vui lòng chọn lại !")
                    continue
            if self.current_player == 1:
                print("Player 2")
                hole = int(input("Chọn lỗ (6-11) <=> (1-5): "))
                if hole == 5 or hole == 11 or self.board[hole] == 0:
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

                #Rải quân về bên trái
                if chieu == "t":
                    while stones > 0:
                        if i < 0:
                            i = 11
                        self.board[i] += 1
                        stones -= 1
                        i = i - 1 #vị trí ô tiếp theo theo chiều trái
                        self.print_board()
                    if i < 0:
                        i = 11
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
                        if stones2 == 0 and i == -1:
                            i = 11
                        self.print_board()

                    #ăn quân
                    diem_cong = 0
                    while self.board[i] == 0:
                        if self.board[i - 1] > 0:
                            if self.current_player == 0:
                                self.scored_01 += self.board[i - 1]
                            if self.current_player == 1:
                                self.scored_02 += self.board[i - 1]
                            diem_cong += self.board[i - 1]
                            self.board[i - 1] = 0
                            i = i - 1
                        elif self.board[i - 1] == 0:
                            break
                        if i == 0:
                            i = 12
                        i = i - 1
                    if self.current_player == 0:
                        print("Người chơi 1 nhận được: ", diem_cong)
                        print("Scored 01: ", self.scored_01)
                    if self.current_player == 1:
                        print("Người chơi 2 nhận được: ", diem_cong)
                        print("Scored 02: ", self.scored_02)

                #Rải quân về bên phải
                elif chieu == "p":
                    while stones > 0:
                        if i > 11:
                            i = 0
                        self.board[i] += 1
                        stones -= 1
                        i = i + 1 #vị trí ô tiếp theo theo chiều phải
                        self.print_board()
                    if i > 11:
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

                        self.print_board()

                    #ăn quân
                    diem_cong = 0
                    while self.board[i] == 0:
                        if self.board[i + 1] > 0:
                            if self.current_player == 0:
                                self.scored_01 += self.board[i + 1]
                            if self.current_player == 1:
                                self.scored_02 += self.board[i + 1]
                            diem_cong += self.board[i + 1]
                            self.board[i + 1] = 0
                            i = i + 1
                        elif self.board[i + 1] == 0:
                            break
                        if i == 11:
                            i = -1
                        i = i + 1

                    if self.current_player == 0:
                        print("Người chơi 1 nhận được: ", diem_cong)
                        print("Scored 01: ", self.scored_01)
                    if self.current_player == 1:
                        print("Người chơi 2 nhận được: ", diem_cong)
                        print("Scored 02: ", self.scored_02)

            phanphoi(self)
            self.current_player += 1

            def raithhem():
                if self.current_player == 0 or self.current_player == 2:
                    if sum(self.board[0:5]) == 0:
                        if self.scored_01 == 0:
                            if self.scored_01 < self.scored_02:
                                print("scored 01: ", self.scored_01)
                                print("scored 02: ", self.scored_02)
                                print("Player 2: Win!")
                            elif self.scored_02 < self.scored_01:
                                print("scored 01: ", self.scored_01)
                                print("scored 02: ", self.scored_02)
                                print("Player 1: Win!")
                            else:
                                print("Hòa")
                        if 0 < self.scored_01 < 5:
                            new_stones = self.scored_01
                            self.scored_01 = 0
                            for z in range(0,5):
                                while new_stones > 0:
                                    self.board[z] += 1
                                    new_stones -= 1

                            new_stones = 0
                        if self.scored_01 > 5:
                            self.scored_01 -= 5
                            self.board[0] = self.board[1] = self.board[2] = self.board[3] = self.board[4] = 1

                if self.current_player == 1:
                    if sum(self.board[6:11]) == 0:
                        if self.scored_02 == 0:
                            if self.scored_01 < self.scored_02:
                                print("scored 01: ", self.scored_01)
                                print("scored 02: ", self.scored_02)
                                print("Player 2: Win!")
                            elif self.scored_02 < self.scored_01:
                                print("scored 01: ", self.scored_01)
                                print("scored 02: ", self.scored_02)
                                print("Player 1: Win!")
                            else:
                                print("scored 01: ", self.scored_01)
                                print("scored 02: ", self.scored_02)
                                print("Hòa")
                        if 0 < self.scored_02 <= 5:
                            new_stones = self.scored_02
                            self.scored_02 = 0
                            for z in range(6, 11):
                                while new_stones > 0:
                                    self.board[z] += 1
                                    new_stones -= 1

                            new_stones = 0
                        if self.scored_02 > 5:
                            self.scored_02 -= 5
                        self.board[6] = self.board[7] = self.board[8] = self.board[9] = self.board[10] = 1

            raithhem()

            #stones = self.board[hole]
#Gọi hàm trò chơi và bắt đầu chơi
game = OAnQuan()
game.play_game()