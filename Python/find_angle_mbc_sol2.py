import math

ab = int(input())
bc = int(input())

ang = str(int(round(math.degrees(math.atan(ab / bc)))))
print(ang + chr(176))
