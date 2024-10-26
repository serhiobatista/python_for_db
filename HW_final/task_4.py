import os
class Cell:
    def __init__(self, num):
        self.num = num
        self.symbol = ' '

class Board:
    def __init__(self):
        self.cells = []
        for i in range(9):
            self.cells.append(Cell(i + 1))

    def display_board(self):
        print(" %s | %s | %s" %(self.cells[0].symbol, self.cells[1].symbol, self.cells[2].symbol))
        print("-------------")
        print(" %s | %s | %s" % (self.cells[3].symbol, self.cells[4].symbol, self.cells[5].symbol))
        print("-------------")
        print(" %s | %s | %s" % (self.cells[6].symbol, self.cells[7].symbol, self.cells[8].symbol))

    def update(self, cell_num, symbol):
        if self.cells[cell_num - 1].symbol == ' ':
            self.cells[cell_num - 1].symbol = symbol
            return True
        else:
            print('Клетка занята.')
            return False

    def is_game_over(self, symbol):
        for i in range(3):
            if self.cells[i * 3].symbol == self.cells[i * 3 + 1].symbol == self.cells[i * 3 + 2].symbol and self.cells[
                i * 3].symbol != ' ':
                return True
        for i in range(3):
            if self.cells[i].symbol == self.cells[i + 3].symbol == self.cells[i + 6].symbol and self.cells[
                i].symbol != ' ':
                return True
        if self.cells[0].symbol == self.cells[4].symbol == self.cells[8].symbol and self.cells[0].symbol != ' ':
            return True
        if self.cells[2].symbol == self.cells[4].symbol == self.cells[6].symbol and self.cells[2].symbol != ' ':
            return True
        for cell in self.cells:
            if cell.symbol == ' ':
                return False
        return True

class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol
        self.score = 0

    def move(self):
        try:
            cell_num = int(input(self.name + ', Введите номер клетки, где вы хотите сделать отметку: '))
            return cell_num
        except ValueError:
            print('Некорректный ввод. Необходимо ввести число.')
            return self.move()


class Game:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.board = Board()
        self.current_player = player1

    def play_turn(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(self.current_player.name + ' ход:\n')
        self.board.display_board()
        cell_num = self.current_player.move()
        while not self.board.update(cell_num, self.current_player.symbol):
            print('Клетка занята другим игроком.')
            cell_num = self.current_player.move()

        if self.board.is_game_over('X') or self.board.is_game_over('O'):
            os.system('cls' if os.name == 'nt' else 'clear')
            print(self.current_player.name + ' wins!\n')
            self.board.display_board()
            self.current_player.score += 1
            return True

        if self.current_player == self.player1:
            self.current_player = self.player2
        else:
            self.current_player = self.player1

        return False

    def play_game(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Начинается новая игра!')
        self.board = Board()
        self.current_player = self.player1
        while not self.board.is_game_over('X') or self.board.is_game_over('O'):
            if self.play_turn():
                break

        print('Score:')
        print(self.player1.name + ': ' + str(self.player1.score))
        print(self.player2.name + ': ' + str(self.player2.score))


while True:
    name1 = input('Введите имя для первого игрока (X): ')
    name2 = input('Введите имя для второго игрока (O): ')
    player1 = Player(name1, 'X')
    player2 = Player(name2, 'O')
    game = Game(player1, player2)
    game.play_game()
