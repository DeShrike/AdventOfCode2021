from aoc import Aoc, Ansi
from dijkstra import DoDijkstra
import itertools
import math
import sys

# Day 15
# https://adventofcode.com/2021

class Day15Solution(Aoc):

    def Run(self):
        self.StartDay(15, "Chiton")
        self.ReadInput()
        self.PartA()
        self.PartB()

    def Test(self):
        self.StartDay(15)

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
        1163751742
        1381373672
        2136511328
        3694931569
        7463417111
        1319128137
        1359912421
        3125421639
        1293138521
        2311944581
        """
        self.inputdata = [line.strip() for line in testdata.strip().split("\n")]
        return 40

    def TestDataB(self):
        self.inputdata.clear()
        self.TestDataA()
        return 315

    def PrintGrid(self, path):
        for y, line in enumerate(self.inputdata):
            for x, col in enumerate(line):
                if (x, y) in path:
                    print(f"{Ansi.BrightRed}{col}{Ansi.Reset}", end="")
                else:
                    print(col, end="")
            print("")

    def PartA(self):
        self.StartPartA()

        path = DoDijkstra(self.inputdata)
        self.PrintGrid(path)
        cost = 0
        for p in path[1:]:
            cost += int(self.inputdata[p[1]][p[0]])
        answer = cost

        # Attempt 1: 624 is too high
        # Attempt 2: 620 is too high
        # Attempt 3: 498 is correct

        self.ShowAnswer(answer)

    def Wrap(self, c, steps):
        num = int(c)
        for _ in range(steps):
            num = 1 if num == 9 else num + 1
        return str(num)

    def Increase(self, line:str, steps:int) -> str:
        return "".join([self.Wrap(c, steps) for c in line])

    def PartB(self):
        self.StartPartB()

        height = len(self.inputdata)
        width = len(self.inputdata[0])

        for s in range(4):
            for y in range(height):
                self.inputdata.append(self.Increase(self.inputdata[y], s + 1))

        height = len(self.inputdata)
        for y in range(height):
            line = self.inputdata[y]
            for s in range(4):
                self.inputdata[y] += self.Increase(line, s + 1)

        path = DoDijkstra(self.inputdata)
        # self.PrintGrid(path)
        cost = 0
        for p in path[1:]:
            cost += int(self.inputdata[p[1]][p[0]])
        answer = cost

        self.ShowAnswer(answer)


if __name__ == "__main__":
    solution = Day15Solution()
    if len(sys.argv) >= 2 and sys.argv[1] == "test":
        solution.Test()
    else:
        solution.Run()

# Template Version 1.3

