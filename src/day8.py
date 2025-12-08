from aoc import Aoc
import itertools
import math
import re
import sys

# Day 8
# https://adventofcode.com/2025

class Day8Solution(Aoc):
   def Run(self):
      self.StartDay(8, "Playground")
      self.ReadInput()
      self.count = 1000
      self.PartA()
      self.PartB()

   def Test(self):
      self.StartDay(8)
      self.count = 10

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
      162,817,812
      57,618,57
      906,360,560
      592,479,940
      352,342,300
      466,668,158
      542,29,236
      431,825,988
      739,650,466
      52,470,668
      216,146,977
      819,987,18
      117,168,530
      805,96,715
      346,949,466
      970,615,88
      941,993,340
      862,61,35
      984,92,344
      425,690,689
      """
      self.inputdata = [line.strip() for line in testdata.strip().split("\n")]
      return 40

   def TestDataB(self):
      self.inputdata.clear()
      self.TestDataA()
      return 25272

   def ParseInput(self):
      data = []
      for line in self.inputdata:
         data.append(line)

      return data

   def distsq(self, j1, j2) -> int:
      return (abs(j1[0] - j2[0]) ** 2) + (abs(j1[1] - j2[1]) ** 2) + (abs(j1[2] - j2[2]) ** 2)

   def JoinCircuits(self, circuits):
      # join the overlapping circuits
      # there is probably a better way to do this
      joinedsome = True
      while joinedsome:
         joinedsome = False

         final = []
         for ix, c in enumerate(circuits):
            joined = False
            for jx, f in enumerate(final):
               if len(set(f).intersection(set(c))) > 0:
                  final[jx] = list(set(f + c))
                  joined = True
                  joinedsome = True
                  break
            if not joined:
               final.append(c)
         circuits = final[:]
      return circuits

   def PartA(self):
      self.StartPartA()

      data = self.ParseInput()

      junctions = [(int(l[0]), int(l[1]), int(l[2])) for l in  [ (line.split(",")) for line in data] ]

      distssq = []
      for a, j1 in enumerate(junctions):
         for b, j2 in enumerate(junctions):
            if a >= b:
               continue
            distssq.append((j1, j2, self.distsq(j1, j2)))

      distssq.sort(key=lambda x: x[2])

      circuits = []
      for ix in range(self.count):
         j1 = distssq[ix][0]
         j2 = distssq[ix][1]

         added = False
         for c in circuits:
            if j1 in c:
               if j2 in c:
                  added = True
                  continue
               c.append(j2)
               added = True
               continue
            elif j2 in c:
               if j1 in c:
                  added = True
                  continue
               c.append(j1)
               added = True
               continue
         if not added:
            circuits.append([j1, j2])

      circuits = self.JoinCircuits(circuits)

      circuits.sort(key=lambda x: len(x), reverse=True)

      answer = len(circuits[0]) * len(circuits[1]) * len(circuits[2])

      # Attempt 1: 48672 is too low
      # Attempt 2: 59319 is too low
      # Attempt 3: 75582 is correct

      self.ShowAnswer(answer)

   def PartB(self):
      self.StartPartB()

      data = self.ParseInput()

      junctions = [(int(l[0]), int(l[1]), int(l[2])) for l in  [ (line.split(",")) for line in data] ]

      distssq = []
      for a, j1 in enumerate(junctions):
         for b, j2 in enumerate(junctions):
            if a >= b:
               continue
            distssq.append((j1, j2, self.distsq(j1, j2)))

      distssq.sort(key=lambda x: x[2])

      circuits = []
      for ix in range(len(distssq)):
         j1 = distssq[ix][0]
         j2 = distssq[ix][1]

         added = False
         for c in circuits:
            if j1 in c:
               if j2 in c:
                  added = True
               else:
                  c.append(j2)
                  added = True
            elif j2 in c:
               if j1 in c:
                  added = True
               else:
                  c.append(j1)
                  added = True
         if not added:
            circuits.append([j1, j2])

         circuits = self.JoinCircuits(circuits)
         circuits.sort(key=lambda x: len(x), reverse=True)
         print(len(circuits), len(circuits[0]), " " * 20, end="\r")
         if len(circuits) == 1 and len(circuits[0]) == len(junctions):
            answer = j1[0] * j2[0]
            break

      # Attempt 1: 582414798 is too high
      # Attempt 2: 59039696 is correct

      self.ShowAnswer(answer)


if __name__ == "__main__":
   solution = Day8Solution()
   if len(sys.argv) >= 2 and sys.argv[1] == "test":
      solution.Test()
   else:
      solution.Run()

# Template Version 1.5

