from aoc import Aoc
import itertools
import math
import re
import sys

# Day 5
# https://adventofcode.com/2025

class Range():
   def __init__(self, v: int, t: int) -> None:
      self.v = v
      self.t = t

class Day5Solution(Aoc):
   def Run(self):

      self.StartDay(5, "Cafeteria")
      self.ReadInput()
      self.PartA()
      self.PartB()

   def Test(self):
      self.StartDay(5)

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
      3-5
      10-14
      16-20
      12-18

      1
      5
      8
      11
      17
      32
      """
      self.inputdata = [line.strip() for line in testdata.strip().split("\n")]
      return 3

   def TestDataB(self):
      self.inputdata.clear()
      self.TestDataA()
      return 14

   def ParseInput(self):
      data = []
      for line in self.inputdata:
         data.append(line)

      return data

   def PartA(self):
      self.StartPartA()

      data = self.ParseInput()
      answer = 0

      ranges = []
      ids = []
      for l, lijn in enumerate(data):
         if "-" in lijn:
            parts = lijn.split("-")
            ranges.append(( int(parts[0]), int(parts[1]) ))
         elif lijn == "":
            continue
         else:
            ids.append(int(lijn))

      for ID in ids:
         for r in ranges:
            if r[0] <= ID <= r[1]:
               answer += 1
               break

      self.ShowAnswer(answer)

   def PartB(self):
      self.StartPartB()

      data = self.ParseInput()
      answer = 0

      ranges = []
      for l, lijn in enumerate(data):
         if "-" in lijn:
            parts = lijn.split("-")
            ranges.append(( int(parts[0]), int(parts[1]) ))

      rr = ranges.sort(key= lambda x: x[0])
      ranges = [Range(r[0], r[1]) for r in ranges]

      count = len(ranges)
      for _ in range(100):
         remaining = []
         c = ranges[0]
         for r in ranges[1:]:
            if c.v <= r.v <= c.t:
               if r.t > c.t:
                  c.t = r.t
            else:
               remaining.append(r)
         remaining.append(c)
         ranges = remaining[:]
         count = len(ranges)

      for r in remaining:
         answer += (r.t - r.v) + 1

      self.ShowAnswer(answer)


if __name__ == "__main__":
   solution = Day5Solution()
   if len(sys.argv) >= 2 and sys.argv[1] == "test":
      solution.Test()
   else:
      solution.Run()

# Template Version 1.5

