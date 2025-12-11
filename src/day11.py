from aoc import Aoc
import itertools
import math
import re
import sys

# Day 11
# https://adventofcode.com/2025

class Device():
   def __init__(self, name: str) -> None:
      self.name = name
      self.outputs = []

   def __repr__(self):
      oo = ""
      for o in self.outputs:
         oo += o.name + " "
      return f"{self.name}: {oo}"

   def PathsTo(self, out: str) -> int:
      if self.name == "out":
         return 1
      c = 0
      for o in self.outputs:
         c += o.PathsTo(out)
      return c

class Day11Solution(Aoc):

   def Run(self):
      self.StartDay(11, "Reactor")
      self.ReadInput()
      self.PartA()
      self.PartB()

   def Test(self):
      self.StartDay(11)

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
      aaa: you hhh
      you: bbb ccc
      bbb: ddd eee
      ccc: ddd eee fff
      ddd: ggg
      eee: out
      fff: out
      ggg: out
      hhh: ccc fff iii
      iii: out
      """
      self.inputdata = [line.strip() for line in testdata.strip().split("\n")]
      return 5

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

   def CreateDevices(self, data):
      devices = {}
      for ix, line in enumerate(data):
         print(ix)
         parts = line.split(":")
         name = parts[0]
         if name not in devices:
            devices[name] = Device(name)
         for o in parts[1].strip().split(" "):
            if o not in devices:
               devices[o] = Device(o)
            devices[name].outputs.append(devices[o])
            
      return devices

   def PartA(self):
      self.StartPartA()

      data = self.ParseInput()

      devices = self.CreateDevices(data)
      for device in devices.items():
         print(device)
      # Add solution here

      answer = 0
      for k, device in devices.items():
         print(device)
         if device.name == "you":
            answer += device.PathsTo("out")


      self.ShowAnswer(answer)

   def PartB(self):
      self.StartPartB()

      data = self.ParseInput()
      answer = None

      # Add solution here

      self.ShowAnswer(answer)


if __name__ == "__main__":
   solution = Day11Solution()
   if len(sys.argv) >= 2 and sys.argv[1] == "test":
      solution.Test()
   else:
      solution.Run()

# Template Version 1.5

