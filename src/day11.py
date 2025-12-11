from aoc import Aoc
from functools import cache
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

   def CountPathsTo(self, out: str) -> int:
      if self.name == out:
         return 1
      c = 0
      for o in self.outputs:
         c += o.CountPathsTo(out)
      return c

   def GetPathsToXXX(self, out: str, level: int, seenfft: bool, seendac: bool):
      if self.name == out and seendac and seenfft:
         print("ok")
         return [[self.name]]
      if self.name == out:
         return None
      allpaths = []
      if self.name == "dac":
         seendac = True
      if self.name == "fft":
         seenfft = True
      for o in self.outputs:
         paths = o.GetPathsTo(out, level + 1, seenfft, seendac)
         if paths is not None:
            for p in paths:
               p.append(self.name)
               allpaths.append(p)
      return allpaths

   @cache
   def GetPathsTo(self, out: str, seenfft: bool, seendac: bool) -> int:
      if self.name == out and seendac and seenfft:
         return 1
      if self.name == "dac":
         seendac = True
      if self.name == "fft":
         seenfft = True
      c = 0
      for o in self.outputs:
         c += o.GetPathsTo(out, seenfft, seendac)
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
      testdata = \
      """
      svr: aaa bbb
      aaa: fft
      fft: ccc
      bbb: tty
      tty: ccc
      ccc: ddd eee
      ddd: hub
      hub: fff
      eee: dac
      dac: fff
      fff: ggg hhh
      ggg: out
      hhh: out
      """
      self.inputdata = [line.strip() for line in testdata.strip().split("\n")]
      return 2

   def ParseInput(self):
      data = []
      for line in self.inputdata:
         data.append(line)

      return data

   def CreateDevices(self, data):
      devices = {}
      for ix, line in enumerate(data):
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

      answer = 0
      for k, device in devices.items():
         if device.name == "you":
            answer += device.CountPathsTo("out")

      self.ShowAnswer(answer)

   def PartB(self):
      self.StartPartB()

      data = self.ParseInput()
      devices = self.CreateDevices(data)

      answer = 0

      for k, device in devices.items():
         if device.name == "svr":
            answer += device.GetPathsTo("out", False, False)

      self.ShowAnswer(answer)


if __name__ == "__main__":
   solution = Day11Solution()
   if len(sys.argv) >= 2 and sys.argv[1] == "test":
      solution.Test()
   else:
      solution.Run()

# Template Version 1.5

