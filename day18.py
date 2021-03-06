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

        goal = self.TestDataA1()
        self.PartA()
        self.Assert(self.GetAnswerA(), goal)

        goal = self.TestDataA2()
        self.PartA()
        self.Assert(self.GetAnswerA(), goal)

        goal = self.TestDataB()
        self.PartB()
        self.Assert(self.GetAnswerB(), goal)

    def TestDataA1(self):
        self.inputdata.clear()
        testdata = \
        """
        [[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]
        [[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]
        """
        self.inputdata = [line.strip() for line in testdata.strip().split("\n")]
        return 3993

    def TestDataA2(self):
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
        self.TestDataA2()
        return 3993

    class Snailfish():

        def __init__(self):
            self.l = None
            self.r = None
            self.value = None
            self.parent = None
            self.index = None

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
                sf.r = cls.Parse(line[c + 1:], sf)
            return sf

        @classmethod
        def Create(cls, l, r, parent):
            sf = cls()
            sf.parent = parent
            sf.l = cls.Parse(str(l), sf)
            sf.r = cls.Parse(str(r), sf)
            sf.l.parent = sf
            sf.r.parent = sf
            return sf

        @classmethod
        def CreateSimple(cls, value:int, parent):
            sf = cls()
            sf.value = value
            sf.parent = parent
            return sf

        def __str__(self) -> str:
            if self.value is not None:
                return str(self.value)
            return f"[{self.l},{self.r}]"

        def CalcIndexes(self, pos:int = 0) -> int:
            if self.IsSimpleValue():
                self.index = pos
                pos += 1
            else:
                self.index = None
                pos = self.l.CalcIndexes(pos)
                pos = self.r.CalcIndexes(pos)
            return pos

        def Magnitude(self) -> int:
            if self.value is not None:
                return self.value
            return 3 * self.l.Magnitude() + 2 * self.r.Magnitude()

        def Add(self, rightnumber):
            som = self.Create(self, rightnumber, self.parent)
            som.Reduce()
            return som

        def IsSimplePair(self) -> bool:
            return self.value is None and self.l.value is not None and self.r.value is not None

        def IsSimpleValue(self) -> bool:
            return self.value is not None

        def TryAddToValueWithIndex(self, index:int, value:int):
            if self.IsSimpleValue() and self.index == index:
                self.value += value
                return True
            if self.IsSimpleValue():
                return False
            if self.l.TryAddToValueWithIndex(index, value):
                return True
            if self.r.TryAddToValueWithIndex(index, value):
                return True
            return False

        def AddToValueWithIndex(self, index:int, value:int):
            current = self
            while current.parent is not None:
                current = current.parent
            current.TryAddToValueWithIndex(index, value)

        def Explode(self, level:int = 0) -> bool:
            if level == 0:
                self.CalcIndexes()

            if level == 4 and self.IsSimplePair():
                self.AddToValueWithIndex(self.l.index - 1, self.l.value)
                self.AddToValueWithIndex(self.r.index + 1, self.r.value)

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
                    self.r = self.CreateSimple(r, self)
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
                    changed = changed or True
                changed = changed or self.Split()

    def ParseInput(self):
        numbers = [self.Snailfish.Parse(line, None) for line in self.inputdata]
        return numbers

    def PartA(self):
        self.StartPartA()

        numbers = self.ParseInput()
        som = numbers[0]
        for num in numbers[1:]:
            som = som.Add(num)
            # print(f"{som}")

        print(f"Final Sum:\n{som}")
        answer = som.Magnitude()

        self.ShowAnswer(answer)

    def PartB(self):
        self.StartPartB()

        numbers = self.ParseInput()

        highest = 0
        for a, b in itertools.product(numbers, numbers):
            som = a.Add(b)
            highest = max(highest, som.Magnitude())

        answer = highest

        self.ShowAnswer(answer)


if __name__ == "__main__":
    solution = Day18Solution()
    if len(sys.argv) >= 2 and sys.argv[1] == "test":
        solution.Test()
    else:
        solution.Run()

# Template Version 1.3
