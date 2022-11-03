print("Area")
print("="*40)    
print("\t1.Area of Rectangle")
print("\t2.Area of Triangle")
print("\t3.Area of Square")
print("\t4.Area of Circle")
print("="*40)
ch=int(input("Enter your choice"))
print("*"*40)
match(ch):
  case 1:
	  l=int(input("Enter length"))
	  w=int(input("Enter width"))
	  area =l*w
	  print("Area of Rectangle={}".format(area))
  case 2:
	  b=int(input("Enter base"))
	  h=int(input("Enter height"))
	  area=(b*h)*1.5
	  print("Area of Triangle={}".format(area))
  case 3:
	  a=int(input("Enter side of Square"))
	  area=a**2
	  print("Area of Square={}".format(area))
  case 4:
      r=int(input("Enter radius"))
      area=3.14*(r**2)
      print("Area of Circle={}".format(area))
  case _:
	  print("Invalid Choice")
