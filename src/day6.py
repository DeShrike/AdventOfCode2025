from aoc import Aoc
import itertools
import math
import re
import sys

# Day 6
# https://adventofcode.com/2025

class Day6Solution(Aoc):

   def Run(self):
      self.StartDay(6, "Trash Compactor")
      self.ReadInput()
      self.PartA()
      self.PartB()

   def Test(self):
      self.StartDay(6)

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
123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  
      """
      self.inputdata = [line.rstrip() for line in testdata.strip().split("\n")]
      return 4277556

   def TestDataB(self):
      self.inputdata.clear()
      self.TestDataA()
      return 3263827

   def ParseInput(self):
      data = []
      for line in self.inputdata:
         data.append(line)

      return data

   def PartA(self):
      self.StartPartA()

      data = self.ParseInput()
      answer = 0
      operations = None
      numbers = []
      for ix, line in enumerate(data):
         if ix == len(data) - 1:
            operations = line.replace("  ", " ").split()
         else:
            l = [int(p) for p in line.replace("  ", " ").split()]
            numbers.append(l)

      for c in range(len(operations)):
         if operations[c] == "*":
            answer += math.prod([n[c] for n in numbers])
         else:
            answer += sum([n[c] for n in numbers])

      self.ShowAnswer(answer)

   def PartB(self):
      self.StartPartB()

      data = self.ParseInput()
      answer = 0

      lines = [d + " " for d in data]

      groups = []
      oper = None
      nums = []
      for p in range(len(lines[0])):
         num = ""
         for d in lines[:-1]:
            num += d[p]
         if p < len(lines[-1]) and (lines[-1][p] == "*" or lines[-1][p] == "+"):
            oper = lines[-1][p]
         if num.strip() == "":
            groups.append((nums, oper))
            nums = []
            oper = None
         else:
            nums.append(int(num.strip()))
      groups.append((nums, oper))

      for group in groups:
         if group[1] == "+":
            answer += sum(group[0])
         elif group[1] == "*":
            answer += math.prod(group[0])

      # Attempt 1: 9640641878594 is too high
      # Attempt 2: 9640641878593 is correct

      self.ShowAnswer(answer)


if __name__ == "__main__":
   solution = Day6Solution()
   if len(sys.argv) >= 2 and sys.argv[1] == "test":
      solution.Test()
   else:
      solution.Run()

# Template Version 1.5

