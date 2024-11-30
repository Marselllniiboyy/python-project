import random
import math

a = int(input("Enter ur lower bound: "))
b = int(input("Enter ur upper bound: "))
num =random.randint(a,b)

maxGuess = int(math.log2(b - a + 1))  #int
print(f"Maximum number of guesses allowed: {maxGuess}")
guesses = 0
start = True

while start:
  guesses += 1
  print(f"Guesses {guesses}")
  guess = int(input("Guess the number: "))
  if guesses < maxGuess:
    if guess < num:
      print("Too low, try again!")
    elif guess > num:
      print("Too high, try again!")
    if guess == num:
      print(f"You guessed it! in {guesses} try; The number was", num)
      start = False
  else:
    print(f"Better Luck Next Time!, the number is {num}")
    start = False