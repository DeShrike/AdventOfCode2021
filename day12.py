from aoc import Aoc
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

        goal = self.TestDataB()
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

    def MakePaths(self, nodes, start:str) -> None:
        node = nodes[start]
        self.newpath.append(start)
        # print(start, self.newpath)
        # a = input()
        if start == "end":
            self.allpaths.append(self.newpath[:])
            self.newpath.pop()
            return
        for nextnode in node:
            if ord(nextnode[0]) < 97 or nextnode not in self.newpath:
                self.MakePaths(nodes, nextnode)
        self.newpath.pop()

    def PartA(self):
        self.StartPartA()

        self.allpaths = []
        self.newpath = []
        nodes = self.ParseData()
        # print(nodes)
        # print(len(nodes))
        self.MakePaths(nodes, "start")
        answer = len(self.allpaths)

        self.ShowAnswer(answer)

    def PartB(self):
        self.StartPartB()

        # Add solution here

        answer = None

        self.ShowAnswer(answer)


if __name__ == "__main__":
    solution = Day12Solution()
    if len(sys.argv) >= 2 and sys.argv[1] == "test":
        solution.Test()
    else:
        solution.Run()

# Template Version 1.3

