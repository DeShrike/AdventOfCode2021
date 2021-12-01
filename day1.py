from aoc import Aoc
import itertools
import math
import re
import sys

# Day 1
# https://adventofcode.com/2021

class Day1Solution(Aoc):

    def Run(self):
        self.StartDay(1)
        self.ReadInput()
        self.PartA()
        self.PartB()

    def Test(self):
        self.StartDay(1)

        goal = self.TestDataA()
        self.PartA()
        assert self.GetAnswerA() == goal

        goal = self.TestDataB()
        self.PartB()
        assert self.GetAnswerB() == goal

    def TestDataA(self):
        self.inputdata.clear()
        testdata = \
        """
        199
        200
        208
        210
        200
        207
        240
        269
        260
        263
        """
        self.inputdata = [line.strip() for line in testdata.strip().split("\n")]
        return 7

    def TestDataB(self):
        self.inputdata.clear()
        self.TestDataA()
        return 5

    def PartA(self):
        self.StartPartA()

        numbers = [int(value) for value in self.inputdata]
        answer = len([x for x in range(1, len(numbers)) if numbers[x] > numbers[x - 1] ])

        self.ShowAnswer(answer)

    def PartB(self):
        self.StartPartB()

        numbers = [int(value) for value in self.inputdata]
        groups = [sum(numbers[x:x + 3]) for x in range(0, len(numbers)) if x < len(numbers) - 2]
        answer = len([x for x in range(1, len(groups)) if groups[x] > groups[x - 1] ])

        self.ShowAnswer(answer)


if __name__ == "__main__":
    solution = Day1Solution()
    if len(sys.argv) >= 2 and sys.argv[1] == "test":
        solution.Test()
    else:
        solution.Run()
