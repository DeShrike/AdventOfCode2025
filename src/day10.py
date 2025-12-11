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
      for b in b.split(" "):
         d = b[1:-1].split(",")
         l = 0
         for ll in d:
            l |= (1 << int(ll))
         self.buttons.append(l)

   def ToggleBitXX(self, num: int, bit: int) -> int:
      #print(f"toggle {bit} in {num}")
      return num ^ (1 << (bit - 1))

   def ToggleBit(self, num: int, bits: int) -> int:
      #print(f"toggle {bits} in {num}")
      return num ^ bits

   def GetBits(self, val):
      for i in range(16):
         if val & (1 << i) != 0:
            yield i

   def SolveLights(self) -> int:
      #for b in self.GetBits(3):
      #   print (b)
      #aa = input()
   
      m = (1 << len(self.buttons)) - 1
      mi = 1000;
      #print("range: ", 0, m)
      for n in range(m):
         val = 0
         c = 0
         #print(f"num {n}: ", end="")
         for nn in self.GetBits(n):
            #print(f" buttons[{nn}] = {self.buttons[nn]}", end="")
            val = self.ToggleBit(val, self.buttons[nn])
            c += 1
         #print(f"X {val} == {self.indi} ??")
         #print(n, val, bin(val), self.indis, bin(self.indi))
         #aa =  input()
         if val == self.indi:
            #print("OK", nn, m, len(self.buttons), len(self.indis))
            mi = min(mi, c)
      #print(mi)
      #aa = input()
      return mi

   def solve_linear_combination(self, coeffs, target):
       """
       Solve c1*x1 + c2*x2 + ... + cn*xn = target
       for non-negative integers x1, x2, ..., xn.

       coeffs: list of integers (coefficients)
       target: integer target sum
       """
       print("solving")
       solutions = []
       n = len(coeffs)
       xs = [0] * n  # placeholder for current solution

       def backtrack(i, remaining):
           print(i, remaining)
           # If we've assigned all variables:
           if i == n:
               if remaining == 0:
                   solutions.append(tuple(xs))
               return
           
           c = coeffs[i]

           # Maximum possible value for xi given the remaining amount
           max_x = remaining // c  

           for v in range(max_x + 1):
               xs[i] = v
               backtrack(i + 1, remaining - v * c)

       backtrack(0, target)
       return solutions

   def Dummy(self):
      coeffs = [1000, 1010, 100, 1100, 101, 11]
      target = 3547

      """
      0,0,0,0
      0,0,0,1  (3)
      0,3,0,4  (1,3)*3
      0,3,3,7  (2,3)*3
      1,3,4,7  (0,2)
      3,5,4,7  (0,1)

      A * 1000 + B * 1010 + C * 100 + D * 1100 + E * 101 + F * 11 = 3547
      """

      solutions = solve_linear_combination(coeffs, target)

      for sol in solutions:
          print(sol)

      print("\nTotal solutions:", len(solutions))

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
      machines[0].SolveB()
      # Add solution here

      self.ShowAnswer(answer)


if __name__ == "__main__":
   solution = Day10Solution()
   if len(sys.argv) >= 2 and sys.argv[1] == "test":
      solution.Test()
   else:
      solution.Run()

# Template Version 1.5

