from aoc import Aoc
import itertools
import math
import re
import sys

# Day 3
# https://adventofcode.com/2021

class Day3Solution(Aoc):

    def Run(self):
        self.StartDay(3)
        self.ReadInput()
        self.PartA()
        self.PartB()

    def Test(self):
        self.StartDay(3)

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
        00100
        11110
        10110
        10111
        10101
        01111
        00111
        11100
        10000
        11001
        00010
        01010
        """
        self.inputdata = [line.strip() for line in testdata.strip().split("\n")]
        return 198

    def TestDataB(self):
        self.inputdata.clear()
        self.TestDataA()
        return 230

    def PartA(self):
        self.StartPartA()

        gamma = ""
        epsilon = ""
        for ix in range(len(self.inputdata[0])):
            count0 = len([x for x in self.inputdata if x[ix] == "0"])
            count1 = len([x for x in self.inputdata if x[ix] == "1"])
            gamma = gamma + ("1" if count1 > count0 else "0")
            epsilon = epsilon + ("0" if count1 > count0 else "1")

        answer = int(gamma, 2) * int(epsilon, 2)

        self.ShowAnswer(answer)

    def PartB(self):
        self.StartPartB()

        lsr = 0
        ogr = 0

        answer = lsr * ogr

        self.ShowAnswer(answer)


if __name__ == "__main__":
    solution = Day3Solution()
    if len(sys.argv) >= 2 and sys.argv[1] == "test":
        solution.Test()
    else:
        solution.Run()
