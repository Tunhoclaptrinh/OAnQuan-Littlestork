class OAnQuan:
    def __init__(self):
        self.board = [5] * 12  # Bàn cờ với 10 lỗ và 2 lỗ nhà
        self.board[5] = self.board[11] = 10  # Lỗ nhà không có đá
        self.current_player = 0  # Người chơi hiện tại, 0 hoặc 1
        self.scored_01 = 0
        self.scored_02 = 0

    def print_board(self):
        print("   ", end="")
        for i in range(10, 5, -1):
            print(self.board[i], " ", end="")
        print()
        print(self.board[11], "             ", self.board[5])
        print("   ", end="")
        for i in range(5):
            print(self.board[i], " ", end="")
        print("\n")

    def play_game(self):
        while True:
            self.print_board()

            # Kiểm tra xem bàn cờ còn đá không (sử dụng để rải thêm thêm quân)
            if sum(self.board[:5]) == 0 or sum(self.board[6:12]) == 0:
                break

            print("Player", self.current_player + 1)
            hole = int(input("Chọn lỗ (0-5): ")) #phím điều hướng để chọn

            # Kiểm tra tính hợp lệ của lựa chọn
            #if hole < 0 or hole > 5 or self.board[hole] == 0:
              #  print("Lựa chọn không hợp lệ! Chọn lại.")
              #  continue
            global stones,i
            stones = self.board[hole]
            self.board[hole] = 0
            #stones1 = self.board[hole+stones]
            #rẽ nhánh, chọn chiều rải đá
            chieu = input("Chieu p/t: ")
            if chieu == "t":
                i = hole - 1
            elif chieu == "p":
                i = hole + 1

            # Phân phối đá (rải tiếp)
            while stones > 0:
                global k
                def phanphoi(self):
                    global stones,i,k
                    k = stones
                    if chieu == "t":
                        while stones > 0:
                            if self.current_player == 0 and i == 12:
                                i = 0
                            if self.current_player == 0 and i == -1:
                                i = 11
                            elif self.current_player == 1 and i == 5:
                                i = 5
                            self.board[i] += 1
                            stones -= 1
                            i = i - 1  # i là ô thứ ...
                            k = k - 1
                    elif chieu == "p":
                        while stones > 0:
                            if self.current_player == 0 and i == 12:
                                i = 0
                            if self.current_player == 0 and i == -1:
                                i = 11
                            elif self.current_player == 1 and i == 5:
                                i = 5
                            self.board[i] += 1
                            stones -= 1
                            i = i + 1  # i là ô thứ ...
                            k = k - 1

                phanphoi(self)
                self.print_board()

                if k == 0:
                    if chieu == "t":
                        if self.current_player == 0 and i == 12:
                            i = 0
                        if self.current_player == 0 and i == -1:
                            i = 11
                        stones = self.board[i]
                        self.board[i] = 0
                        i = i - 1
                    elif chieu == "p":
                        if self.current_player == 0 and i == 12:
                            i = 0
                        if self.current_player == 0 and i == -1:
                            i = 11
                        stones = self.board[i]
                        self.board[i] = 0
                        i = i + 1
                        k = stones
                phanphoi(self)

                if chieu == "p":
                    i = i - 1
                if chieu == "t":
                    i = i + 1
                while self.board[i] == 0:
                    def an_da(self):
                        global i
                        diem_cong = 0
                        while self.board[i] == 0:
                            if chieu == "p":
                                if self.board[i + 1] > 0:
                                    self.scored_02 += self.board[i + 1]
                                    diem_cong += self.board[i + 1]
                                    self.board[i + 1] = 0
                                    i = i + 1
                                elif self.board[i + 1] == 0:
                                    break
                                if i >= 11:
                                    i = 0
                                i = i + 1
                            if chieu == "t":
                                if self.board[i - 1] > 0:
                                    self.scored_02 += self.board[i - 1]
                                    diem_cong += self.board[i - 1]
                                    self.board[i - 1] = 0
                                    i = i - 1
                                elif self.board[i + 1] == 0:
                                    break
                                if i <= 0:
                                    i = 11
                                i = i - 1
                        print("người t2 nhận đc: ", diem_cong)
                        print("scored 2: ", self.scored_02)

                    an_da(self)

        self.print_board()
        score1 = self.board[5]
        score2 = self.board[11]
        print("Kết thúc trò chơi!")
        print("Điểm người chơi 1:", score1)
        print("Điểm người chơi 2:", score2)
        if score1 > score2:
            print("Người chơi 1 thắng!")
        elif score2 > score1:
            print("Người chơi 2 thắng!")
        else:
            print("Hòa!")

# Tạo trò chơi và bắt đầu chơi
game = OAnQuan()
game.play_game()