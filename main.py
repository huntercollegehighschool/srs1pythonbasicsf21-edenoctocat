from part1 import trianglearea
from part2 import twodigitodd
from part3 import isprime
from part4 import possibletriangle
from part5 import isotriangle

program = int(input("Which program (1, 2, 3, 4, or 5)? "))

if program == 1:
  number = int(input("Enter a number: "))
  if isprime(number) == True:
    print(str(number) + " is prime")
  else:
    print(str(number) + " is not prime")
  
if program == 2:
  number = int(input("Enter a number: "))
  if twodigitodd(number) == True:
    print(str(number) + " is a two digit odd number")
  else:
    print(str(number) + " is not a two digit odd number")

if program == 3:
  base = int(input("Base: "))
  height = int(input("Height: "))
  print("The area of the triangle is " + str(trianglearea(base, height)))

if program == 4:
  side1 = int(input("Side 1: "))
  side2 = int(input("Side 2: "))
  side3 = int(input("Side 3: "))
  if possibletriangle(side1, side2, side3) == True:
    print("This is a possible triangle")
  else:
    print("This is not a possible triangle")

if program == 5:
  leg = int(input("Leg length: "))
  print(isotriangle(leg))