import time

# why do we have big o notation
# To evalute performance
# to find out the time it takes to complete a function
# different computers run at different print
# because we care about efficiency

# 0(n) -- linear
# 0(n^2) -- quadratic
# 0(1) -- constant -- the performance doesn't change regardless of input
# 0(log n) -- logarithmic -- every time we double the input size, we only add one extra step


def number_of_steps(num):
    # overall: 0(log n)
    # 0(1) + 0(log n + c) --> 0(c log n + 1) --> 0(log n)
    steps = 0  ## constant 0(1)
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


"""
Classify the runtime complexity of the sorted_squares function below using Big O notation.
"""


def sorted_squares(A):
  ## overall runtime complexity? 0(4N + 5) --> 0(N)
    N = len(A)  ## constant 0(1)
    j = 0  ## constant 0(1)
    ## how many times does loop run? at most N times -- 0(N)
    while j < N and A[j] < 0:
        j += 1  ## constant 0(1)
        i = j - 1  ## constant 0(1)

    ans = []  ## constant 0(1)
    ## how many times does this loop run? N -- 0(N)
    while 0 <= i and j < N:
        if A[i]**2 < A[j]**2:  ## constant 0(1)
            ## appending to end of list is usually constant
            ans.append(A[i]**2)
            i -= 1
        else:
            ans.append(A[j]**2)
            j += 1
    ## how many times does this loop run? at most N
    while i >= 0:
        ans.append(A[i]**2)  ## constant 0(1)
        i -= 1
    while j < N:
        ans.append(A[j]**2)
        j += 1

    return ans


