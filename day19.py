from aoc import Aoc
import itertools
import collections
import math
import re
import sys

# Day 19
# https://adventofcode.com/2021

class Scanner():

    # http://www.euclideanspace.com/maths/algebra/matrix/transforms/examples/index.htm
    rotations = [
        ((1, 0, 0),
         (0, 1, 0),
         (0, 0, 1)),

        ((1, 0, 0),
         (0, 0, -1),
         (0, 1, 0)),

        ((1, 0, 0),
         (0, -1, 0),
         (0, 0, -1)),

        ((1, 0, 0),
         (0, 0, 1),
         (0, -1, 0)),

        #
        ((0, -1, 0),
         (1, 0, 0),
         (0, 0, 1)),

        ((0, 0, 1),
         (1, 0, 0),
         (0, 1, 0)),

        ((0, 1, 0),
         (1, 0, 0),
         (0, 0, -1)),

        ((0, 0, -1),
         (1, 0, 0),
         (0, -1, 0)),

        #
        ((-1, 0, 0),
         (0, -1, 0),
         (0, 0, 1)),

        ((-1, 0, 0),
         (0, 0, -1),
         (0, -1, 0)),

        ((-1, 0, 0),
         (0, 1, 0),
         (0, 0, -1)),

        ((-1, 0, 0),
         (0, 0, 1),
         (0, 1, 0)),

        #
        ((0, 1, 0),
         (-1, 0, 0),
         (0, 0, 1)),

        ((0, 0, 1),
         (-1, 0, 0),
         (0, -1, 0)),

        ((0, -1, 0),
         (-1, 0, 0),
         (0, 0, -1)),

        ((0, 0, -1),
         (-1, 0, 0),
         (0, 1, 0)),

        #
        ((0, 0, -1),
         (0, 1, 0),
         (1, 0, 0)),

        ((0, 1, 0),
         (0, 0, 1),
         (1, 0, 0)),

        ((0, 0, 1),
         (0, -1, 0),
         (1, 0, 0)),

        ((0, -1, 0),
         (0, 0, -1),
         (1, 0, 0)),

        #
        ((0, 0, -1),
         (0, -1, 0),
         (-1, 0, 0)),

        ((0, -1, 0),
         (0, 0, 1),
         (-1, 0, 0)),

        ((0, 0, 1),
         (0, 1, 0),
         (-1, 0, 0)),

        ((0, 1, 0),
         (0, 0, -1),
         (-1, 0, 0)),
    ]

    def __init__(self, name):
        self.name = name
        self.beacons = []
        self.pos = [0, 0, 0]
        self.rotationix = 0
        self.posknown = True if name == 0 else False

    def Rotate(self, rotation):
        result = [[0, 0, 0] for _ in self.beacons]
        for i in range(len(self.beacons)):
           for j in range(len(rotation[0])):
              for k in range(len(rotation)):
                 result[i][j] += self.beacons[i][k] * rotation[k][j]
        return result

    def FindOverlap(self, fixedscanner) -> bool:
        for rix, rot in enumerate(self.rotations):
            result = self.Rotate(rot)

            diffs = []
            for x, y in itertools.product(range(len(result)), range(len(fixedscanner.beacons))):
                diff = (result[x][0] - fixedscanner.beacons[y][0], result[x][1] - fixedscanner.beacons[y][1], result[x][2] - fixedscanner.beacons[y][2])
                diffs.append(diff)

            c = dict(collections.Counter(diffs))
            cc = [(di, co) for (di, co) in c.items() if co >= 12]
            if len(cc) > 0:
                di = cc[0][0]
                x = cc[0][1]
                self.rotationsix = rix
                self.beacons = result
                self.pos = [fixedscanner.pos[0] - di[0], fixedscanner.pos[1] - di[1], fixedscanner.pos[2] - di[2]]
                self.posknown = True
                print(f"Scanner {self.name} pos is {self.pos}")
                return True

        return False

class Day19Solution(Aoc):

    def Run(self):
        self.StartDay(19, "Beacon Scanner")
        self.ReadInput()
        self.PartA()
        self.PartB()

    def Test(self):
        self.StartDay(19)

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
        --- scanner 0 ---
        404,-588,-901
        528,-643,409
        -838,591,734
        390,-675,-793
        -537,-823,-458
        -485,-357,347
        -345,-311,381
        -661,-816,-575
        -876,649,763
        -618,-824,-621
        553,345,-567
        474,580,667
        -447,-329,318
        -584,868,-557
        544,-627,-890
        564,392,-477
        455,729,728
        -892,524,684
        -689,845,-530
        423,-701,434
        7,-33,-71
        630,319,-379
        443,580,662
        -789,900,-551
        459,-707,401

        --- scanner 1 ---
        686,422,578
        605,423,415
        515,917,-361
        -336,658,858
        95,138,22
        -476,619,847
        -340,-569,-846
        567,-361,727
        -460,603,-452
        669,-402,600
        729,430,532
        -500,-761,534
        -322,571,750
        -466,-666,-811
        -429,-592,574
        -355,545,-477
        703,-491,-529
        -328,-685,520
        413,935,-424
        -391,539,-444
        586,-435,557
        -364,-763,-893
        807,-499,-711
        755,-354,-619
        553,889,-390

        --- scanner 2 ---
        649,640,665
        682,-795,504
        -784,533,-524
        -644,584,-595
        -588,-843,648
        -30,6,44
        -674,560,763
        500,723,-460
        609,671,-379
        -555,-800,653
        -675,-892,-343
        697,-426,-610
        578,704,681
        493,664,-388
        -671,-858,530
        -667,343,800
        571,-461,-707
        -138,-166,112
        -889,563,-600
        646,-828,498
        640,759,510
        -630,509,768
        -681,-892,-333
        673,-379,-804
        -742,-814,-386
        577,-820,562

        --- scanner 3 ---
        -589,542,597
        605,-692,669
        -500,565,-823
        -660,373,557
        -458,-679,-417
        -488,449,543
        -626,468,-788
        338,-750,-386
        528,-832,-391
        562,-778,733
        -938,-730,414
        543,643,-506
        -524,371,-870
        407,773,750
        -104,29,83
        378,-903,-323
        -778,-728,485
        426,699,580
        -438,-605,-362
        -469,-447,-387
        509,732,623
        647,635,-688
        -868,-804,481
        614,-800,639
        595,780,-596

        --- scanner 4 ---
        727,592,562
        -293,-554,779
        441,611,-461
        -714,465,-776
        -743,427,-804
        -660,-479,-426
        832,-632,460
        927,-485,-438
        408,393,-506
        466,436,-512
        110,16,151
        -258,-428,682
        -393,719,612
        -211,-452,876
        808,-476,-593
        -575,615,604
        -485,667,467
        -680,325,-822
        -627,-443,-432
        872,-547,-609
        833,512,582
        807,604,487
        839,-516,451
        891,-625,532
        -652,-548,-490
        30,-46,-14
        """
        self.inputdata = [line.strip() for line in testdata.strip().split("\n")]
        return 79

    def TestDataB(self):
        # Using results of PartA
        return 3621

    def ParseInput(self):
        scanners = []
        scanner = None

        rx1 = re.compile(f"--- scanner (?P<id>[0-9]*) ---")
        rx2 = re.compile(f"(?P<x>[\-0-9]*),(?P<y>[\-0-9]*),(?P<z>[\-0-9]*)")
        for line in self.inputdata:
            match = rx1.search(line)
            if match:
                scanner = Scanner(int(match["id"]))
                scanners.append(scanner)
            match = rx2.search(line)
            if match:
                scanner.beacons.append([int(match["x"]),int(match["y"]),int(match["z"])])
        return scanners

    def PartA(self):
        self.StartPartA()

        self.scanners = self.ParseInput()

        while True:
            found = False
            for s1 in self.scanners:
                if not s1.posknown:
                    continue
                for s2 in self.scanners:
                    if s2.posknown:
                        continue
                    found = found or s2.FindOverlap(s1)
            if not found:
                break

        print([s.name for s in self.scanners if s.posknown == False])

        base = self.scanners[0]
        bea = set([ (x, y, z) for x, y, z in base.beacons])
        for s in self.scanners[1:]:
            for b in s.beacons:
                pos = (base.pos[0] + b[0] + s.pos[0], base.pos[1] + b[1] + s.pos[1], base.pos[2] + b[2] + s.pos[2])
                bea.add(pos)
        answer = len(bea)

        self.ShowAnswer(answer)

    @staticmethod
    def Manhattan(pos1, pos2):
        return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1]) + abs(pos1[2] - pos2[2])

    def PartB(self):
        self.StartPartB()

        # Using results of PartA (in self.scanners)

        highest = 0
        for a, b in itertools.product(self.scanners, self.scanners):
            highest = max(self.Manhattan(a.pos, b.pos), highest)

        answer = highest

        self.ShowAnswer(answer)


if __name__ == "__main__":
    solution = Day19Solution()
    if len(sys.argv) >= 2 and sys.argv[1] == "test":
        solution.Test()
    else:
        solution.Run()

# Template Version 1.3

