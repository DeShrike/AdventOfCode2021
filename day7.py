from aoc import Aoc
from collections import Counter, defaultdict
import sys

# Day 7
# https://adventofcode.com/2021

class Day7Solution(Aoc):

    def Run(self):
        self.StartDay(7, "The Treachery of Whales")
        self.ReadInput()
        self.PartA()
        self.PartB()

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

    def FindBestFuelCost(self, numbers, left:int, right:int, part:int) -> int:
        if part == 1:
            calcer = lambda num: sum([ abs(num - x) for x in numbers ])
        else:
            tn = lambda num: ((num + 1) * num) // 2
            calcer = lambda num: sum([ tn(abs(num - x)) for x in numbers ])

        cost_left = calcer(left)
        cost_right = calcer(right)

        while cost_left != cost_right:
            # print(f"{left} -> {cost_left}")
            # print(f"{right} -> {cost_right}")
            nleft = left + 1
            nright = right - 1

            cost_nleft = calcer(nleft)
            cost_nright = calcer(nright)

            if cost_nleft < cost_left:
                left = nleft
                cost_left = cost_nleft

            if cost_nright < cost_right:
                right = nright
                cost_right = cost_nright

        return cost_left

    def PartA_Krisje(self):
        self.StartPartA()

        numbers = [int(x) for x in self.inputdata[0].split(",")]

        numbers.sort()
        crabs = dict(Counter(numbers))
        dist = defaultdict(int)
        for crab in range(len(numbers) + 1):
            dist[crab] = sum([abs(crab - c) * crabs[c] for c in crabs if c != crab])
        answer = min(dist.values())
        self.ShowAnswer(answer)

    def PartB_Krisje(self):
        self.StartPartB()

        numbers = [int(x) for x in self.inputdata[0].split(",")]

        numbers.sort()
        crabs = dict(Counter(numbers))
        dist = defaultdict(int)
        for crab in range(len(numbers) + 1):
            dist[crab] = sum([sum(range(abs(crab - c) + 1)) * crabs[c] for c in crabs if c != crab])
        answer = min(dist.values())
        self.ShowAnswer(answer)

    def PartA(self):
        self.StartPartA()

        numbers = [int(x) for x in self.inputdata[0].split(",")]

        a = list(sorted(numbers))
        ix = a[len(numbers) // 2]
        answer = sum([ abs(ix - x) for x in numbers ])

        # Attempt 1: 359696 = too high
        # Attempt 2: 359648 = Correct (Pos 346)

        self.ShowAnswer(answer)

    def PartB(self):
        self.StartPartB()

        print("This will take a few seconds ...")
        numbers = [int(x) for x in self.inputdata[0].split(",")]
        answer = self.FindBestFuelCost(numbers, min(numbers), max(numbers), 2)
        self.ShowAnswer(answer)


if __name__ == "__main__":
    solution = Day7Solution()
    if len(sys.argv) >= 2 and sys.argv[1] == "test":
        solution.Test()
    else:
        solution.Run()

# Template Version 1.3

