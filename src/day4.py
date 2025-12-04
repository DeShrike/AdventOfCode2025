from aoc import Aoc
from utilities import dirange
from canvas import Canvas
import itertools
import math
import re
import sys

# Day 4
# https://adventofcode.com/2025

class Day4Solution(Aoc):

   def Run(self):
      self.StartDay(4, "Printing Department")
      self.ReadInput()
      self.PartA()
      self.PartB()

   def Test(self):
      self.StartDay(4)

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
      ..@@.@@@@.
      @@@.@.@.@@
      @@@@@.@.@@
      @.@@@@..@.
      @@.@@@@.@@
      .@@@@@@@.@
      .@.@.@.@@@
      @.@@@.@@@@
      .@@@@@@@@.
      @.@.@@@.@.
      """
      self.inputdata = [line.strip() for line in testdata.strip().split("\n")]
      return 13

   def TestDataB(self):
      self.inputdata.clear()
      self.TestDataA()
      return 43

   def ParseInput(self):
      data = []
      for line in self.inputdata:
         data.append(line)

      return data

   def Neighbours(self, data, x: int, y: int):
      width = len(data[0])
      height = len(data)
      for dx in dirange(-1, 1):
         for dy in dirange(-1, 1):
            if 0 <= x + dx < width and 0 <= y + dy < height and not (dx == 0 and dy  == 0):
               yield (x + dx, y + dy)

   def GetRemovalble(self, grid):
      removable = []
      for y, row in enumerate(grid):
         for x, roll in enumerate(grid):
            if grid[y][x] != '@':
               continue
            nn = [True for xx, yy in self.Neighbours(grid, x, y) if grid[yy][xx] == '@']
            if len(nn) < 4:
               removable.append((x, y))
      return removable

   def PartA(self):
      self.StartPartA()

      data = self.ParseInput()

      rem = self.GetRemovalble(data)
      answer = len(rem)

      self.ShowAnswer(answer)

   def PartB(self):
      self.StartPartB()

      data = self.ParseInput()
      answer = 0

      grid = [[r for r in row] for row in data]
      while True:
         rem = self.GetRemovalble(grid)
         answer += len(rem)
         for p in rem:
            grid[p[1]][p[0]] = "."
         if len(rem) == 0:
            break

      boxsize = 4
      coloron = (0xFF, 0x00, 0x00)
      coloroff = (0x18, 0x18, 0x18)

      width = len(data[0])
      height = len(data)
      canvas = Canvas(width * boxsize, height * boxsize)
      for y, row in enumerate(grid):
         for x, roll in enumerate(grid):
            xx = x * boxsize
            yy = y * boxsize
            if grid[y][x] != '@':
               canvas.set_big_pixel(xx, yy, coloroff, boxsize)
            else:
               canvas.set_big_pixel(xx + 1, yy + 1, coloron, boxsize - 2)

      pngname = "day4b.png"
      print(f"Saving {pngname}")
      canvas.save_PNG(pngname)

      self.ShowAnswer(answer)


if __name__ == "__main__":
   solution = Day4Solution()
   if len(sys.argv) >= 2 and sys.argv[1] == "test":
      solution.Test()
   else:
      solution.Run()

# Template Version 1.5

