from aoc import Aoc
import sys

# Day 20
# https://adventofcode.com/2021

class Day20Solution(Aoc):

    def Run(self):
        self.StartDay(20, "Trench Map")
        self.ReadInput()
        self.PartA()
        self.PartB()

    def Test(self):
        self.StartDay(20)

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
        ..#.#..#####.#.#.#.###.##.....###.##.#..###.####..#####..#....#..#..##..###..######.###...####..#..#####..##..#.#####...##.#.#..#.##..#.#......#.###.######.###.####...#.##.##..#..#..#####.....#.#....###..#.##......#.....#..#..#..##..#...##.######.####.####.#.#...#.......#..#.#.#...####.##.#......#..#...##.#.##..#...##.#.##..###.#......#.#.......#.#.#.####.###.##...#.....####.#..#..#.##.#....##..#.####....##...##..#...#......#.#.......#.......##..####..#...#.#.#...##..#.#..###..#####........#..####......#..#

        #..#.
        #....
        ##..#
        ..#..
        ..###
        """
        self.inputdata = [line.strip() for line in testdata.strip().split("\n")]
        return 35

    def TestDataB(self):
        self.inputdata.clear()
        self.TestDataA()
        return 3351

    def NineSquareId(self, grid, x:int, y:int) -> int:
        nine = [
            (-1, -1), (0, -1), (1, -1),
            (-1,  0), (0,  0), (1,  0),
            (-1,  1), (0,  1), (1,  1),
        ]
        bits = ""
        width = len(grid[0])
        height = len(grid)
        for dx, dy in nine:
            xx = x + dx
            yy = y + dy
            if xx < 0 or yy < 0 or xx >= width or yy >= height:
                bits += "0"
            else:
                bits += str(grid[yy][xx])
        return int(bits, 2)

    def ParseInput(self):
        algo = [1 if c == "#" else 0 for c in self.inputdata[0]]
        grid = []
        for line in self.inputdata[2:]:
            grid.append([1 if c == "#" else 0 for c in line])
        return algo, grid

    def ExpandGrid(self, grid, count:int):
        for ix, line in enumerate(grid):
            grid[ix] = [0 for _ in range(count)] + line + [0 for _ in range(count)]
        width = len(grid[0])
        for _ in range(count):
            grid.append([0 for _ in range(width)])
            grid.insert(0, [0 for _ in range(width)])
        return grid

    def Enhance(self, grid, algo):
        width = len(grid[0])
        height = len(grid)
        result = [[0 for _ in range(width)] for _ in range(height)]
        padding = 0
        for y in range(padding, height - padding):
            for x in range(padding, width - padding):
                ix = self.NineSquareId(grid, x, y)
                result[y][x] = algo[ix]
        return result

    def PrintGrid(self, grid):
        for line in grid:
            for c in line:
                print("#" if c == 1 else ".", end="")
            print("")
        # a = input()

    def ClearBorder(self, grid):
        width = len(grid[0])
        height = len(grid)
        for x in range(width):
            grid[0][x] = 0
            grid[-1][x] = 0
        for y in range(height):
            grid[y][0] = 0
            grid[y][-1] = 0

    def PartA(self):
        self.StartPartA()

        algo, grid = self.ParseInput()
        grid = self.ExpandGrid(grid, 3)
        grid = self.Enhance(grid, algo)
        grid = self.Enhance(grid, algo)
        self.ClearBorder(grid)
        # self.PrintGrid(grid)

        answer = sum([sum(line) for line in grid])

        self.ShowAnswer(answer)

    def PartB(self):
        self.StartPartB()

        algo, grid = self.ParseInput()
        grid = self.ExpandGrid(grid, 51)
        for i in range(25):
            print(i, end=" ", flush=True)
            grid = self.Enhance(grid, algo)
            grid = self.Enhance(grid, algo)
            self.ClearBorder(grid)
        print("")

        # self.PrintGrid(grid)

        answer = sum([sum(line) for line in grid])

        self.ShowAnswer(answer)


if __name__ == "__main__":
    solution = Day20Solution()
    if len(sys.argv) >= 2 and sys.argv[1] == "test":
        solution.Test()
    else:
        solution.Run()

# Template Version 1.3

