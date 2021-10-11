import math

ab = int(input())
bc = int(input())

hac = math.sqrt(ab*ab + bc*bc) / 2.0
hbc = bc / 2.0

ang = str(int(round(math.degrees(math.acos(hbc / hac)))))
print(ang + chr(176))
