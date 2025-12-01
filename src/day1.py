from aoc import Aoc
import itertools
import math
import re
import sys

# Day 1
# https://adventofcode.com/2025

class Day1Solution(Aoc):

   def Run(self):
      self.StartDay(1, "Secret Entrance")
      self.ReadInput()
      self.PartA()
      self.PartB()

   def Test(self):
      self.StartDay(1)

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
      L68
      L30
      R48
      L5
      R60
      L55
      L1
      L99
      R14
      L82
      """
      self.inputdata = [line.strip() for line in testdata.strip().split("\n")]
      return 3

   def TestDataB(self):
      self.inputdata.clear()
      self.TestDataA()
      return 6

   def ParseInput(self):
      data = []
      for line in self.inputdata:
         data.append(line)

      return data

   def PartA(self):
      self.StartPartA()

      data = self.ParseInput()
      pos = 50
      answer = 0
      for line in data:
         count = int(line[1:])
         if line[0] == "R":
            pos += count
         else:
            pos -= count
         pos = pos % 100
         if pos == 0:
            answer += 1

      self.ShowAnswer(answer)

   def PartB(self):
      self.StartPartB()

      data = self.ParseInput()
      pos = 50
      answer = 0

      for line in data:
         count = int(line[1:])
         for _ in range(count):
            pos = pos + (1 if line[0] == "R" else -1)
            pos = (pos + 100) % 100
            if pos == 0:
               answer += 1

      # Attempt 1: 2454 is too low
      # Attempt 2: 6351 is too low
      # Attempt 3: 6558 is correct

      self.ShowAnswer(answer)


if __name__ == "__main__":
   solution = Day1Solution()
   if len(sys.argv) >= 2 and sys.argv[1] == "test":
      solution.Test()
   else:
      solution.Run()

# Template Version 1.5

