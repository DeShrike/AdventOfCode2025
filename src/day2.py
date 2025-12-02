from aoc import Aoc
from utilities import dirange
import itertools
import math
import re
import sys

# Day 2
# https://adventofcode.com/2025

class Day2Solution(Aoc):

   def Run(self):
      self.StartDay(2, "Gift Shop")
      self.ReadInput()
      self.PartA()
      self.PartB()

   def Test(self):
      self.StartDay(2)

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
      11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124
      """
      self.inputdata = [line.strip() for line in testdata.strip().split("\n")]
      return 1227775554

   def TestDataB(self):
      self.inputdata.clear()
      self.TestDataA()
      return 4174379265

   def ParseInput(self):
      data = []
      for line in self.inputdata:
         data.append(line)

      return data

   def IsInvalidA(self, id: int) -> bool:
      s = str(id)
      if len(s) % 2 == 1:
         return False
      if s[0:len(s) // 2] * 2 == s:
         return True
      return False

   def IsInvalidB(self, id: int) -> bool:
      s = str(id)
      if len(s) == 1:
         return False
      for l in dirange(1, len(s) // 2):
         if len(s) % l != 0:
            continue
         c = len(s) // l
         if s[0:l] * c == s:
            return True

      return False

   def PartA(self):
      self.StartPartA()

      data = self.ParseInput()

      answer = 0
      ranges = data[0].split(",")
      for range in ranges:
         van, tot = range.split("-")
         van = int(van)
         tot = int(tot)
         for id in dirange(van, tot):
            if self.IsInvalidA(id):
               answer += id

      self.ShowAnswer(answer)

   def PartB(self):
      self.StartPartB()

      data = self.ParseInput()
      answer = 0
      ranges = data[0].split(",")
      for range in ranges:
         van, tot = range.split("-")
         van = int(van)
         tot = int(tot)
         for id in dirange(van, tot):
            if self.IsInvalidB(id):
               answer += id

      # Attempt 1: 36037497081 is too high
      # Attempt 2: 36037497037 is correct

      self.ShowAnswer(answer)


if __name__ == "__main__":
   solution = Day2Solution()
   if len(sys.argv) >= 2 and sys.argv[1] == "test":
      solution.Test()
   else:
      solution.Run()

# Template Version 1.5

