from aoc import Aoc
from collections import Counter
import itertools
import math
import re
import sys

# Day 10
# https://adventofcode.com/2021

class Day10Solution(Aoc):

    def Run(self):
        self.StartDay(10, "Syntax Scoring")
        self.ReadInput()
        self.PartA()
        self.PartB()

    def Test(self):
        self.StartDay(10)

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
        [({(<(())[]>[[{[]{<()<>>
        [(()[<>])]({[<{<<[]>>(
        {([(<{}[<>[]}>{[]{[(<()>
        (((({<>}<{<{<>}{[]{[]{}
        [[<[([]))<([[{}[[()]]]
        [{[{({}]{}}([{[{{{}}([]
        {<[[]]>}<{[{[{[]{()[[[]
        [<(<(<(<{}))><([]([]()
        <{([([[(<>()){}]>(<<{{
        <{([{{}}[<[[[<>{}]]]>[]]
        """
        self.inputdata = [line.strip() for line in testdata.strip().split("\n")]
        return 26397

    def TestDataB(self):
        self.inputdata.clear()
        self.TestDataA()
        return 288957

    def FindError(self, line:str) -> str:
        o = []
        begins = "([{<"
        ends = ")]}>"
        for ix, char in enumerate(line):
            if char in begins:
                o.append(begins.index(char))
            elif char in ends:
                last = o.pop()
                if last != ends.index(char):
                    return char
            else:
                print("????")

        return None

    def PartA(self):
        self.StartPartA()

        scores = {
            ")": 3,
            "]": 57,
            "}": 1197,
            ">": 25137
        }

        errors = Counter([self.FindError(line) for line in self.inputdata])
        answer = sum([count * scores[c] for c, count in errors.items() if c is not None])

        self.ShowAnswer(answer)

    def PartB(self):
        self.StartPartB()

        # Add solution here

        answer = None

        self.ShowAnswer(answer)


if __name__ == "__main__":
    solution = Day10Solution()
    if len(sys.argv) >= 2 and sys.argv[1] == "test":
        solution.Test()
    else:
        solution.Run()

# Template Version 1.3

