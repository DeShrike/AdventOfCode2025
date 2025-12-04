from aoc import Aoc
from utilities import dirange
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

   def PartA(self):
      self.StartPartA()

      data = self.ParseInput()
      answer = 0

      for y, row in enumerate(data):
         for x, roll in enumerate(row):
            if data[y][x] != '@':
               continue
            #print(x, y, end="")
            nn = [True for xx, yy in self.Neighbours(data, x, y) if data[yy][xx] == '@']
            #print(f"  => {len(nn)}")
            #a = input()
            if len(nn) < 4:
               answer += 1

      self.ShowAnswer(answer)

   def PartB(self):
      self.StartPartB()

      data = self.ParseInput()
      answer = None

      # Add solution here

      self.ShowAnswer(answer)


if __name__ == "__main__":
   solution = Day4Solution()
   if len(sys.argv) >= 2 and sys.argv[1] == "test":
      solution.Test()
   else:
      solution.Run()

# Template Version 1.5

