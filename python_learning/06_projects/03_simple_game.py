2
"""
项目3: 简单猜数字游戏
实战练习：随机数生成、循环、条件判断、异常处理
"""

import random
from datetime import datetime


class GuessNumberGame:
    """猜数字游戏"""

    def __init__(self, min_num=1, max_num=100, max_attempts=10):
        self.min_num = min_num
        self.max_num = max_num
        self.max_attempts = max_attempts
        self.secret_number = 0
        self.attempts = 0
        self.history = []

    def start_new_game(self):
        """开始新游戏"""
        self.secret_number = random.randint(self.min_num, self.max_num)
        self.attempts = 0
        self.history = []
        print(f"\n猜数字游戏开始！")
        print(f"范围: {self.min_num} - {self.max_num}")
        print(f"最多尝试次数: {self.max_attempts}")

    def make_guess(self, guess):
        """进行猜测"""
        self.attempts += 1

        # 验证输入
        if not self.min_num <= guess <= self.max_num:
            return False, f"数字必须在 {self.min_num} 到 {self.max_num} 之间"

        # 记录猜测历史
        self.history.append(guess)

        # 检查是否猜中
        if guess == self.secret_number:
            return True, f"恭喜！你用 {self.attempts} 次猜对了数字 {self.secret_number}！"
        elif guess < self.secret_number:
            return False, f"太小了！还剩 {self.max_attempts - self.attempts} 次机会"
        else:
            return False, f"太大了！还剩 {self.max_attempts - self.attempts} 次机会"

    def print_history(self):
        """打印猜测历史"""
        if not self.history:
            return

        print("\n猜测历史:")
        for i, guess in enumerate(self.history, 1):
            hint = ""
            if guess < self.secret_number:
                hint = "(太小)"
            elif guess > self.secret_number:
                hint = "(太大)"
            else:
                hint = "(正确!)"
            print(f"  {i}. {guess} {hint}")

    def is_game_over(self):
        """游戏是否结束"""
        return self.attempts >= self.max_attempts or (self.history and self.history[-1] == self.secret_number)

    def get_stats(self):
        """获取统计信息"""
        return {
            "attempts": self.attempts,
            "max_attempts": self.max_attempts,
            "secret": self.secret_number,
            "history": self.history.copy()
        }


class TicTacToe:
    """井字棋游戏"""

    def __init__(self):
        self.board = [" " for _ in range(9)]
        self.current_player = "X"

    def print_board(self):
        """打印棋盘"""
        print("\n" + "-" * 11)
        for i in range(3):
            print(f"| {self.board[i*3]} | {self.board[i*3+1]} | {self.board[i*3+2]} |")
            print("-" * 11)

    def make_move(self, position):
        """落子"""
        if not 1 <= position <= 9:
            return False, "位置必须在1-9之间"
        if self.board[position - 1] != " ":
            return False, "该位置已有棋子"

        self.board[position - 1] = self.current_player
        return True, None

    def check_winner(self):
        """检查是否有赢家"""
        # 赢的组合
        winning_combos = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # 横向
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # 纵向
            [0, 4, 8], [2, 4, 6]              # 斜向
        ]

        for combo in winning_combos:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != " ":
                return self.board[combo[0]]

        return None

    def is_board_full(self):
        """棋盘是否已满"""
        return " " not in self.board

    def switch_player(self):
        """切换玩家"""
        self.current_player = "O" if self.current_player == "X" else "X"

    def reset(self):
        """重置游戏"""
        self.board = [" " for _ in range(9)]
        self.current_player = "X"


def play_guess_number():
    """玩猜数字游戏"""
    game = GuessNumberGame(min_num=1, max_num=100, max_attempts=10)
    game.start_new_game()

    while not game.is_game_over():
        try:
            guess = int(input(f"\n输入你的猜测 (1-100): "))
            success, message = game.make_guess(guess)
            print(message)
        except ValueError:
            print("请输入有效的数字！")

    # 游戏结束，显示结果
    game.print_history()
    if game.history[-1] != game.secret_number:
        print(f"\n游戏结束！正确答案是 {game.secret_number}")


def play_tictactoe():
    """玩井字棋游戏"""
    game = TicTacToe()
    game.print_board()

    while True:
        print(f"\n玩家 {game.current_player} 的回合")
        try:
            position = int(input("输入位置 (1-9): "))
            success, error = game.make_move(position)
            if not success:
                print(error)
                continue

            game.print_board()

            # 检查是否有赢家
            winner = game.check_winner()
            if winner:
                print(f"\n恭喜！玩家 {winner} 获胜！")
                break

            # 检查是否平局
            if game.is_board_full():
                print("\n平局！")
                break

            game.switch_player()

        except ValueError:
            print("请输入1-9之间的数字！")


def game_menu():
    """游戏菜单"""
    while True:
        print("\n" + "=" * 40)
        print("游戏中心")
        print("=" * 40)
        print("1. 猜数字游戏")
        print("2. 井字棋")
        print("3. 退出")
        print("=" * 40)

        choice = input("选择游戏 (1-3): ")

        if choice == "1":
            play_guess_number()
        elif choice == "2":
            play_tictactoe()
        elif choice == "3":
            print("再见！")
            break
        else:
            print("无效选择，请重新输入")


# 测试代码
if __name__ == "__main__":
    # 启动游戏菜单
    game_menu()
