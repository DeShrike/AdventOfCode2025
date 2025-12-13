from aoc import Aoc
import itertools
import math
import re
import sys

# Day 12
# https://adventofcode.com/2025

class Region():
   def __init__(self, line: str) -> None:
      p = line.split(":")
      w, h = p[0].split("x")
      self.width = int(w)
      self.height = int(h)
      pp = p[1].strip().split(" ")
      self.needed = []
      for ix, ppp in enumerate(pp):
         self.needed.append(int(ppp))

   def __repr__(self) -> str:
      return f"{self.width}x{self.height} : {self.needed}"

class Shape():
   def __init__(self, lines) -> None:
      self.id = int(lines[0].split(":")[0])
      self.w = len(lines[1])
      self.h = len(lines) - 1
      self.activecount = 0
      self.grid = [ [0 for _ in range(self.w)] for _ in range(self.h) ]
      for y, l in enumerate(lines[1:]):
         for x, c in enumerate(l):
            if c == "#":
               self.activecount += 1
               self.grid[y][x] = 1

   def __repr__(self) -> str:
      return f"{self.id}: {self.w}x{self.h}"


class Day12Solution(Aoc):

   def Run(self):
      self.StartDay(12, "Christmas Tree Farm")
      self.ReadInput()
      self.PartA()
      self.PartB()

   def Test(self):
      self.StartDay(12)

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
      0:
      ###
      ##.
      ##.

      1:
      ###
      ##.
      .##

      2:
      .##
      ###
      ##.

      3:
      ##.
      ###
      ##.

      4:
      ###
      #..
      ###

      5:
      ###
      .#.
      ###

      4x4: 0 0 0 0 2 0
      12x5: 1 0 1 0 2 2
      12x5: 1 0 1 0 3 2
      """
      self.inputdata = [line.strip() for line in testdata.strip().split("\n")]
      return 2

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

   def ParseInput(self):
      # rx = re.compile("^(?P<from>[A-Z0-9]{3}) = \((?P<left>[A-Z0-9]{3}), (?P<right>[A-Z0-9]{3})\)$")
      # match = rx.search(line)
      # pos = match["from"]

      data = []
      for line in self.inputdata:
         data.append(line)

      return data

   def ParseData(self, data):
      shapes = []
      regions = []
      l = []
      for line in data:
         if line == "":
            shapes.append(Shape(l))
            l = []
         else:
            l.append(line)
      for line in l:
         regions.append(Region(line))
      return shapes, regions

   def TryRegion(self, region: Region, shapes) -> bool:
      available = region.width * region.height
      needed = 0
      for ix, n in enumerate(region.needed):
         needed += shapes[ix].activecount * n
      return needed <= available

   def PartA(self):
      self.StartPartA()

      data = self.ParseInput()
      shapes, regions = self.ParseData(data)
      answer = 0

      for region in regions:
         if self.TryRegion(region, shapes):
            answer += 1

      self.ShowAnswer(answer)

   def PartB(self):
      self.StartPartB()

      data = self.ParseInput()
      answer = None

      # Add solution here

      self.ShowAnswer(answer)


if __name__ == "__main__":
   solution = Day12Solution()
   if len(sys.argv) >= 2 and sys.argv[1] == "test":
      solution.Test()
   else:
      solution.Run()

# Template Version 1.5

