n = int(input())
sum = 0
 
for i in range(n):
	x = int(input())
	sum = sum + x
 
sum = str(sum)
print(sum[:10])