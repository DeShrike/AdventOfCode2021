from aoc import Aoc
import itertools
import math
import re
import sys

# Day 24
# https://adventofcode.com/2021

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
        inp w
        add z w
        mod z 2
        div w 2
        add y w
        mod y 2
        div w 2
        add x w
        mod x 2
        div w 2
        mod w 2
        """
        self.inputdata = [line.strip() for line in testdata.strip().split("\n")]
        return None

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

    def PartA(self):
        self.StartPartA()

        answer = None
        program = [line.split(" ") for line in self.inputdata]
        alu = Alu(program)

        """
        digits = ["9" for _ in range(14)]
        for _ in range(10):
            for dix in range(14):
                mi = 1e20
                mix = None
                for v in range(9, 0, -1):
                    digits[dix] = str(v)

                    num = "".join(digits)
                    alu.Run(num)
                    if alu.z < mi:
                        mi = alu.z
                        mix = v
                    if alu.z < 10:
                        print(f"{num}\t{alu.w}\t{alu.x}\t{alu.y}\t{alu.z}")

                if alu.z == 0:
                    break
                digits[dix] = str(mix)

        print("Next Step")

        for ii in range(11, 100):
            digits[0] = str(ii // 10)
            digits[1] = str(ii % 10)
            for dix in range(2, 14):
                mem = digits[dix]
                for v in range(9, 0, -1):
                    digits[dix] = str(v)

                    num = "".join(digits)
                    alu.Run(num)
                    if alu.z < 10:
                        print(f"{num}\t{alu.w}\t{alu.x}\t{alu.y}\t{alu.z}")
                    digits[dix] = mem
                if alu.z == 0:
                    break
                digits[dix] = str(mix)

        """
        digits = ["1", "9", "9", "2", "9", "9", "9", "4", "2", "9", "3", "9", "6", "9"]
        for ii in range(1, 10):
            for dix in range(2, 14):
                mem = digits[dix]
                for v in range(9, 0, -1):
                    digits[dix] = str(v)

                    num = "".join(digits)
                    alu.Run(num)
                    if alu.z < 10:
                        print(f"{num}\t{alu.w}\t{alu.x}\t{alu.y}\t{alu.z}")
                    digits[dix] = mem
                if alu.z == 0:
                    answer = num
                    break
                digits[dix] = mem
        """
        parts = ["19", "29", "39", "49", "59", "69", "79", "89", "99", "98", "97", "96", "95", "94", "93", "92", "91"]
        for d in itertools.permutations(parts, 7):
            num = "".join(d)
            alu.Run(num)
            if alu.z < 10000:
                print(f"{num}\t{alu.w}\t{alu.x}\t{alu.y}\t{alu.z}")
            if alu.z == 0:
                break
        """
        """
        parts = ["19", "29", "39", "49", "59", "69", "79", "89", "99", "98", "97", "96", "95", "94", "93", "92", "91"]
        groups = ["19", "92", "99", "94", "29", "39", "69"]

        for g in range(len(groups)):
            mem = groups[g]
            for p in parts:
                groups[g] = p
                num = "".join(groups)
                    alu.Run(num)
                if alu.z < 100:
                    print(f"{num}\t{alu.w}\t{alu.x}\t{alu.y}\t{alu.z}")
                if alu.z == 0:
                    break
            groups[g] = mem
        """

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

