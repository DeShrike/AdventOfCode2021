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
            count0, count1 = self.CountBits(self.inputdata, ix)
            gamma = gamma + ("1" if count1 > count0 else "0")
            epsilon = epsilon + ("0" if count1 > count0 else "1")

        answer = int(gamma, 2) * int(epsilon, 2)

        self.ShowAnswer(answer)

    def CountBits(self, data, bitpos: int):
        count0 = len([num for num in data if num[bitpos] == "0"])
        count1 = len([num for num in data if num[bitpos] == "1"])
        return count0, count1

    def PartB(self):
        self.StartPartB()

        numbers = self.inputdata[:]
        while len(numbers) > 1:
            for bitpos in range(len(numbers[0])):
                count0, count1 = self.CountBits(numbers, bitpos)
                if count1 >= count0:
                    numbers = [num for num in numbers if num[bitpos] == "1"]
                else:
                    numbers = [num for num in numbers if num[bitpos] == "0"]
                if len(numbers) == 1:
                    break

        csr = int(numbers[0], 2)

        numbers = self.inputdata[:]
        while len(numbers) > 1:
            for bitpos in range(len(numbers[0])):
                count0, count1 = self.CountBits(numbers, bitpos)
                if count1 < count0:
                    numbers = [num for num in numbers if num[bitpos] == "1"]
                else:
                    numbers = [num for num in numbers if num[bitpos] == "0"]
                if len(numbers) == 1:
                    break

        ogr = int(numbers[0], 2)

        answer = csr * ogr

        self.ShowAnswer(answer)


if __name__ == "__main__":
    solution = Day3Solution()
    if len(sys.argv) >= 2 and sys.argv[1] == "test":
        solution.Test()
    else:
        solution.Run()
