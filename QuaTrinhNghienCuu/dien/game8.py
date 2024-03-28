class OAnQuan:
    def __init__(self):
        self.board = [5] * 12  # Bàn cờ với 10 lỗ và 2 lỗ nhà
        self.board[5] = self.board[11] = 10  # Lỗ nhà không có đá
        self.current_player = 0  # Người chơi hiện tại, 0 hoặc 1

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
            def phanphoi(self):
                global stones, i
                if chieu == "t":
                    while stones > 0:
                        if self.current_player == 0 and i == 11:
                            i = 0
                        elif self.current_player == 1 and i == 5:
                            i = 5
                        self.board[i] += 1
                        stones -= 1
                        i = i - 1 #i là ô thứ ...

                    last_hole = i + 1
                elif chieu == "p":
                    while stones > 0:
                        if self.current_player == 0 and i == 11:
                            i = 0
                        elif self.current_player == 1 and i == 5:
                            i = 5
                        self.board[i] += 1
                        stones -= 1
                        i = i + 1  # i là ô thứ ...

                    last_hole = i - 1
            phanphoi(self)
            stones = self.board[hole + stones]
            #bổ sung thuật toán tiếp tục rải quân khi gặp ô > 0 và 2 ô liên tiếp = 0 , mất lượt (ăn ô có gtrij = 0)
            # Kiểm tra điều kiện để ăn đá (sửa)
            '''if self.current_player == 0 and 0 <= last_hole <= 4 and self.board[last_hole] == 1:
                self.board[5] += self.board[last_hole] + self.board[10 - last_hole]
                self.board[last_hole] = self.board[10 - last_hole] = 0
            elif self.current_player == 1 and 6 <= last_hole <= 10 and self.board[last_hole] == 1:
                self.board[11] += self.board[last_hole] + self.board[10 - last_hole]
                self.board[last_hole] = self.board[10 - last_hole] = 0

            # Đổi lượt chơi nếu không phải vào nhà
            if last_hole != 5 and last_hole != 11:
                self.current_player = 1 - self.current_player
            '''

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