# 1.Input
from math import sqrt
x1 = input("Enter x1:")
x2 = input("Enter x2:")
x3 = input("Enter x3:")
op = input("Enter operator:")

# 2.Process
if op== "+":
    sum=int(x1)+int(x2)+int(x3)
elif op== "-":
    sum=int(x1)-int(x2)-int(x3)
elif op== "*":
    sum=int(x1)*int(x2)*int(x3)
#elif op== "percent":
    #sum=int(x1)/int(x2)*100
elif op== "average":
    sum=(int(x1)+int(x2)+int(x3))/3
elif op== "sd":
    sum=sqrt(
	(
	(int(x1)-((int(x1)+int(x2)+int(x3))/3))**2+
	(int(x2)-((int(x1)+int(x2)+int(x3))/3))**2+
	(int(x3)-((int(x1)+int(x2)+int(x3))/3))**2
	)
	/3)
#
# 3.Output
print(f"Sum:{sum}")
