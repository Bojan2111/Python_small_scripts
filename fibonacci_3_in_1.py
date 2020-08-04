n = int(input("Enter number: "))
na = str(n)
lst = []
if n == 1:
	lst.append(0)
else:
	lst.append(0)
	lst.append(1)

i = len(lst)
while i<n:
	a = lst[len(lst) - 1] + lst[len(lst) - 2]
	lst.append(a)
	i = len(lst)

lsta = ', '.join(map(str, lst))
if n <= 0 :
	print("Invalid entry. Only numbers greater than 0.")
else :
	print("The first " + na + " numbers of Fibonacci sequence are: " + lsta + ".")

print("Press Enter to continue...")
input()

# Fibonaci to a specific number e.g. input=12, output=0, 1, 1, 2, 3, 5, 8; total length=7

x = int(input("Enter number: "))
xa = str(x)
flst = []

if x == 0:
	flst.append(0)
elif x == 1:
	flst.append(0)
	flst.append(1)
	flst.append(1)
else :
	flst.append(0)
	flst.append(1)

	fi = flst[len(flst) - 1]
	while fi < x:
		fa = flst[len(flst) - 1] + flst[len(flst) - 2]
		flst.append(fa)
		fi = flst[len(flst) - 1]
	
	if flst[len(flst) - 1] > x :
		flst.pop()

fres = ', '.join(map(str, flst))

if x < 0 :
	print("Invalid entry. Try again.")
else :
	print("Fibonacci sequence up to " + str(x) + " is: " + fres + ".")
	print("Total numbers in this sequence: " + str(len(flst)) + ".")

print("Press Enter to continue...")
input()

y  = int(input("Enter number: "))
fiblst = []

if y == 1 :
	fiblst.append(0)
else :
	fiblst.append(0)
	fiblst.append(1)

fii = len(fiblst)
while fii < y :
	fia = fiblst[len(fiblst) - 1] + fiblst[len(fiblst) - 2]
	fiblst.append(fia)
	fii = len(fiblst)

if y <= 0 :
	print("Invalid entry. Try again.")
else :
	fnum = fiblst.pop()
	print("The " + str(y) + ". number in Fibonacci sequence is: " + str(fnum))

print("Press Enter to continue...")
input()