from aoc import Aoc
from collections import Counter
import itertools
import math
import re
import sys

# Day 12
# https://adventofcode.com/2021

class Day12Solution(Aoc):

    def Run(self):
        self.StartDay(12, "Passage Pathing")
        self.ReadInput()
        self.PartA()
        self.PartB()

    def Test(self):
        self.StartDay(12)

        goal = self.TestDataA1()
        self.PartA()
        self.Assert(self.GetAnswerA(), goal)

        goal = self.TestDataA2()
        self.PartA()
        self.Assert(self.GetAnswerA(), goal)

        goal = self.TestDataA3()
        self.PartA()
        self.Assert(self.GetAnswerA(), goal)

        goal = self.TestDataB1()
        self.PartB()
        self.Assert(self.GetAnswerB(), goal)

        goal = self.TestDataB2()
        self.PartB()
        self.Assert(self.GetAnswerB(), goal)

        goal = self.TestDataB3()
        self.PartB()
        self.Assert(self.GetAnswerB(), goal)

    def TestDataA1(self):
        self.inputdata.clear()
        testdata = \
        """
        start-A
        start-b
        A-c
        A-b
        b-d
        A-end
        b-end
        """
        self.inputdata = [line.strip() for line in testdata.strip().split("\n")]
        return 10

    def TestDataA2(self):
        self.inputdata.clear()
        testdata = \
        """
        dc-end
        HN-start
        start-kj
        dc-start
        dc-HN
        LN-dc
        HN-end
        kj-sa
        kj-HN
        kj-dc
        """
        self.inputdata = [line.strip() for line in testdata.strip().split("\n")]
        return 19

    def TestDataA3(self):
        self.inputdata.clear()
        testdata = \
        """
        fs-end
        he-DX
        fs-he
        start-DX
        pj-DX
        end-zg
        zg-sl
        zg-pj
        pj-he
        RW-he
        fs-DX
        pj-RW
        zg-RW
        start-pj
        he-WI
        zg-he
        pj-fs
        start-RW
        """
        self.inputdata = [line.strip() for line in testdata.strip().split("\n")]
        return 226

    def TestDataB1(self):
        self.inputdata.clear()
        self.TestDataA1()
        return 36

    def TestDataB2(self):
        self.inputdata.clear()
        self.TestDataA2()
        return 103

    def TestDataB3(self):
        self.inputdata.clear()
        self.TestDataA3()
        return 3509

    def ParseData(self):
        v = {}
        for line in self.inputdata:
            n1, n2 = line.split("-")
            if n1 in v:
                v[n1].append(n2)
            else:
                v[n1] = [n2]
            if n2 in v:
                v[n2].append(n1)
            else:
                v[n2] = [n1]
        return v

    def CanEnter1(self, name:str) -> bool:
        if ord(name[0]) < 97:
            return True
        if name not in self.newpath:
            return True
        return False

    def CanEnter2(self, name:str) -> bool:
        if ord(name[0]) < 97:
            return True
        if name not in self.newpath:
            return True

        if (name == "end" or name == "start") and name in self.newpath:
            return False

        if not any([x for x in list(Counter(self.newpath).items()) if ord(x[0][0]) >= 97 and x[1] > 1]):
            return True
        return False

    def MakePaths(self, nodes, start:str, part:int) -> None:
        node = nodes[start]
        self.newpath.append(start)
        if start == "end":
            self.allpaths.append(self.newpath[:])
            self.newpath.pop()
            return
        for nextnode in node:
            if (part == 1 and self.CanEnter1(nextnode)) or (part == 2 and self.CanEnter2(nextnode)):
                self.MakePaths(nodes, nextnode, part)
        self.newpath.pop()

    def ShowStats(self):
        lengths = list(sorted([len(p) for p in self.allpaths]))
        print(f"Paths: {len(lengths)}")
        print(f"Shortest: {lengths[0]} steps")
        print(f"Longest: {lengths[-1]} steps")
        print(f"Average: {sum(lengths) / len(lengths):.2f} steps")

    def PartA(self):
        self.StartPartA()

        self.allpaths = []
        self.newpath = []
        nodes = self.ParseData()
        self.MakePaths(nodes, "start", 1)
        answer = len(self.allpaths)

        self.ShowStats()
        self.ShowAnswer(answer)

    def PartB(self):
        self.StartPartB()

        self.allpaths = []
        self.newpath = []
        nodes = self.ParseData()

        self.MakePaths(nodes, "start", 2)
        answer = len(self.allpaths)

        self.ShowStats()
        self.ShowAnswer(answer)


if __name__ == "__main__":
    solution = Day12Solution()
    if len(sys.argv) >= 2 and sys.argv[1] == "test":
        solution.Test()
    else:
        solution.Run()

# Template Version 1.3

