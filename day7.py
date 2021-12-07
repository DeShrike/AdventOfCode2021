from aoc import Aoc
import itertools
import math
import re
import sys

# Day 7
# https://adventofcode.com/2021

class Day7Solution(Aoc):

    def Run(self):
        self.StartDay(7, "The Treachery of Whales")
        self.ReadInput()
        self.PartA()
        # self.PartB()

    def Test(self):
        self.StartDay(7)

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
        16,1,2,0,4,2,7,1,2,14
        """
        self.inputdata = [line.strip() for line in testdata.strip().split("\n")]
        return 37

    def TestDataB(self):
        self.inputdata.clear()
        self.TestDataA()    # If test data is same as test data for part A
        return 168

    def FindBestFuelCost(self, numbers, left:int, right:int) -> int:
        # This does not work !!!!! :(
        cost_left = sum([ abs(left - x) for x in numbers ])
        cost_right = sum([ abs(right - x) for x in numbers ])



        print(f"{left} -> {cost_left}")
        print(f"{right} -> {cost_right}")
        center = (right - left) // 2 + left
        # a = input()
        if cost_left < cost_right:
            return self.FindBestFuelCost(numbers, left, center)
        elif cost_right < cost_left:
            return self.FindBestFuelCost(numbers, center, right)
        else:
            return cost_left

    def PartA(self):
        self.StartPartA()

        numbers = [int(x) for x in self.inputdata[0].split(",")]
        # answer = self.FindBestFuelCost(numbers, min(numbers), max(numbers))

        # Brute forcing it
        costs = {}
        for num in numbers:
            cost = sum([ abs(num - x) for x in numbers ])
            costs[num] = cost
            # print(f"{num} -> {cost}")

        sor = dict(sorted(costs.items(), key=lambda x: x[1]))
        # print(sor)

        answer = list(sor.items())[0][1]

        # Attempt 1: 359696 = too high
        # Attempt 2: 359648 = Correct (Pos 346)

        self.ShowAnswer(answer)

    def PartB(self):
        self.StartPartB()

        print("This will take some time... a few minutes... :(")
        numbers = [int(x) for x in self.inputdata[0].split(",")]
        costs = {}
        for num in range(max(numbers)):
            cost = sum([ sum(range(abs(num - x) + 1)) for x in numbers ])
            costs[num] = cost
        sor = dict(sorted(costs.items(), key=lambda x: x[1]))
        # print(sor)
        answer = list(sor.items())[0][1]

        self.ShowAnswer(answer)


if __name__ == "__main__":
    solution = Day7Solution()
    if len(sys.argv) >= 2 and sys.argv[1] == "test":
        solution.Test()
    else:
        solution.Run()

# Template Version 1.3

