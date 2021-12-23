from aoc import Aoc
import itertools
import math
import re
import sys

# Day 23
# https://adventofcode.com/2021

class Day23Solution(Aoc):

    def Run(self):
        self.StartDay(23, "Amphipod")
        self.ReadInput()
        self.PartA()
        self.PartB()

    def Test(self):
        self.StartDay(23)

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
        #############
        #...........#
        ###B#C#B#D###
        ###A#D#C#A#
        ###########
        """
        self.inputdata = [line.strip() for line in testdata.strip().split("\n")]
        return 12521

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

    def PartA(self):
        self.StartPartA()

        costs = {
            "A": 1,
            "B": 10,
            "C": 100,
            "D": 1000
        }

        answer = None

        # Attempt 1: 16058 is too high
        # Attempt 2: 15958 is too high
        # Attempt 3: 15938 is too high
        # Attempt 4: 15324 not correct

        self.ShowAnswer(answer)

    def PartB(self):
        self.StartPartB()

        # Add solution here

        answer = None

        self.ShowAnswer(answer)


if __name__ == "__main__":
    solution = Day23Solution()
    if len(sys.argv) >= 2 and sys.argv[1] == "test":
        solution.Test()
    else:
        solution.Run()

# Template Version 1.3

