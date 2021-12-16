from aoc import Aoc
import itertools
import math
import re
import sys

# Day 16
# https://adventofcode.com/2021

class Day16Solution(Aoc):

    hextobin = {
        "0": "0000",
        "1": "0001",
        "2": "0010",
        "3": "0011",
        "4": "0100",
        "5": "0101",
        "6": "0110",
        "7": "0111",
        "8": "1000",
        "9": "1001",
        "A": "1010",
        "B": "1011",
        "C": "1100",
        "D": "1101",
        "E": "1110",
        "F": "1111"
    }

    def Run(self):
        self.StartDay(16, "Packet Decoder")
        self.ReadInput()
        self.PartA()
        self.PartB()

    def Test(self):
        self.StartDay(16)

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
        A0016C880162017C3686B18A3D4780
        """
        self.inputdata = [line.strip() for line in testdata.strip().split("\n")]
        return 31

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

    def HexToBinary(self, data:str) -> str:
        bindata = "".join([self.hextobin[c] for c in data])
        return bindata

    class Packet():
        def __init__(self):
            self.type = 0
            self.version = 0
            self.literal = None
            self.operator = None
            self.children = []
            self.parent = None

        def __repr__(self):
            return f"Packet: (V:{self.version} T:{self.type}) "

        def __str__(self):
            return f"Packet: (V:{self.version} T:{self.type}) "

        @classmethod
        def Decode(cls, bits:str, ix:int, count:int = -1) -> int:
            print(f"Length: {len(bits)} - Start At {ix}  - SubCOunt: {count}")
            packets = []
            while (ix < len(bits) - 1 and count == -1) or (len(packets) < count):
                p = cls()
                packets.append(p)
                p.version = int(bits[ix:ix + 3], 2)
                ix += 3
                p.type = int(bits[ix:ix + 3], 2)
                ix += 3
                print(f"Version {p.version} - Type: {p.type}")
                if p.type == 4: # literal
                    value = ""
                    while True:
                        group = bits[ix:ix + 5]
                        ix += 5
                        value += group[1:]
                        if group[0] == "0":
                            break
                    p.literal = int(value, 2)
                    print(f"  Literal: {p.literal} - Ix: {ix}")
                else:
                    lti = bits[ix]
                    ix += 1
                    if lti == "0": # 15
                        l = int(bits[ix:ix + 15], 2)
                        print(f"  Sublength: {l}")
                        ix += 15
                        subpackets, _ = cls.Decode(bits[ix:ix + l], 0, -1)
                        p.children += subpackets
                        ix += l
                    else:           # 11
                        c = int(bits[ix:ix + 11], 2)
                        print(f"  SubCount: {c}")
                        ix += 11
                        subpackets, ix = cls.Decode(bits, ix, c)
                        p.children += subpackets

            print(f"Return with {len(packets)} packets -  {ix}")
            a = input()
            return packets, ix

        def VersionTotal(self) -> int:
            return sum([c.VersionTotal() for c in self.children]) + self.version

    def PartA(self):
        self.StartPartA()

        bits = self.HexToBinary(self.inputdata[0])
        print(bits)
        roots,  = self.Packet.Decode(bits, 0, -1)
        root.Decode(bits, 0)

        answer = root.VersionTotal()

        self.ShowAnswer(answer)

    def PartB(self):
        self.StartPartB()

        # Add solution here

        answer = None

        self.ShowAnswer(answer)


if __name__ == "__main__":
    solution = Day16Solution()
    if len(sys.argv) >= 2 and sys.argv[1] == "test":
        solution.Test()
    else:
        solution.Run()

# Template Version 1.3

