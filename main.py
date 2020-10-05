import time


# why do we have big o notation
# To evalute performance
# to find out the time it takes to complete a function 
# different computers run at different print
# because we care about efficiency

# 0(n) -- linear
# 0(n^2) -- quadratic
# 0(1) -- constant -- the performance doesn't change regardless of input


def number_of_steps(num):
  # overall: 0(log n)
  # 0(1) + 0(log n + c) --> 0(c log n + 1) --> 0(log n)
  steps = 0           ## constant 0(1)
  ## how many times does the loop run? log n times
  while num > 0:      
    if num % 2 == 0:  ## code w/in the loop is constant 
      num = num // 2
    else:
      num = num - 1
    steps = steps + 1
  return steps
number_of_steps(16)

for i in [100, 1000, 10000, 100000]:
  print(f"number_of_steps | N: {i} \steps: {number_of_steps(i)}")

print("------")