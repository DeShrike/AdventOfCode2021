from aoc import Aoc
import itertools
import math
import re
import sys

# Day 17
# https://adventofcode.com/2021

class Day17Solution(Aoc):

    def Run(self):
        self.StartDay(17, "Trick Shot")
        self.ReadInput()
        self.PartA()
        self.PartB()

    def Test(self):
        self.StartDay(17)

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
        target area: x=20..30, y=-10..-5
        """
        self.inputdata = [line.strip() for line in testdata.strip().split("\n")]
        return 45

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

    def ParseInput(self):
        rx1 = re.compile(f"target area: x=(?P<x1>[\-0-9]*)..(?P<x2>[\-0-9]*), y=(?P<y1>[\-0-9]*)..(?P<y2>[\-0-9]*)")
        match = rx1.search(self.inputdata[0])
        if match:
            x1 = int(match["x1"])
            x2 = int(match["x2"])
            y1 = int(match["y1"])
            y2 = int(match["y2"])
            return x1, y1, x2, y2
        return None

    def Shoot(self, vx:int, vy:int) -> int:
        x, y = 0, 0
        maxy = 0
        while y > self.ty2:
            x += vx
            y += vy
            vx = max(0, vx - 1)
            vy -= 1
            maxy = max(maxy, y)
            if self.tx1 <= x <= self.tx2 and self.ty1 <= y <= self.ty2:
                return maxy
        return None

    def PartA(self):
        self.StartPartA()

        self.tx1, self.ty1, self.tx2, self.ty2 = self.ParseInput()
        print(f"T: {self.tx1},{self.ty1} - {self.tx2}, {self.ty2}")
        maxy = 0
        for vx, vy in itertools.product(range(100), range(100)):
            highy = self.Shoot(vx, vy)
            if highy is not None:
                maxy = max(maxy, highy)
                if maxy == highy:
                    print(f"Velocity {vx},{vy} -> {highy} {'MAX' if maxy == highy else ''}")

        answer = maxy

        # Attempt 1: 4950 is too high
        # Attempt 2: 2278 is Correct

        self.ShowAnswer(answer)

    def PartB(self):
        self.StartPartB()

        # Add solution here

        answer = None

        self.ShowAnswer(answer)


if __name__ == "__main__":
    solution = Day17Solution()
    if len(sys.argv) >= 2 and sys.argv[1] == "test":
        solution.Test()
    else:
        solution.Run()

# Template Version 1.3

