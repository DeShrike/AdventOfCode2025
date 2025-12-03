from aoc import Aoc
import itertools
import math
import re
import sys

# Day 3
# https://adventofcode.com/2025

class Day3Solution(Aoc):

   def Run(self):
      self.StartDay(3, "Lobby")
      self.ReadInput()
      self.PartA()
      self.PartB()

   def Test(self):
      self.StartDay(3)

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
      987654321111111
      811111111111119
      234234234234278
      818181911112111
      """
      self.inputdata = [line.strip() for line in testdata.strip().split("\n")]
      return 357

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

   def PartA(self):
      self.StartPartA()

      data = self.ParseInput()
      answer = 0

      perms = list(itertools.permutations(range(len(data[0])), 2))
      for bank in data:
         answer += max([ int(bank[b[0]] + bank[b[1]]) for b in perms if b[0] < b[1] ])

      # Attempt 1: 16471 is too low.
      # Attempt 2: 16956 is too low.
      # Attempt 3: 17427 is correct.

      self.ShowAnswer(answer)

   def PartB(self):
      self.StartPartB()

      data = self.ParseInput()
      answer = None

      # Add solution here

      self.ShowAnswer(answer)


if __name__ == "__main__":
   solution = Day3Solution()
   if len(sys.argv) >= 2 and sys.argv[1] == "test":
      solution.Test()
   else:
      solution.Run()

# Template Version 1.5

