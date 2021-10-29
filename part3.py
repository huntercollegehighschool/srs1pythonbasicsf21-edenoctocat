"""
The function below is supposed to return True if the integer entered as the argument is prime, and False if it's not. Fix the code so that it runs the way it's supposed to.
"""

def isprime(number):
  for i in range(number/2):
    if number % i == 0:
      return False
    else:
      return True