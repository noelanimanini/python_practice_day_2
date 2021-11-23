# check to see if the number given is a prime number
def prime_checker(number):
  if number % 1 == 0 and number % 2 == 0:
    print(True)
  else: 
    print(False)

n = int(input("Check this number: "))
prime_checker(number=n)