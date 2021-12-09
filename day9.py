from aoc import Aoc
import itertools
import math
import re
import sys

# Day 9
# https://adventofcode.com/2021

class Day9Solution(Aoc):

    def Run(self):
        self.StartDay(9, "Smoke Basin")
        self.ReadInput()
        self.PartA()
        self.PartB()

    def Test(self):
        self.StartDay(9)

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
        2199943210
        3987894921
        9856789892
        8767896789
        9899965678
        """
        self.inputdata = [line.strip() for line in testdata.strip().split("\n")]
        return 15

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

    def GetNeighbours(self, x:int, y:int):
        n = []
        if y > 0:
            n.append(int(self.inputdata[y - 1][x]))
        if x > 0:
            n.append(int(self.inputdata[y][x - 1]))
        if y < len(self.inputdata) - 1:
            n.append(int(self.inputdata[y + 1][x]))
        if x < len(self.inputdata[0]) - 1:
            n.append(int(self.inputdata[y][x + 1]))
        return n

    def PartA(self):
        self.StartPartA()

        width = len(self.inputdata[0])
        height = len(self.inputdata)
        lowpoints = []
        for x in range(width):
            for y in range(height):
                current = int(self.inputdata[y][x])
                n = self.GetNeighbours(x, y)
                if all([num > current for num in n]):
                    lowpoints.append(current)
        answer = sum([lp + 1 for lp in lowpoints])
        print(lowpoints)
        self.ShowAnswer(answer)

    def PartB(self):
        self.StartPartB()

        # Add solution here

        answer = None

        self.ShowAnswer(answer)


if __name__ == "__main__":
    solution = Day9Solution()
    if len(sys.argv) >= 2 and sys.argv[1] == "test":
        solution.Test()
    else:
        solution.Run()

# Template Version 1.3

