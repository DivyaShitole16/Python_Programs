print("Result")
print("="*40)
print("\t1.Addition")
print("\t2.Substraction")
print("\t3.Multiplication")
print("\t4.Division")
print("\t5.Mod")
print("="*40)
ch=int(input("Enter Your choice"))
print("*"*40)
match(ch):
	case 1:
		a=int(input("enter first number"))
		b=int(input("enter second number"))
		Result=a+b
		print("Addition of two numbers={}".format(Result))
	case 2:
		a=int(input("enter first number"))
		b=int(input("enter second number"))
		Result=a-b
		print("Substraction of two numbers={}".format(Result))
	case 3:
		a=int(input("enter first number"))
		b=int(input("enter second number"))
		Result=a*b
		print("Multiplication of two numbers={}".format(Result))
	case 4:
		a=int(input("enter first number"))
		b=int(input("enter second number"))
		Result=a/b
		print("Division of two numbers={}".format(Result))
	case 5:
		a=int(input("enter first number"))
		b=int(input("enter second number"))
		Result=a%b
		print("Mod of two numbers={}".format(Result))
	case _:
		print("Invalid Choice")
