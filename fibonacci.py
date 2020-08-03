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
print("The first " + na + " numbers of Fibonacci sequence are: " + lsta + ".")

print("Press Enter to continue...")
input()
