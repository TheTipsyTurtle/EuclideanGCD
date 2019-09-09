#psuedo code:
#n1 and n2 are the two numbers whose gcd has to be found
#using the concept gcd(n1,n2)= a*n1 + b*n2
#
#
#if n1<n2
#check1 = last multiple of n1 smaller than n2
#check2 = first multiple of n1 bigger than n2
#
#find check1
#while check1<n2
#	check1=n1*i
#	i++
#
#find check2
#check2=check1-n1
#
#compare(check1-n2,n2-check2)
#gcd = smaller


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
	#print("loop entered",check1)
check2=check1+n1

final1=n2-check1
final2=check2-n2
#print(final2)

if final1<final2:
	print("gcd is:",final1)
else:
	print("gcd is:",final2)
#print("greater:",check1)
#print("smaller:",check2)

