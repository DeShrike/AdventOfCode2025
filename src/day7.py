from aoc import Aoc
import itertools
import math
import re
import sys

# Day 7
# https://adventofcode.com/2025

class Day7Solution(Aoc):

   def Run(self):
      self.StartDay(7, "Laboratories")
      self.ReadInput()
      self.PartA()
      self.PartB()

   def Test(self):
      self.StartDay(7)

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
      .......S.......
      ...............
      .......^.......
      ...............
      ......^.^......
      ...............
      .....^.^.^.....
      ...............
      ....^.^...^....
      ...............
      ...^.^...^.^...
      ...............
      ..^...^.....^..
      ...............
      .^.^.^.^.^...^.
      ...............
      """
      self.inputdata = [line.strip() for line in testdata.strip().split("\n")]
      return 21

   def TestDataB(self):
      self.inputdata.clear()
      self.TestDataA()
      return 40

   def ParseInput(self):
      data = []
      for line in self.inputdata:
         data.append(line)

      return data

   def PartA(self):
      self.StartPartA()

      data = self.ParseInput()

      beams = []
      splits = 0
      height = len(data)
      width = len(data[0])
      for ix, line in enumerate(data):
         if "S" in line:
            beams.append((line.index("S"), ix + 1))

      uni = 1

      while True:
         newbeams = []
         for beam in beams:
            x, y = beam
            if y + 1 >= height:
               pass
            elif data[y + 1][x] == ".":
               newbeams.append((x, y + 1))
            elif data[y + 1][x] == "^":
               split = False
               uni += 2
               if x >= 0 and (x - 1, y + 1) not in newbeams:
                  newbeams.append((x - 1, y + 1))
                  split = True
               if x < width - 1 and (x + 1, y + 1) not in newbeams:
                  newbeams.append((x + 1, y + 1))
                  split = True
               splits += 1 if split else 0
         beams = newbeams[:]
         if len(beams) == 0:
            break

      print(uni)
      answer = splits
      self.ShowAnswer(answer)

   def PartB(self):
      self.StartPartB()

      data = self.ParseInput()

      height = len(data)
      width = len(data[0])
      beam = None
      for ix, line in enumerate(data):
         if "S" in line:
            beam = (line.index("S"), ix + 1)

      def dropbeam(b, timelines: int) -> int:
         #print("dropbeam", b, timelines)
         x, y = b
         while y < height and data[y][x] == ".":
            y += 1
         if y >= height:
            #print("done")
            return timelines + 1
         #print(x, y, data[y][x])
         if data[y][x] == "^":
            #print("Split")
            timelines = dropbeam((x - 1, y), timelines)
            timelines = dropbeam((x + 1, y), timelines)
         if timelines % 100_000 == 0:
            print("return", timelines)
         return timelines

      answer = dropbeam(beam, 0)

      self.ShowAnswer(answer)


if __name__ == "__main__":
   solution = Day7Solution()
   if len(sys.argv) >= 2 and sys.argv[1] == "test":
      solution.Test()
   else:
      solution.Run()

# Template Version 1.5

