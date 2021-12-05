#!/usr/bin/env python3

import sys

board_dimension = 5

class Number:
    def __init__(self, value):
        self.value = value
        self.is_marked = False

    def mark(self):
        self.is_marked = True

class Board:
    def __init__(self, numbers):
        self.numbers = list(map(lambda x: Number(x), numbers))
        self.has_won = False
        self.won_in_round = -1
        self.winning_number = -1

    def __str__(self):
        result = ''
        for i in range(len(self.numbers)):
            if self.numbers[i].is_marked:
                result += u"\u001b[31m"
            result += str(self.numbers[i].value).rjust(2, ' ') + ' '
            if self.numbers[i].is_marked:
                result += u"\u001b[0m"
            if i % board_dimension == 4:
                result += '\n'

        return result

    def sum_of_unmarked_numbers(self):
        return sum(n.value for n in self.numbers if not n.is_marked)

    def index_to_coords(self, index):
        x = index % board_dimension
        y = index // board_dimension

        return (x, y)

    def number_at(self, x, y):
        return self.numbers[y*board_dimension+x]

    def check_for_win(self, index):
        (x, y) = self.index_to_coords(index)

        is_win = True

        # check for vertical win
        for i in range(board_dimension):
            if not self.number_at(x, i).is_marked:
                is_win = False
                break

        if is_win:
            return True

        is_win = True

        # check for horizontal win
        for i in range(board_dimension):
            if not self.number_at(i, y).is_marked:
                is_win = False
                break

        return is_win

    def mark_number(self, number):
        indices_of_number = [i for i,n in enumerate(self.numbers) if n.value == number]

        for i in indices_of_number:
            self.numbers[i].mark()

        for i in indices_of_number:
            if self.check_for_win(i):
                self.winning_number = number
                return True

        return False


if len(sys.argv) != 2:
    print("Expected one argument but got %d" % (len(sys.argv) - 1))
    exit(1)

filename = sys.argv[1]

with open(filename) as file:
    lines = file.readlines()

drawn_numbers = list(map(int, lines[0].split(',')))

board_input = lines[2:]

current_board_numbers = []
boards = []

for line in board_input:
    if line == "\n":
        boards.append(Board(current_board_numbers))
        current_board_numbers = []
        continue
    
    current_board_numbers.extend(list(map(int, line.split())))

boards.append(Board(current_board_numbers))

for round_index, drawn_number in enumerate(drawn_numbers):
    for i, board in enumerate(b for b in boards if not b.has_won):
        is_win = board.mark_number(drawn_number)
        if is_win:
            board.has_won = True
            board.won_in_round = round_index

boards.sort(key=lambda b: b.won_in_round, reverse=True)

board = boards[0]

sum_of_unmarked_numbers = board.sum_of_unmarked_numbers()
print(board)
print("Sum of unmarked numbers: %d" % sum_of_unmarked_numbers)
print("Winning number: %d" % board.winning_number)
print("Result: %d" % (sum_of_unmarked_numbers * board.winning_number))

