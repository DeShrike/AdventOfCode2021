from aoc import Aoc
import itertools
import math
import re
import sys

# Day 18
# https://adventofcode.com/2021

class Day18Solution(Aoc):

    def Run(self):
        self.StartDay(18, "Snailfish")
        self.ReadInput()
        self.PartA()
        self.PartB()

    def Test(self):
        self.StartDay(18)

        goal = self.TestDataA0()
        self.PartA()
        self.Assert(self.GetAnswerA(), goal)

        """
        goal = self.TestDataA1()
        self.PartA()
        self.Assert(self.GetAnswerA(), goal)

        goal = self.TestDataA2()
        self.PartA()
        self.Assert(self.GetAnswerA(), goal)

        goal = self.TestDataA3()
        self.PartA()
        self.Assert(self.GetAnswerA(), goal)

        goal = self.TestDataA4()
        self.PartA()
        self.Assert(self.GetAnswerA(), goal)

        goal = self.TestDataA5()
        self.PartA()
        self.Assert(self.GetAnswerA(), goal)
        """
        """
        goal = self.TestDataB()
        self.PartB()
        self.Assert(self.GetAnswerB(), goal)
        """

    def TestDataA0(self):
        self.inputdata.clear()
        testdata = \
        """
        [[[[4,3],4],4],[7,[[8,4],9]]]
        [1,1]
        """
        self.inputdata = [line.strip() for line in testdata.strip().split("\n")]
        return None

    def TestDataA1(self):
        self.inputdata.clear()
        testdata = \
        """
        [[[[1,1],[2,2]],[3,3]],[4,4]]
        """
        self.inputdata = [line.strip() for line in testdata.strip().split("\n")]
        return 445

    def TestDataA2(self):
        self.inputdata.clear()
        testdata = \
        """
        [[1,2],[[3,4],5]]
        """
        self.inputdata = [line.strip() for line in testdata.strip().split("\n")]
        return 143

    def TestDataA3(self):
        self.inputdata.clear()
        testdata = \
        """
        [[[[5,0],[7,4]],[5,5]],[6,6]]
        """
        self.inputdata = [line.strip() for line in testdata.strip().split("\n")]
        return 1137

    def TestDataA4(self):
        self.inputdata.clear()
        testdata = \
        """
        [[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]
        """
        self.inputdata = [line.strip() for line in testdata.strip().split("\n")]
        return 3488

    def TestDataA5(self):
        self.inputdata.clear()
        testdata = \
        """
        [[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]
        [[[5,[2,8]],4],[5,[[9,9],0]]]
        [6,[[[6,2],[5,6]],[[7,6],[4,7]]]]
        [[[6,[0,7]],[0,9]],[4,[9,[9,0]]]]
        [[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]]
        [[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]]
        [[[[5,4],[7,7]],8],[[8,3],8]]
        [[9,3],[[9,9],[6,[4,9]]]]
        [[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]
        [[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]
        """
        self.inputdata = [line.strip() for line in testdata.strip().split("\n")]
        return 4140

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

    class Snailfish():

        def __init__(self):
            self.l = None
            self.r = None
            self.value = None
            self.parent = None
            self.kant = ""

        @staticmethod
        def FindCenter(line:str) -> int:
            o = 0
            for ix, c in enumerate(line):
                if c == "[":
                    o += 1
                elif c == "]":
                    o -= 1
                elif c == ",":
                    if o == 0:
                        return ix
            return None

        @classmethod
        def Parse(cls, line:str, parent):
            sf = cls()
            sf.parent = parent
            if len(line) <= 2:
                sf.value = int(line)
            else:
                line = line[1:-1]
                c = cls.FindCenter(line)
                sf.l = cls.Parse(line[0:c], sf)
                sf.l.kant = "L"
                sf.r = cls.Parse(line[c + 1:], sf)
                sf.r.kant = "R"
            return sf

        @classmethod
        def Create(cls, l, r, parent):
            sf = cls()
            sf.parent = parent
            sf.l = l
            sf.r = r
            l.kant = "L"
            r.kant = "R"
            l.parent = sf
            r.parent = sf
            return sf

        @classmethod
        def CreateSimple(cls, value:int, parent):
            sf = cls()
            sf.value = value
            sf.parent = parent
            return sf

        def __str__(self):
            if self.parent is None:
                if self.value is not None:
                    return "Root:" + str(self.value)
                return f"ROOT[{self.l},{self.r}]"
            if self.value is not None:
                return str(self.value)
            return f"[{self.l},{self.r}]"

            # if self.value is not None:
            #     return self.kant + str(self.value)
            # return f"{self.kant}[{self.l},{self.r}]"

        def Magnitude(self):
            if self.value is not None:
                return self.value
            return 3 * self.l.Magnitude() + 2 * self.r.Magnitude()

        def Add(self, rightnumber):
            som = self.Create(self, rightnumber, self.parent)
            print(f"         Sum: {som}")
            som.Reduce()
            print(f"After Reduce: {som}")
            return som

        def IsSimplePair(self) -> bool:
            return self.value is None and self.l.value is not None and self.r.value is not None

        def IsSimpleValue(self) -> bool:
            return self.value is not None

        def PassToRight(self, value:int):
            print(f"PassToRight {self}")
            n = self
            while not n.IsSimpleValue():
                n = n.l
                print(n)
            print(f"Add {value} to {n.value}")
            n.value += value

        def PassToLeft(self, value:int):
            print(f"PassToLeft {self}")
            n = self
            while not n.IsSimpleValue():
                n = n.r
                print(n)
            print(f"Add {value} to {n.value}")
            n.value += value

        def Explode(self, level:int = 0) -> bool:
            if level == 4 and self.IsSimplePair():
                print(f"Need explode: {self}")
                if self.l.value is None or self.r.value is None:
                    print(f"Bad Explode: {self}")
                    quit()

                a = input()

                # left
                if self.kant == "R":
                    self.parent.l.PassToLeft(self.l.value)
                else:
                    pass
                    # self.parent.r.PassToRight(self.l.value) # ???

                # right
                if self.kant == "L":
                    self.parent.r.PassToRight(self.r.value)
                else:
                    pass
                    # self.parent.l.PassToLeft(self.r.value) # ???

                self.l = None
                self.r = None
                self.value = 0
                return True
            if self.l is not None and self.l.Explode(level + 1):
                return True
            if self.r is not None and self.r.Explode(level + 1):
                return True
            return False

        def Split(self) -> bool:
            if self.value is not None:
                if self.value >= 10:
                    l = self.value // 2
                    r = self.value - l
                    self.l = self.CreateSimple(l, self)
                    self.l.kant = "L"
                    self.r = self.CreateSimple(r, self)
                    self.r.kant = "R"
                    self.value = None
                    return True
            else:
                if self.l.Split():
                    return True
                if self.r.Split():
                    return True
            return False

        def Reduce(self) -> None:
            changed = True
            while changed:
                changed = False
                while self.Explode():
                    print(f"After Explode: {self}")
                    changed = changed or True
                while self.Split():
                    print(f"After Split: {self}")
                    changed = changed or True

    def ParseInput(self):
        numbers = [self.Snailfish.Parse(line, None) for line in self.inputdata]
        return numbers

    def PartA(self):
        self.StartPartA()

        numbers = self.ParseInput()
        som = numbers[0]
        for num in numbers[1:]:
            som = som.Add(num)

        print(f"   Final Sum: {som}")
        answer = som.Magnitude()

        self.ShowAnswer(answer)

    def PartB(self):
        self.StartPartB()

        # Add solution here

        answer = None

        self.ShowAnswer(answer)


if __name__ == "__main__":
    solution = Day18Solution()
    if len(sys.argv) >= 2 and sys.argv[1] == "test":
        solution.Test()
    else:
        solution.Run()

# Template Version 1.3

