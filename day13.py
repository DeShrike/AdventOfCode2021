from aoc import Aoc
import itertools
import math
import re
import sys

# Day 13
# https://adventofcode.com/2021

class Day13Solution(Aoc):

    def Run(self):
        self.StartDay(13, "Transparent Origami")
        self.ReadInput()
        self.PartA()
        self.PartB()

    def Test(self):
        self.StartDay(13)

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
        6,10
        0,14
        9,10
        0,3
        10,4
        4,11
        6,0
        6,12
        4,1
        0,13
        10,12
        3,4
        3,0
        8,4
        1,10
        2,14
        8,10
        9,0

        fold along y=7
        fold along x=5
        """
        self.inputdata = [line.strip() for line in testdata.strip().split("\n")]
        return 17

    def TestDataB(self):
        self.inputdata.clear()
        self.TestDataA()
        return None

    def ParseInput(self):
        dots = []       # (x, y)
        folds = []      # (x, None) or (None, y)

        rx1 = re.compile(f"(?P<xx>[0-9]*),(?P<yy>[0-9]*)")
        rx2 = re.compile(f"fold along x=(?P<xx>[0-9]*)")
        rx3 = re.compile(f"fold along y=(?P<yy>[0-9]*)")

        for line in self.inputdata:
            match = rx1.search(line)
            if match:
                dots.append((int(match["xx"]), int(match["yy"])))
                continue
            match = rx2.search(line)
            if match:
                folds.append((int(match["xx"]), None))
                continue
            match = rx3.search(line)
            if match:
                folds.append((None, int(match["yy"])))
                continue

        return dots, folds

    def FoldHorizontal(self, fy:int, dots):
        newdots = []
        for x, y in dots:
            if y > fy:
                dot = (x, y - (y - fy) * 2)
            else:
                dot = (x, y)
            if dot not in newdots:
                newdots.append(dot)
        return newdots

    def Fold(self, fold, dots):
        if fold[1] is None:
            dots_t = [(x[1], x[0]) for x in dots]
            dots_t = self.FoldHorizontal(fold[0], dots_t)
            dots = [(x[1], x[0]) for x in dots_t]
            return dots
        else:
            dots = self.FoldHorizontal(fold[1], dots)
            return dots

    def ShowDots(self, dots):
        width = max([x[0] for x in dots])
        height = max([x[1] for x in dots])
        for y in range(height + 1):
            for x in range(width + 1):
                if (x,y) in dots:
                    print("#", end="")
                else:
                    print(" ", end="")
            print("")

    def PartA(self):
        self.StartPartA()

        dots, folds = self.ParseInput()

        dots = self.Fold(folds[0], dots)
        answer = len(dots)
        self.ShowAnswer(answer)

    def PartB(self):
        self.StartPartB()

        dots, folds = self.ParseInput()

        for fold in folds:
            dots = self.Fold(fold, dots)

        self.ShowDots(dots)
        answer = "CEJKLUGJ"
        self.ShowAnswer(answer)


if __name__ == "__main__":
    solution = Day13Solution()
    if len(sys.argv) >= 2 and sys.argv[1] == "test":
        solution.Test()
    else:
        solution.Run()

# Template Version 1.3

