from aoc import Aoc
import itertools
import math
import re
import sys

# Day 24
# https://adventofcode.com/2021

"""
inp w       inp w       inp w   inp w   inp w   inp w   inp w   inp w   inp w   inp w   inp w   inp w   inp w   inp w
mul x 0     mul x 0     mul x 0 mul x 0 mul x 0 mul x 0 mul x 0 mul x 0 mul x 0 mul x 0 mul x 0 mul x 0 mul x 0 mul x 0
add x z     add x z     add x z add x z add x z add x z add x z add x z add x z add x z add x z add x z add x z add x z
mod x 26    mod x 26    mod x 26    mod x 26    mod x 26    mod x 26    mod x 26    mod x 26    mod x 26    mod x 26    mod x 26    mod x 26    mod x 26    mod x 26
div z 1     div z 1 div z 1 div z 26    div z 1 div z 1 div z 1 div z 26    div z 1 div z 26    div z 26    div z 26    div z 26    div z 26
add x 13    add x 12    add x 10    add x -11   add x 14    add x 13    add x 12    add x -5    add x 10    add x 0 add x -11   add x -13   add x -13   add x -11
eql x w     eql x w eql x w eql x w eql x w eql x w eql x w eql x w eql x w eql x w eql x w eql x w eql x w eql x w
eql x 0     eql x 0 eql x 0 eql x 0 eql x 0 eql x 0 eql x 0 eql x 0 eql x 0 eql x 0 eql x 0 eql x 0 eql x 0 eql x 0
mul y 0     mul y 0 mul y 0 mul y 0 mul y 0 mul y 0 mul y 0 mul y 0 mul y 0 mul y 0 mul y 0 mul y 0 mul y 0 mul y 0
add y 25    add y 25    add y 25    add y 25    add y 25    add y 25    add y 25    add y 25    add y 25    add y 25    add y 25    add y 25    add y 25    add y 25
mul y x     mul y x mul y x mul y x mul y x mul y x mul y x mul y x mul y x mul y x mul y x mul y x mul y x mul y x
add y 1     add y 1 add y 1 add y 1 add y 1 add y 1 add y 1 add y 1 add y 1 add y 1 add y 1 add y 1 add y 1 add y 1
mul z y     mul z y mul z y mul z y mul z y mul z y mul z y mul z y mul z y mul z y mul z y mul z y mul z y mul z y
mul y 0     mul y 0 mul y 0 mul y 0 mul y 0 mul y 0 mul y 0 mul y 0 mul y 0 mul y 0 mul y 0 mul y 0 mul y 0 mul y 0
add y w     add y w add y w add y w add y w add y w add y w add y w add y w add y w add y w add y w add y w add y w
add y 8     add y 16    add y 4 add y 1 add y 13    add y 5 add y 0 add y 10    add y 7 add y 2 add y 13    add y 15    add y 14    add y 9
mul y x     mul y x mul y x mul y x mul y x mul y x mul y x mul y x mul y x mul y x mul y x mul y x mul y x mul y x
add z y     add z y add z y add z y add z y add z y add z y add z y add z y add z y add z y add z y add z y add z y
"""

class Alu():

    def __init__(self, program):
        self.program = program
        self.w = 0
        self.x = 0
        self.y = 0
        self.z = 0
        self.ip = 0

    @staticmethod
    def IsNumeric(value:str) -> bool:
        result = re.match("[-+]?\d+$", value)
        if result is not None:
            return True
        return False

    def Store(self, reg:str, value:int):
        if reg == "w":
            self.w = value
        elif reg == "x":
            self.x = value
        elif reg == "y":
            self.y = value
        elif reg == "z":
            self.z = value
        else:
            print(f"Bad Register: {reg}")

    def Load(self, reg:str):
        if reg == "w":
            return self.w
        elif reg == "x":
            return self.x
        elif reg == "y":
            return self.y
        elif reg == "z":
            return self.z
        print(f"Bad Register: {reg}")
        return None

    def Eval(self, par2:str):
        if self.IsNumeric(par2):
            return int(par2)
        else:
            return self.Load(par2)

    def Execute(self, instruction):
        mne = instruction[0]
        reg = instruction[1]
        par2 = None if len(instruction) == 2 else instruction[2]

        if mne == "inp":
            self.Store(reg, int(self.input[self.inputix]))
            self.inputix += 1
        elif mne == "add":
            self.Store(reg, self.Load(reg) + self.Eval(par2))
        elif mne == "mul":
            self.Store(reg, self.Load(reg) * self.Eval(par2))
        elif mne == "div":
            self.Store(reg, self.Load(reg) // self.Eval(par2))
        elif mne == "mod":
            self.Store(reg, self.Load(reg) % self.Eval(par2))
        elif mne == "eql":
            self.Store(reg, 1 if self.Load(reg) == self.Eval(par2) else 0)

    def Run(self, number:str) -> bool:
        self.w = 0
        self.x = 0
        self.y = 0
        self.z = 0
        self.ip = 0

        self.input = number
        self.inputix = 0

        for instruction in self.program:
            self.Execute(instruction)

        return self.z == 0

class Day24Solution(Aoc):

    def Run(self):
        self.StartDay(24, "Arithmetic Logic Unit")
        self.ReadInput()
        self.PartA()
        self.PartB()

    def Test(self):
        self.StartDay(24)

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
        """
        self.inputdata = [line.strip() for line in testdata.strip().split("\n")]
        return None

    def TestDataB(self):
        self.inputdata.clear()
        # self.TestDataA()    # If test data is same as test data for part A
        testdata = \
        """
        """
        self.inputdata = [line.strip() for line in testdata.strip().split("\n")]
        return None

    def PartA(self):
        self.StartPartA()

        answer = None
        program = [line.split(" ") for line in self.inputdata]
        alu = Alu(program)

        divz = [ 1   1,  1, 26,  1,  1,  1, 26,  1, 26,  26,  26,  26,  26]
        addx = [13, 12, 10, 11, 14, 13, 12, -5, 10,  0, -11, -13, -13, -11]
        addy = [ 8, 16,  4,  1, 13,  5,  0, 10,  7,  2,  13,  15,  14,   9]

        # num = 19929994293900
        self.ShowAnswer(answer)

    def PartB(self):
        self.StartPartB()

        # Add solution here

        answer = None

        self.ShowAnswer(answer)


if __name__ == "__main__":
    solution = Day24Solution()
    if len(sys.argv) >= 2 and sys.argv[1] == "test":
        solution.Test()
    else:
        solution.Run()

# Template Version 1.3

