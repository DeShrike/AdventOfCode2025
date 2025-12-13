from aoc import Aoc
import itertools
import math
import re
import sys

# Day 10
# https://adventofcode.com/2025

class Machine():
   def __init__(self, line: str) -> None:
      rx = re.compile("^\[(?P<lights>[\.\#]*)\] (?P<buttons>[0-9\,\(\) ]*) \{(?P<jolt>[\,0-9]*)\}")

      match = rx.search(line)
      l = match["lights"]
      b = match["buttons"]
      j = match["jolt"]

      self.indis = l
      self.indi = int(l[::-1].replace(".", "0").replace("#", "1"), 2)
      self.lights = 0
      self.joltage = [int(x) for x in j.split(",")]
      self.buttons = []
      self.fullbuttons = []
      
      for bb in b.split(" "):
         self.fullbuttons.append([int(n) for n in bb[1:-1].split(",")])
         d = bb[1:-1].split(",")
         l = 0
         for ll in d:
            l |= (1 << int(ll))
         self.buttons.append(l)

   """
   def ToggleBitXX(self, num: int, bit: int) -> int:
      return num ^ (1 << (bit - 1))
   """

   def ToggleBit(self, num: int, bits: int) -> int:
      return num ^ bits

   def GetBits(self, val):
      for i in range(16):
         if val & (1 << i) != 0:
            yield i

   def SolveLights(self) -> int:
      m = (1 << len(self.buttons)) - 1
      mi = 1000;
      for n in range(m):
         val = 0
         c = 0
         for nn in self.GetBits(n):
            val = self.ToggleBit(val, self.buttons[nn])
            c += 1
         if val == self.indi:
            mi = min(mi, c)
      return mi

   def SolveB(self):
      buttoncount = len(self.fullbuttons)
      joltagecount = len(self.joltage)
      mat = [[0 for _ in range(buttoncount+1)] for _ in range(joltagecount)]
      for ix, j in enumerate(self.joltage):
         mat[ix][-1] = j
      for bix, b in enumerate(self.fullbuttons):
         for n in b:
            mat[n][bix] += 1
      print(" ")
      print(" ")
      for m in mat:
         print(m, len([True for t in m if t == 1]))

   """
(3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}

0 * A + 0 * B + 0 * C + 0 * D + 1 * E + 1 * F = 3
0 * A + 1 * B + 0 * C + 0 * D + 0 * E + 1 * F = 5
0 * A + 0 * B + 1 * C + 1 * D + 1 * E + 0 * F = 4
1 * A + 1 * B + 0 * C + 1 * D + 0 * E + 0 * F = 7

A = 1
B = 3
D = 3
C = 0
E = 1
F = 2

1 * 1 + 1 * 2 = 3
1 * 3 + 1 * 2 = 5
1 * 3 + 1 * 1 = 4
1 * 1 + 1 * 3 + 1 * 3 = 7


   """



   """
   def SolveB(self):
      coeffs = []
      target = 0
      for button in self.buttons:
         co = 0
         for bit in self.GetBits(button):
            co += 100 ** bit
         coeffs.append(co)
      print(coeffs)
      
      for i, j in enumerate(reversed(self.joltage)):
         target += j * (100 ** i)
      print(target)

      a = input()

      solutions = self.solve_linear_combination(coeffs, target)

      for sol in solutions:
          print(sol)

      smallest = min([sum(x) for x in solutions])
      print(smallest)
      print("\nTotal solutions:", len(solutions))

      a = input()
   """

class Day10Solution(Aoc):

   def Run(self):
      self.StartDay(10, "Factory")
      self.ReadInput()
      self.PartA()
      self.PartB()

   def Test(self):
      self.StartDay(10)

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
      [.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
      [...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
      [.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}
      """
      self.inputdata = [line.strip() for line in testdata.strip().split("\n")]
      return 7

   def TestDataB(self):
      self.inputdata.clear()
      self.TestDataA()
      return 33

   def ParseInput(self):
      data = []
      for line in self.inputdata:
         data.append(line)

      return data

   def PartA(self):
      self.StartPartA()

      data = self.ParseInput()
      answer = None

      machines = [Machine(line) for line in data]
      answer = sum([m.SolveLights() for m in machines])

      self.ShowAnswer(answer)

   def PartB(self):
      self.StartPartB()

      data = self.ParseInput()
      answer = None

      machines = [Machine(line) for line in data]
      for m in machines:
         m.SolveB()
         aa= input()
      self.ShowAnswer(answer)


if __name__ == "__main__":
   solution = Day10Solution()
   if len(sys.argv) >= 2 and sys.argv[1] == "test":
      solution.Test()
   else:
      solution.Run()

# Template Version 1.5

