from aoc import Aoc
from canvas import Canvas
import itertools
import math
import re
import sys

# Day 9
# https://adventofcode.com/2021

class FloodFill():

    directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]

    def __init__(self, m):
        self.field = m
        self.points = []
        self.height = len(self.field)
        self.width = len(self.field[0])

    def Run(self, startx, starty):
        self.startx = startx
        self.starty = starty

        self.points = []
        q = []
        q.append((startx, starty))

        while True:
            newposses = []
            increased = False
            for qq in q:
                curx = qq[0]
                cury = qq[1]

                for d in self.directions:
                    nx = curx + d[0]
                    ny = cury + d[1]
                    if nx < 0 or ny < 0 or nx >= self.width or ny >= self.height:
                        continue
                    if self.field[ny][nx] != "9" and (nx, ny) not in self.points:
                        self.points.append((nx, ny))
                        increased = True
                        q.append((nx, ny))

            if not increased:
                break

        return self.points


class Day9Solution(Aoc):

    def Run(self):
        self.StartDay(9, "Smoke Basin")
        self.ReadInput()
        self.PartA()
        self.PartB()

    def Test(self):
        self.StartDay(9)

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
        2199943210
        3987894921
        9856789892
        8767896789
        9899965678
        """
        self.inputdata = [line.strip() for line in testdata.strip().split("\n")]
        return 15

    def TestDataB(self):
        self.inputdata.clear()
        self.TestDataA()
        return 1134

    def CreatePNG(self, cellsize:int = 1):
        print("Creating PNG")
        width = len(self.inputdata[0]) * cellsize
        height = len(self.inputdata) * cellsize
        canvas = Canvas(width, height)

        ff = FloodFill(self.inputdata)
        lowpoints = self.FindLowPointsB()
        for lp in lowpoints:
            fieldpoints = ff.Run(*lp)
            for fp in fieldpoints:
                h = int(self.inputdata[fp[1]][fp[0]]) + 1
                self.SetPixel(canvas, cellsize, *fp, (255 // h, 255 // h, 255 // h))
            self.SetPixel(canvas, cellsize, *lp, (255, 255, 255))
        canvas.save_PNG("day9.png")

    def SetPixel(self, canvas, cellsize:int, x:int, y:int, color):
        for xx in range(x * cellsize, (x + 1) * cellsize + 1):
            for yy in range(y * cellsize, (y + 1) * cellsize + 1):
                canvas.set_pixel(xx, yy, color)

    def GetNeighbours(self, x:int, y:int):
        n = []
        if y > 0:
            n.append(int(self.inputdata[y - 1][x]))
        if x > 0:
            n.append(int(self.inputdata[y][x - 1]))
        if y < len(self.inputdata) - 1:
            n.append(int(self.inputdata[y + 1][x]))
        if x < len(self.inputdata[0]) - 1:
            n.append(int(self.inputdata[y][x + 1]))
        return n

    def FindLowPointsA(self):
        width = len(self.inputdata[0])
        height = len(self.inputdata)
        lowpoints = []
        for x in range(width):
            for y in range(height):
                current = int(self.inputdata[y][x])
                n = self.GetNeighbours(x, y)
                if all([num > current for num in n]):
                    lowpoints.append(current)
        return lowpoints

    def FindLowPointsB(self):
        width = len(self.inputdata[0])
        height = len(self.inputdata)
        lowpoints = []
        for x in range(width):
            for y in range(height):
                current = int(self.inputdata[y][x])
                n = self.GetNeighbours(x, y)
                if all([num > current for num in n]):
                    lowpoints.append((x, y))
        return lowpoints

    def PartA(self):
        self.StartPartA()

        answer = sum([lp + 1 for lp in self.FindLowPointsA()])

        self.ShowAnswer(answer)

    def PartB(self):
        self.StartPartB()

        ff = FloodFill(self.inputdata)
        lowpoints = self.FindLowPointsB()
        sizes = list(sorted([len(ff.Run(*lp)) for lp in lowpoints], reverse=True))

        answer = sizes[0] * sizes[1] * sizes[2]

        self.ShowAnswer(answer)
        self.CreatePNG(3)


if __name__ == "__main__":
    solution = Day9Solution()
    if len(sys.argv) >= 2 and sys.argv[1] == "test":
        solution.Test()
    else:
        solution.Run()

# Template Version 1.3

