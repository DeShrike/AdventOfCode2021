from aoc import Aoc
from collections import Counter
import itertools
import math
import re
import sys

# Day 14
# https://adventofcode.com/2021

class Day14Solution(Aoc):

    def Run(self):
        self.StartDay(14, "AOC")
        self.ReadInput()
        self.PartA()
        self.PartB()

    def Test(self):
        self.StartDay(14)

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
		NNCB

		CH -> B
		HH -> N
		CB -> H
		NH -> C
		HB -> C
		HC -> B
		HN -> C
		NN -> C
		BH -> H
		NC -> B
		NB -> B
		BN -> B
		BB -> N
		BC -> B
		CC -> N
		CN -> C
        """
        self.inputdata = [line.strip() for line in testdata.strip().split("\n")]
        return 1588

    def TestDataB(self):
        self.inputdata.clear()
        self.TestDataA()
        return 2188189693529

    def ParseInput(self):
    	template = self.inputdata[0]
    	rules = {}
    	for line in self.inputdata[2:]:
    		parts = line.split(" -> ")
    		rules[parts[0]] = parts[1]
    	return template, rules

    def DoStep(self, template:str, rules) -> str:
    	newtemplate = ""

    	for ix in range(len(template) - 1):
    		newtemplate += template[ix] + rules[template[ix:ix + 2]]

    	return newtemplate + template[-1]

    def PartA(self):
        self.StartPartA()

        template, rules = self.ParseInput()
        for _ in range(10):
        	template = self.DoStep(template, rules)

        counts = sorted(Counter(template).values())
        answer = counts[-1] - counts[0]

        self.ShowAnswer(answer)

    def PartB(self):
        self.StartPartB()

        # Add solution here

        answer = None

        self.ShowAnswer(answer)


if __name__ == "__main__":
    solution = Day14Solution()
    if len(sys.argv) >= 2 and sys.argv[1] == "test":
        solution.Test()
    else:
        solution.Run()

# Template Version 1.3

