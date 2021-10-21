# write the code to loop through and count all the evens. only 1 print statement
ans = 0

for num in range(0,101, 2):
  # you can use the modulus if you didnt want to use the 2 step range
  # if num % 2 == 0:
    ans += num

print(ans)