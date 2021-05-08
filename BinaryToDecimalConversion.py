"""
Creator -Vijay Gunwant
Decimal Number System is a number sysytem with base 10. 
Binary Number System is a number system with base 2 . 
To convert Binary to Decimal we need to multiply the No. in binary with respective powers of 2 . Then add them all. 
Ex - 1000 in Decimal is 8 
			1 0 0 0 
			| | | |
			| | | |- 2 ^0 *0 = 0
			| | |- 2 ^ 1 * 0  = 0
			| |- 2 ^ 2 * 0 = 0
			|- 2 ^ 3 * 1 =0
		1000  = 0 + 0 + 0 + 8 = 8 
		(Binary)             (Decimal)
"""
n = input("Enter a Binary Number:")
print()
x = True
for a in n:
	if (a!="1") and (a!="0"):
		x = False
		break
if not(x):
	print("Invalid Character Entered!!")
else:
	print(n , end="")
	i = 0 #Powers 
	d = 0 #Decimal Numner
	for a in n[::-1]:
		d += (int(a) * (2 ** i))
		i += 1
	print(" in Decimal is ",d)