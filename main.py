from part1 import trianglearea
from part2 import twodigitodd
from part3 import isprime
from part4 import possibletriangle
from part5 import isotriangle

program = int(input("Which program (1, 2, 3, 4, or 5)?"))

if program == 1:
  number = int(input("Enter a number: "))
  print(isprime(number))
  
if program == 2:
  number = int(input("Enter a number: "))
  print(twodigiteven(number))

if program == 3:
  month = input("Month: ")
  year = int(input("Year: "))
  print(daysinmonth(month, year))
  
if program == 4:
  side1 = int(input("Side 1: "))
  side2 = int(input("Side 2: "))
  side3 = int(input("Side 3: "))
  print(possibletriangle(side1, side2, side3))