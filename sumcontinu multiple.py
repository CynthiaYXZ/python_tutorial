#
# Covariance for Python program
#
import statistics, math

def my_add(input):
    sum = 1
    for x in input:
        sum *= int(x)
    return sum

# 1.input
input = [1,2,3,4]
# 2. Process
answer = my_add(input)
# 3. Output
print(f'answer: {answer}')