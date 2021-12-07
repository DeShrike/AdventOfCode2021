from aoc import Aoc, Ansi
import itertools
import math
import re
import sys

# Template Version 1.2

# Day 4
# https://adventofcode.com/2021

class Day4Solution(Aoc):

    def Run(self):
        self.StartDay(4, "Giant Squid")
        self.ReadInput()
        self.PartA()
        self.PartB()

    def Test(self):
        self.StartDay(4)

        goal = self.TestDataA()
        self.PartA()
        self.Assert(self.GetAnswerA(), goal)

        goal = self.TestDataB()
        self.PartB()
        self.Assert(self.GetAnswerB(), goal)

    def TestDataA(self):
        self.inputdata.clear()
        testdata = \
        """
        7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

        22 13 17 11  0
         8  2 23  4 24
        21  9 14 16  7
         6 10  3 18  5
         1 12 20 15 19

         3 15  0  2 22
         9 18 13 17  5
        19  8  7 25 23
        20 11 10 24  4
        14 21 16 12  6

        14 21 17 24  4
        10 16 15  9 19
        18  8 23 26 20
        22 11 13  6  5
         2  0 12  3  7
        """
        self.inputdata = [line.strip() for line in testdata.strip().split("\n")]
        return 4512

    def TestDataB(self):
        self.inputdata.clear()
        self.TestDataA()
        return 1924

    def ParseInput(self):
        numbers = list(map(int, [num for num in self.inputdata[0].split(",")]))
        boards = []
        boardcount = (len(self.inputdata) - 1) // 6
        for bix in range(boardcount):
            lix = bix * 6 + 2
            board = []
            for line in self.inputdata[lix:lix + 5]:
                board.append(list(map(int, [num for num in line.replace("  "," ").split(" ")])))
            boards.append(board)

        return numbers, boards

    def MarkDraw(self, number, boards):
        for b in boards:
            for l in b:
                for ix, num in enumerate(l):
                    if num == number:
                        l[ix] += 100

    def PrintBoard(self, board):
        for line in board:
            for num in line:
                print(f"{Ansi.BrightYellow}{num - 100:2}{Ansi.Reset} " if num >= 100 else f"{num:2} ", end="")
            print("")

    def CheckWinner(self, boards):
        winners = []
        for b in boards:
            if any([all([c >= 100 for c in l]) for l in b]):
                winners.append(b)
            else:
                b_t = list(zip(*b))
                if any([all([c >= 100 for c in l]) for l in b_t]):
                    winners.append(b)
        return winners

    def PartA(self):
        self.StartPartA()

        answer = None

        numbers, boards = self.ParseInput()
        for draw in numbers:
            self.MarkDraw(draw, boards)
            winners = self.CheckWinner(boards)
            if len(winners) > 0:
                self.PrintBoard(winners[0])
                answer = draw * sum([sum([c for c in l if c < 100]) for l in winners[0]])
                break

        self.ShowAnswer(answer)

    def PartB(self):
        self.StartPartB()

        answer = None

        numbers, boards = self.ParseInput()
        for draw in numbers:
            self.MarkDraw(draw, boards)
            winners = self.CheckWinner(boards)
            for winner in winners:
                if len(boards) == 1:
                    self.PrintBoard(winner)
                    answer = draw * sum([sum([c for c in l if c < 100]) for l in winner])
                    break
                else:
                    boards.remove(winner)
            if answer:
                break

        self.ShowAnswer(answer)


if __name__ == "__main__":
    solution = Day4Solution()
    if len(sys.argv) >= 2 and sys.argv[1] == "test":
        solution.Test()
    else:
        solution.Run()
