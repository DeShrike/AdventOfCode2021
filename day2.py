from aoc import Aoc
import itertools
import math
import re
import sys

# Day 2
# https://adventofcode.com/2021

class Day2Solution(Aoc):

    def Run(self):
        self.StartDay(2)
        self.ReadInput()
        self.PartA()
        self.PartB()

    def Test(self):
        self.StartDay(2)

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
		forward 5
		down 5
		forward 8
		up 3
		down 8
		forward 2
        """
        self.inputdata = [line.strip() for line in testdata.strip().split("\n")]
        return 150

    def TestDataB(self):
        self.inputdata.clear()
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

        pos, depth = 0, 0
        for line in self.inputdata:
        	command, count = line.split(" ")
        	if command == "forward":
        		pos += int(count)
        	elif command == "down":
        		depth += int(count)
        	elif command == "up":
        		depth -= int(count)
        answer = pos * depth

        self.ShowAnswer(answer)

    def PartB(self):
        self.StartPartB()

        # Add solution here

        answer = None

        self.ShowAnswer(answer)


if __name__ == "__main__":
    solution = Day2Solution()
    if len(sys.argv) >= 2 and sys.argv[1] == "test":
        solution.Test()
    else:
        solution.Run()
