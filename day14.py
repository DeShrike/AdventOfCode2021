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

    def MakePairs(self, template:str):
        pairs = {}
        for ix in range(len(template) - 1):
            pair = template[ix:ix + 2]
            if pair in pairs:
                pairs[pair][0] += 1
                pairs[pair][1] += ix == len(template) - 2
            else:
                pairs[pair] = (1, ix == len(template) - 2)
        return pairs

    def SplitPair(self, key, count, rule, islast:bool, newpairs):
        # print(f"Key: {key}  Count: {count}  Rule: {rule} IsLast: {islast}")
        newkeyleft = key[0] + rule
        newkeyright = rule + key[1]
        # print(f"{newkeyleft} - {newkeyright}")
        if newkeyleft in newpairs:
            newpairs[newkeyleft] = (newpairs[newkeyleft][0] + count, False)
        else:
            newpairs[newkeyleft] = (count, False)

        if newkeyright in newpairs:
            newpairs[newkeyright] = (newpairs[newkeyright][0] + count, islast)
        else:
            newpairs[newkeyright] = (count, islast)

    def DoStepEx(self, pairs, rules):
        newpairs = {}
        for key, data in pairs.items():
            if key in rules:
                count = data[0]
                islast = data[1]
                self.SplitPair(key, count, rules[key], islast, newpairs)
        return newpairs

    def PartB(self):
        self.StartPartB()

        template, rules = self.ParseInput()
        pairs = self.MakePairs(template)
        for _ in range(40):
            pairs = self.DoStepEx(pairs, rules)

        counts = {}
        for pair, data in pairs.items():
            l = pair[0]
            r = pair[1]
            count = data[0]
            islast = data[1]
            if l in counts:
                counts[l] += count
            else:
                counts[l] = count
            if islast:
                if r in counts:
                    counts[r] += count
                else:
                    counts[r] = count
        sortedcounts = sorted(counts.values())
        answer = sortedcounts[-1] - sortedcounts[0] + 1

        self.ShowAnswer(answer)


if __name__ == "__main__":
    solution = Day14Solution()
    if len(sys.argv) >= 2 and sys.argv[1] == "test":
        solution.Test()
    else:
        solution.Run()

# Template Version 1.3

