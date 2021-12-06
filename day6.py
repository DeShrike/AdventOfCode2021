from aoc import Aoc
import itertools
import math
import re
import sys

# Day 6
# https://adventofcode.com/2021

class Day6Solution(Aoc):

    def Run(self):
        self.StartDay(6)
        self.ReadInput()
        self.PartA()
        self.PartB()

    def Test(self):
        self.StartDay(6)

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
		3,4,3,1,2
        """
        self.inputdata = [line.strip() for line in testdata.strip().split("\n")]
        return 5934

    def TestDataB(self):
        self.inputdata.clear()
        self.TestDataA()
        return 26984457539

    def Breed(self, days:int) -> int:
        numbers = [int(x) for x in self.inputdata[0].split(",")]
        stages = [len([x for x in numbers if x == d]) for d in range(8 + 1)]
        for day in range(days):
        	pregnant = stages[0]
        	for x in range(1, len(stages)):
        		stages[x - 1] = stages[x]
        		stages[x] = 0
        	stages[6] += pregnant
        	stages[8] += pregnant

        return sum(stages)

    def PartA(self):
        self.StartPartA()

        answer = self.Breed(80)

        self.ShowAnswer(answer)

    def PartB(self):
        self.StartPartB()

        answer = self.Breed(256)

        self.ShowAnswer(answer)


if __name__ == "__main__":
    solution = Day6Solution()
    if len(sys.argv) >= 2 and sys.argv[1] == "test":
        solution.Test()
    else:
        solution.Run()

# Template Version 1.3

