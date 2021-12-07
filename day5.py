from aoc import Aoc
import itertools
import math
import re
import sys
from collections import defaultdict

# Day 5
# https://adventofcode.com/2021

class Day5Solution(Aoc):

    def Run(self):
        self.StartDay(5, "Hydrothermal Venture")
        self.ReadInput()
        self.PartA()
        self.PartB()

    def Test(self):
        self.StartDay(5)

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
        0,9 -> 5,9
        8,0 -> 0,8
        9,4 -> 3,4
        2,2 -> 2,1
        7,0 -> 7,4
        6,4 -> 2,0
        0,9 -> 2,9
        3,4 -> 1,4
        0,0 -> 8,8
        5,5 -> 8,2
        """
        self.inputdata = [line.strip() for line in testdata.strip().split("\n")]
        return 5

    def TestDataB(self):
        self.inputdata.clear()
        self.TestDataA()
        return 12

    def ParseInput(self):
        lines = []
        rx1 = re.compile(f"(?P<x1>[0-9]*),(?P<y1>[0-9]*) -> (?P<x2>[0-9]*),(?P<y2>[0-9]*)")
        for line in self.inputdata:
            match = rx1.search(line)
            if match:
                x1 = int(match["x1"])
                y1 = int(match["y1"])
                x2 = int(match["x2"])
                y2 = int(match["y2"])
                lines.append((x1, y1, x2, y2))
        return lines

    def PlotLine(self, coords, line):
        if line[0] == line[2]:
            # Vertical
            dy = -1 if line[1] > line[3] else 1
            for y in range(line[1], line[3] + dy, dy):
                pos = (line[0], y)
                coords[pos] += 1
        elif line[1] == line[3]:
            # Horizonal
            dx = -1 if line[0] > line[2] else 1
            for x in range(line[0], line[2] + dx, dx):
                pos = (x, line[1])
                coords[pos] += 1
        else:
            # Diagonal
            dx = -1 if line[0] > line[2] else 1
            dy = -1 if line[1] > line[3] else 1
            for x, y in zip(range(line[0], line[2] + dx, dx), range(line[1], line[3] + dy, dy)):
                pos = (x, y)
                coords[pos] += 1

    def PartA(self):
        self.StartPartA()

        lines = self.ParseInput()
        coords = defaultdict(int)
        for line in lines:
            if line[0] == line[2] or line[1] == line[3]:
                self.PlotLine(coords, line)

        answer = len([key for (key, value) in coords.items() if value > 1])

        self.ShowAnswer(answer)

    def PartB(self):
        self.StartPartB()

        lines = self.ParseInput()
        coords = defaultdict(int)
        for line in lines:
            self.PlotLine(coords, line)

        answer = len([key for (key, value) in coords.items() if value > 1])

        self.ShowAnswer(answer)


if __name__ == "__main__":
    solution = Day5Solution()
    if len(sys.argv) >= 2 and sys.argv[1] == "test":
        solution.Test()
    else:
        solution.Run()

# Template Version 1.2
