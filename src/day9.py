from aoc import Aoc
import itertools
import math
import re
import sys

# Day 9
# https://adventofcode.com/2025

class Day9Solution(Aoc):

   def Run(self):
      self.StartDay(9, "Movie Theater")
      self.ReadInput()
      self.PartA()
      self.PartB()

   def Test(self):
      self.StartDay(9)

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

   def CalcArea(self, p1, p2):
      return (abs(p1[0] - p2[0]) + 1) * (abs(p1[1] - p2[1]) + 1)

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

   """
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

   def IsOnBorder(self, points, p) -> bool:
      for ix, p1 in enumerate(points):
         np = points[(ix + 1) % len(points)]

         if p1[0] == np[0]:
            # vertical line
            if p[0] == p1[0]:
               if self.IsBetweenIncl(p1[1], np[1], p[1]):
                  return True
         elif p1[1] == np[1]:
            # horizontal line
            if p[1] == p1[1]:
               if self.IsBetweenIncl(p1[0], np[0], p[0]):
                  return True
         else:
            print("Oops")
            aa = input
      return False

   def IsInPolygon(self, points, p) -> bool:
      i = 90
      j = len(points) - 1
      oddNodes=False
      polyY = [pp[1] for pp in points]
      polyX = [pp[0] for pp in points]
      x, y = p
      for i in range(len(points)):
         if (polyY[i] < y and polyY[j] >= y or polyY[j] < y and polyY[i] >= y):
            if (polyX[i] + (y - polyY[i]) / (polyY[j] - polyY[i]) * (polyX[j] - polyX[i]) < x):
               oddNodes = not oddNodes
         j = i 
      return oddNodes or self.IsOnBorder(points, p)

   def IsInPolygonX(self, points, p) -> bool:
      vertical_lines = []
      for ix, p1 in enumerate(points):
         np = points[(ix + 1) % len(points)]
         if p1[0] == np[0]:
            if p1[1] < np[1]:
               vertical_lines.append((p1, np))
            else:
               vertical_lines.append((np, p1))
      #print("vertical lines:")
      #print(vertical_lines)
      #a = input()
      print("IsInPolygon", p)
      vlines = [True for l in vertical_lines if p[0] < l[0][0] and l[0][1] <= p[1] <= l[1][1]]
      print("vlines:", len(vlines))
      print(vlines)
      bb = input()
      return (len(vlines) % 2 == 1) or self.IsOnBorder(points, p)

   def IsRectInPolygon(self, p1, p2, points) -> bool:
      pp1 = (min(p1[0], p2[0]), min(p1[1], p2[1]))
      pp2 = (max(p1[0], p2[0]), max(p1[1], p2[1]))
      tr = (pp2[0], pp1[1])
      bl = (pp1[0], pp2[1])

      return self.IsInPolygon(points, tr) and self.IsInPolygon(points, bl)
   """

   def IsRectInPolygon(self, p1, p2, points, lines) -> bool:
      pp1 = (min(p1[0], p2[0]), min(p1[1], p2[1]))
      pp2 = (max(p1[0], p2[0]), max(p1[1], p2[1]))
      tr = (pp2[0], pp1[1])
      bl = (pp1[0], pp2[1])

      #print("Trying")
      #print("TL: ", pp1)
      #print("TR: ", tr)
      #print("BL: ", bl)
      #print("BR: ", pp2)

      for line in lines:
         if line[0] == p1 or line[0] == p2 or line[1] == p1 or line[1] == p2:
            continue

         if self.DoLinesIntersect(pp1, tr, line[0], line[1]):
            return False
         if self.DoLinesIntersect(tr, pp2, line[0], line[1]):
            return False
         if self.DoLinesIntersect(bl, pp2, line[0], line[1]):
            return False
         if self.DoLinesIntersect(pp1, bl, line[0], line[1]):
            return False

      #print("YES")
      #aa = input()

      return True

   def DoLinesIntersect(self, l1a, l1b, l2a, l2b) -> bool:
      """
      line 1: l1a to l1b
      line 2: l2a to l2b
      """
      #print("Intersect ? ", l1a, "to", l1b, " and ", l2a, l2b)

      # if both vertical then return false
      if l1a[0] == l1b[0] and l2a[0] == l2b[0]:
         #print("both vertical")
         return False

      # if both horizontal then return false
      if l1a[1] == l1b[1] and l2a[1] == l2b[1]:
         #print("both horizontal")
         return False

      if l1a[0] == l1b[0]:
         va = l1a
         vb = l1b
         ha = l2a
         hb = l2b
      else:
         ha = l1a
         hb = l1b
         va = l2a
         vb = l2b

      va = (va[0], va[1] - 0.5)
      vb = (vb[0], vb[1] + 0.5)
      ha = (ha[0] - 0.5, ha[1])
      hb = (hb[0] + 0.5, hb[1])

      #print("hor: ", ha, hb)
      #print("ver: ", va, vb)

      if ha[0] < va[0] and hb[0] > va[0] and \
         va[1] < ha[1] and vb[1] > ha[1]:
         #print("intersect")
         return True

      #print("no intersect")

      return False

   def CalcLines(self, points):
      lines = []
      for ix, p1 in enumerate(points):
         np = points[(ix + 1) % len(points)]
         if p1[0] == np[0]:
            # vertical
            if p1[1] < np[1]:
               lines.append((p1, np))
            else:
               lines.append((np, p1))
         elif p1[1] == np[1]:
            # horizontal
            if p1[0] < np[0]:
               lines.append((p1, np))
            else:
               lines.append((np, p1))
         else:
            print("OOOOppps")
            aa = input()

      return lines

   def PartB(self):
      self.StartPartB()

      data = self.ParseInput()
      answer = 0

      points = [ (int(l[0]), int(l[1])) for l in [ (line.split(",")) for line in data ] ]
      lines = self.CalcLines(points)

      """
      minx = 1_000_000
      miny = 1_000_000
      maxx = 0
      maxy = 0
      for p in points:
         minx = min(minx, p[0])
         maxx = max(maxx, p[0])
         miny = min(miny, p[1])
         maxy = max(maxy, p[1])
      print(f"X : {minx} -> {maxx}")
      print(f"Y : {miny} -> {maxy}")

      for y in range(maxy + 2):
         for x in range(maxx + 2):
            print(f"({x}, {y})", "Yes" if self.IsInPolygon(points, (x, y) ) else "")
            a = input()
      """

      """
      for a, p1 in enumerate(points):
         for b, p2 in enumerate(points):
            if a >= b:
               continue
            area = self.CalcArea(p1, p2)
            if area > answer:
               if not self.IsRectInPolygon(p1, p2, points):
                  continue
               good = True
               for c, p3 in enumerate(points):
                  if a == c or b == c:
                     continue
                  if self.IsInRect(p1, p2, p3):
                     good = False
                     break
               if good:
                  print(p1, p2)
                  answer = area
      """

      for a, p1 in enumerate(points):
         for b, p2 in enumerate(points):
            if a >= b:
               continue
            area = self.CalcArea(p1, p2)
            if area > answer:
               #print(p1, p2)
               #aa = input()
               if not self.IsRectInPolygon(p1, p2, points, lines):
                  continue
               answer = area

      # Attempt 1: 4750092396 is too high
      # Attempt 2: 2679903198 is too high
      # Attempt 3: 1363080015 is too low

      self.ShowAnswer(answer)


if __name__ == "__main__":
   solution = Day9Solution()
   if len(sys.argv) >= 2 and sys.argv[1] == "test":
      solution.Test()
   else:
      solution.Run()

# Template Version 1.5

