from aoc import Aoc, Ansi
import itertools
import math
import re
import sys

# Day 11
# https://adventofcode.com/2021

class Day11Solution(Aoc):

    def Run(self):
        self.StartDay(11, "Dumbo Octopus")
        self.ReadInput()
        self.PartA()
        self.PartB()

    def Test(self):
        self.StartDay(11)

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
        5483143223
        2745854711
        5264556173
        6141336146
        6357385478
        4167524645
        2176841721
        6882881134
        4846848554
        5283751526
        """
        self.inputdata = [line.strip() for line in testdata.strip().split("\n")]
        return 1656

    def TestDataB(self):
        self.inputdata.clear()
        self.TestDataA()
        return 195

    def ShowGrid(self, step, grid):
        if step > 1:
            print(f"{self.MoveCursorUp(13)}", end="")
        print(f"Step {Ansi.BrightGreen}{step}{Ansi.Reset}")
        for y in range(10):
            for x in range(10):
                if grid[y][x] == 0:
                    print(f"{Ansi.BrightYellow}{grid[y][x]}{Ansi.Reset}", end="")
                else:
                    print(grid[y][x], end="")
            print("")
        print("")

    def GetNeighbours(self, x:int, y:int):
        directions = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]
        for d in directions:
            nx = x + d[0]
            ny = y + d[1]
            if nx < 0 or ny < 0 or nx > 9 or ny > 9:
                continue
            yield nx, ny

    def DoStep(self, step, grid) -> int:
        for y in range(10):
            for x in range(10):
                grid[y][x] = grid[y][x] + 1
        flashes = 0
        flashed = True
        while flashed:
            flashed = False
            for y in range(10):
                for x in range(10):
                    if grid[y][x] > 9 and grid[y][x] < 100:
                        flashed = True
                        grid[y][x] = 100
                        for nx, ny in self.GetNeighbours(x, y):
                            grid[ny][nx] += 1

        for y in range(10):
            for x in range(10):
                if grid[y][x] > 9:
                    flashes += 1
                    grid[y][x] = 0

        # self.ShowGrid(step, grid)
        # a = input()
        return flashes

    def PartA(self):
        self.StartPartA()

        grid = [[int(c) for c in line] for line in self.inputdata]
        answer = sum([ self.DoStep(i + 1, grid) for i in range(100)])

        self.ShowAnswer(answer)

    def PartB(self):
        self.StartPartB()

        grid = [[int(c) for c in line] for line in self.inputdata]
        step = 0
        while True:
            step += 1
            if self.DoStep(step, grid) == 100:
                answer = step
                break

        self.ShowAnswer(answer)


if __name__ == "__main__":
    solution = Day11Solution()
    if len(sys.argv) >= 2 and sys.argv[1] == "test":
        solution.Test()
    else:
        solution.Run()

# Template Version 1.3

