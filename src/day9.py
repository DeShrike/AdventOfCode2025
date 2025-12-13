from aoc import Aoc
from canvas import Canvas
from utilities import dirange, neighbours8
import itertools
import math
import re
import sys

# Day 9
# https://adventofcode.com/2025

class Point():
   def __init__(self, x: int, y: int) -> None:
      self.x = x
      self.ox = x
      self.y = y
      self.oy = y

   def __repr__(self):
      return f"Point({self.x},{self.y})"

class Day9Solution(Aoc):

   def Run(self):
      self.StartDay(9, "Movie Theater")
      self.ReadInput()
      self.spacing = 1
      self.PartA()
      self.PartB()

   def Test(self):
      self.StartDay(9)
      self.spacing = 10

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
      7,1
      11,1
      11,7
      9,7
      9,5
      2,5
      2,3
      7,3
      """
      self.inputdata = [line.strip() for line in testdata.strip().split("\n")]
      return 50

   def TestDataB(self):
      self.inputdata.clear()
      self.TestDataA()
      return 24

   def ParseInput(self):
      data = []
      for line in self.inputdata:
         data.append(line)
      return data

   def CalcArea(self, p1, p2) -> int:
      return (abs(p1[0] - p2[0]) + 1) * (abs(p1[1] - p2[1]) + 1)

   def CalcExpandedArea(self, p1: Point, p2: Point) -> int:
      return (abs(p1.ox - p2.ox) + 1) * (abs(p1.oy - p2.oy) + 1)

   def PartA(self):
      self.StartPartA()

      data = self.ParseInput()
      points = [ (int(l[0]), int(l[1])) for l in [ (line.split(",")) for line in data ] ]

      answer = 0
      for a, p1 in enumerate(points):
         for b, p2 in enumerate(points):
            if a >= b:
               continue
            area = self.CalcArea(p1, p2)
            if area > answer:
               answer = area

      self.ShowAnswer(answer)

   def IsInRect(self, p1, p2, p) -> bool:
      pp1 = (min(p1[0], p2[0]), min(p1[1], p2[1]))
      pp2 = (max(p1[0], p2[0]), max(p1[1], p2[1]))
      return pp1[0] < p[0] < pp2[0] and pp1[1] < p[1] < pp2[1]

   def IsBetweenIncl(self, a, b, x) -> bool:
      if a > b:
         b, a = a, b
      return a <= x <= b;

   def IsBetweenExcl(self, a, b, x) -> bool:
      if a > b:
         b, a = a, b
      return a < x < b;

   def GridToPng(self, grid) -> None:
      width = len(grid[0])
      height = len(grid)
      boxsize = 5

      canvas = Canvas(width * boxsize, height * boxsize)
      for y, row in enumerate(grid):
         for x, col in enumerate(row):
            if col == 1:
               canvas.set_big_pixel(x * boxsize, y * boxsize, (255,0,0), boxsize)
            elif col == 2:
               canvas.set_big_pixel(x * boxsize, y * boxsize, (0,255,0), boxsize)
            elif col == 3:
               canvas.set_big_pixel(x * boxsize, y * boxsize, (0,0,255), boxsize)
            elif col == 4:
               canvas.set_big_pixel(x * boxsize, y * boxsize, (255,255,0), boxsize)

      pngname = "day9b.png"
      print(f"Saving {pngname}")
      canvas.save_PNG(pngname)

   def Floodfill(self, grid) -> None:
      width = len(grid[0])
      height = len(grid)
      x = width // 2
      y = height // 3
      grid[y][x] = 3
      #print("floodfilling")
      q = [(x, y)]
      while len(q) > 0:
         p = q.pop()
         grid[p[1]][p[0]] = 3
         for n in neighbours8(p[0], p[1], (width, height)):
            if grid[n[1]][n[0]] == 0:
               grid[n[1]][n[0]] = 3
               q.append((n[0], n[1]))
      #print("done")

   def IsAreaInside(self, p1: Point, p2: Point, grid) -> bool:
      # print(f"Trying {p1} -> {p2}")
      y1 = p1.y
      y2 = p2.y
      if y1 > y2:
         y1, y2 = y2, y1

      x1 = p1.x
      x2 = p2.x
      if x1 > x2:
         x1, x2 = x2, x1

      for y in dirange(y1, y2):
         for x in dirange(x1, x2):
            if grid[y][x] == 0:
               return False
      return True

   def FillAreaInside(self, p1: Point, p2: Point, grid) -> None:
      # print(f"Trying {p1} -> {p2}")
      y1 = p1.y
      y2 = p2.y
      if y1 > y2:
         y1, y2 = y2, y1

      x1 = p1.x
      x2 = p2.x
      if x1 > x2:
         x1, x2 = x2, x1

      for y in dirange(y1, y2):
         for x in dirange(x1, x2):
            grid[y][x] = 4

   def PartB(self):
      self.StartPartB()

      data = self.ParseInput()
      answer = 0

      points = [ Point(int(l[0]), int(l[1])) for l in [ (line.split(",")) for line in data ] ]

      minx = miny = 1_000_000_000
      maxx = maxy = 0
      for point in points:
         minx = min(minx, point.x)
         miny = min(miny, point.y)
         maxx = max(maxx, point.x)
         maxy = max(maxy, point.y)

      #print(f"Extent X: {minx} -> {maxx}")
      #print(f"Extent Y: {miny} -> {maxy}")

      xs = list(set([p.x for p in points]))
      xs.sort()
      ys = list(set([p.y for p in points]))
      ys.sort()

      ny = 1
      for y in ys:
         ny += self.spacing
         for p in points:
            if p.oy == y:
               p.y = ny
      nx = 1
      for x in xs:
         nx += self.spacing
         for p in points:
            if p.ox == x:
               p.x = nx

      minx = miny = 1_000_000_000
      maxx = maxy = 0
      for point in points:
         minx = min(minx, point.x)
         miny = min(miny, point.y)
         maxx = max(maxx, point.x)
         maxy = max(maxy, point.y)

      #print(f"Extent X: {minx} -> {maxx}")
      #print(f"Extent Y: {miny} -> {maxy}")

      grid = [[0 for x in range(maxx + 5)] for y in range(maxy + 5)]

      for ix, p1 in enumerate(points):
         nx = (ix + 1) % len(points)
         p2 = points[nx]
         if p1.x == p2.x:
            # vert
            y1 = p1.y
            y2 = p2.y
            if y1 > y2:
               y1, y2 = y2, y1
            for y in range(y1, y2):
               grid[y][p1.x] = 2
         else:
            # hor
            x1 = p1.x
            x2 = p2.x
            if x1 > x2:
               x1, x2 = x2, x1
            for x in range(x1, x2):
               grid[p1.y][x] = 2

      for p in points:
         grid[p.y][p.x] = 1

      self.Floodfill(grid)

      answer = 0
      bestp1 = None
      bestp2 = None
      for a, p1 in enumerate(points):
         for b, p2 in enumerate(points):
            if a >= b:
               continue
            if self.IsAreaInside(p1, p2, grid):
               area = self.CalcExpandedArea(p1, p2)
               if area > answer:
                  answer = area
                  bestp1 = p1
                  bestp2 = p2

      self.FillAreaInside(bestp1, bestp2, grid)

      self.GridToPng(grid)

      # Attempt 1: 4750092396 is too high
      # Attempt 2: 2679903198 is too high
      # Attempt 3: 1363080015 is too low
      # Attempt 4: 1468516555 is correct

      self.ShowAnswer(answer)


if __name__ == "__main__":
   solution = Day9Solution()
   if len(sys.argv) >= 2 and sys.argv[1] == "test":
      solution.Test()
   else:
      solution.Run()

# Template Version 1.5

