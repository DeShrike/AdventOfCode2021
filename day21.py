from aoc import Aoc
import itertools
import math
import re
import sys

# Day 21
# https://adventofcode.com/2021

class Day21Solution(Aoc):

    def Run(self):
        self.StartDay(21, "Dirac Dice")
        self.ReadInput()
        self.PartA()
        self.PartB()

    def Test(self):
        self.StartDay(21)

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
        Player 1 starting position: 4
        Player 2 starting position: 8
        """
        self.inputdata = [line.strip() for line in testdata.strip().split("\n")]
        return 739785

    def TestDataB(self):
        self.inputdata.clear()
        self.TestDataA()
        return 444356092776315

    def GetRoll(self, dice:int):
        roll = 0
        roll += (dice + 1)
        dice = (dice + 1) % 100
        roll += (dice + 1)
        dice = (dice + 1) % 100
        roll += (dice + 1)
        dice = (dice + 1) % 100
        return roll, dice

    def GetQuantumRoll(self, dice:int):
        roll = 0
        roll += (dice + 1)
        dice = (dice + 1) % 3
        roll += (dice + 1)
        dice = (dice + 1) % 3
        roll += (dice + 1)
        dice = (dice + 1) % 3
        return roll, dice

    def PartA(self):
        self.StartPartA()

        answer = None
        pos1 = int(self.inputdata[0].split(" ")[-1]) - 1
        pos2 = int(self.inputdata[1].split(" ")[-1]) - 1
        score1 = 0
        score2 = 0
        dice = 0
        rollcount = 0
        turn1 = True
        while True:
            roll, dice = self.GetRoll(dice)
            rollcount += 3
            if turn1:
                pos1 = (pos1 + roll) % 10
                score1 += (pos1 + 1)
                if score1 >= 1000:
                    answer = rollcount * score2
                    break
            else:
                pos2 = (pos2 + roll) % 10
                score2 += (pos2 + 1)
                if score2 >= 1000:
                    answer = rollcount * score1
                    break
            turn1 = not turn1

        self.ShowAnswer(answer)

    def PlayDiracDice(self, startpos, d1:int, d2:int, d3:int):
        pos = startpos
        score = 0
        rollcount = 0
        while score < 21:
            pass

    def PartB(self):
        self.StartPartB()

        answer = None
        pos1 = int(self.inputdata[0].split(" ")[-1]) - 1
        pos2 = int(self.inputdata[1].split(" ")[-1]) - 1
        score1 = 0
        score2 = 0
        dice = 0
        rollcount = 0
        turn1 = True
        while True:
            roll, dice = self.GetQuantumRoll(dice)
            rollcount += 3
            if turn1:
                pos1 = (pos1 + roll) % 10
                score1 += (pos1 + 1)
                print(f"P1: R:{roll} P:{pos1} S:{score1}")
                if score1 >= 21:
                    answer = rollcount * score2
                    break
            else:
                pos2 = (pos2 + roll) % 10
                score2 += (pos2 + 1)
                print(f"P2: R:{roll} P:{pos2} S:{score2}")
                if score2 >= 21:
                    answer = rollcount * score1
                    break
            turn1 = not turn1

        self.ShowAnswer(answer)


if __name__ == "__main__":
    solution = Day21Solution()
    if len(sys.argv) >= 2 and sys.argv[1] == "test":
        solution.Test()
    else:
        solution.Run()

# Template Version 1.3

