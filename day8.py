from aoc import Aoc
import itertools
import math
import re
import sys

# Day 8
# https://adventofcode.com/2021

class Day8Solution(Aoc):

    def Run(self):
        self.StartDay(8, "Seven Segment Search")
        self.ReadInput()
        self.PartA()
        self.PartB()

    def Test(self):
        self.StartDay(8)

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
        be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
        edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
        fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
        fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
        aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
        fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
        dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
        bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
        egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
        gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce
        """
        self.inputdata = [line.strip() for line in testdata.strip().split("\n")]
        return 26

    def TestDataB(self):
        self.inputdata.clear()
        self.TestDataA()
        return 61229

    def ParseInput(self):
        data = []
        for line in self.inputdata:
            parts = line.split("|")
            inputs = parts[0].strip().split(" ")
            outputs = parts[1].strip().split(" ")
            data.append((inputs, outputs))
        return data

    def MissingLetter(self, s:str) -> str:
        for o in range(7):
            if chr(o + 97) not in s:
                return chr(o + 97)
        return None

    def Decode(self, codes):
        inputs = ["".join(sorted(c)) for c in codes[0]]
        outputs = ["".join(sorted(c)) for c in codes[1]]

        decoded = [None for _ in range(10)]
        decoded[1] = [s for s in inputs if len(s) == 2][0]
        decoded[4] = [s for s in inputs if len(s) == 4][0]
        decoded[7] = [s for s in inputs if len(s) == 3][0]
        decoded[8] = [s for s in inputs if len(s) == 7][0]
        decoded[3] = [s for s in inputs if len(s) == 5 and (decoded[1][0] in s and decoded[1][1] in s)][0]
        decoded[6] = [s for s in inputs if len(s) == 6 and (decoded[1][0] not in s or decoded[1][1] not in s)][0]
        decoded[5] = [s for s in inputs if len(s) == 5 and (self.MissingLetter(decoded[6]) not in s) and (decoded[1][0] not in s or decoded[1][1] not in s)][0]
        decoded[2] = [s for s in inputs if len(s) == 5 and s not in decoded][0]
        decoded[0] = [s for s in inputs if len(s) == 6 and (self.MissingLetter(s) in decoded[4]) and s not in decoded][0]
        decoded[9] = [s for s in inputs if len(s) == 6 and s not in decoded][0]

        d4 = decoded.index(outputs[0])
        d3 = decoded.index(outputs[1])
        d2 = decoded.index(outputs[2])
        d1 = decoded.index(outputs[3])
        number = d1 + (d2 * 10) + (d3 * 100) + (d4 * 1000)
        return number

    def PartA(self):
        self.StartPartA()

        data = self.ParseInput()
        answer = sum([len([x for x in dat[1] if len(x) == 2 or len(x) == 4 or len(x) == 3 or len(x) == 7]) for dat in data])

        self.ShowAnswer(answer)

    def PartB(self):
        self.StartPartB()

        data = self.ParseInput()
        answer = sum([self.Decode(codes) for codes in data])

        # Attempt 1: 1014246 is too low
        # Attempt 2: 1019355 = Correct

        self.ShowAnswer(answer)


if __name__ == "__main__":
    solution = Day8Solution()
    if len(sys.argv) >= 2 and sys.argv[1] == "test":
        solution.Test()
    else:
        solution.Run()

# Template Version 1.3

