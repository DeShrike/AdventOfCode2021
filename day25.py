from aoc import Aoc
import itertools
import math
import re
import sys

# Day 25
# https://adventofcode.com/2021

class Day25Solution(Aoc):

    def Run(self):
        self.StartDay(25, "AOC")
        self.ReadInput()
        self.PartA()
        self.PartB()

    def Test(self):
        self.StartDay(25)

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
        v...>>.vv>
        .vv>>.vv..
        >>.>v>...v
        >>v>>.>.v.
        v>v.vv.v..
        >.>>..v...
        .vv..>.>v.
        v.v..>>v.v
        ....v..v.>
        """
        self.inputdata = [line.strip() for line in testdata.strip().split("\n")]
        return 58

    def TestDataB(self):
        self.inputdata.clear()
        # self.TestDataA()    # If test data is same as test data for part A
        testdata = \
        """
        1000
        2000
        3000
        """
        self.inputdata = [line.strip() for line in testdata.strip().split("\n")]
        return None

    def DoStep(self, grid):
        moved = False
        ngrid = [["." for c in row] for row in grid]
        nngrid = [["." for c in row] for row in grid]
        width = len(grid[0])
        height = len(grid)
        for y, row in enumerate(grid):
            for x, pos in enumerate(row):
                if grid[y][x] == "v":
                    ngrid[y][x] = "v"
                elif grid[y][x] == ">":
                    if grid[y][(x + 1) % width] == ".":
                        ngrid[y][(x + 1) % width] = ">"
                        moved = True
                    else:
                        ngrid[y][x] = ">"

        for y, row in enumerate(ngrid):
            for x, pos in enumerate(row):
                if ngrid[y][x] == "v":
                    if ngrid[(y + 1) % height][x] == ".":
                        nngrid[(y + 1) % height][x] = "v"
                        moved = True
                    else:
                        nngrid[y][x] = "v"
                elif ngrid[y][x] == ">":
                    nngrid[y][x] = ">"

        return nngrid, moved

    def PrintGrid(self, grid):
        for row in grid:
            print("".join(row))
        # a = input()

    def PartA(self):
        self.StartPartA()

        grid = [[c for c in line] for line in self.inputdata]
        # self.PrintGrid(grid)
        answer = 0
        while True:
            grid, moved = self.DoStep(grid)
            # self.PrintGrid(grid)
            if not moved:
                break
            answer += 1
            print(answer)

        answer += 1
        self.ShowAnswer(answer)

    def PartB(self):
        self.StartPartB()

        # Add solution here

        answer = None

        self.ShowAnswer(answer)


if __name__ == "__main__":
    solution = Day25Solution()
    if len(sys.argv) >= 2 and sys.argv[1] == "test":
        solution.Test()
    else:
        solution.Run()

# Template Version 1.3

