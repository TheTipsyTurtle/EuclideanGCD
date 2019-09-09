# EuclideanGCD
This is the way of finding the GCD using euclid's theorem


Finding the Greatest common denominator of two numbers (n1 and n2) using the euclidean equation of writing the GCD
where a, b are arbitrary constants:
GCD(n1,n2) = a * n1 + b * n2

*CODE
n1=int(input("Please enter the smaller digit:"))
n2=int(input("please enter the larger digit:"))

if n2%n1==0:
	print("gcd is:",n1)
	exit()

check1=n1
i=1
while check1*i<n2:
	check1=n1*i
	i=i+1

check2=check1+n1

final1=n2-check1
final2=check2-n2


if final1<final2:
	print("gcd is:",final1)
else:
	print("gcd is:",final2)


