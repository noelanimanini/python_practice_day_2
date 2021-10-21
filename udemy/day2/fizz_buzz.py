# Your program should print each number from 1 to 100 in turn.

# When the number is divisible by 3 then instead of printing the number it should print "Fizz".

# `When the number is divisible by 5, then instead of printing the number it should print "Buzz".` 
#   `And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz"`
ans = []
# set up the for loop with the range
for num in range(1, 100):
  if num % 5 ==0 and num % 3 ==0:
    ans.append("FizzBuzz")
  elif num % 3 ==0:
    ans.append("Fizz")
  elif num % 5 ==0:
    ans.append("Buzz")
  else:
    ans.append(num)

print(ans)