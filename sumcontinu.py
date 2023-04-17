#
# Covariance for Python program
#
import statistics, math

def my_add(input):
    sum = 0 
    for x in input:
        sum += int(x)
    return sum

# 1.input
input = [23,45,63,75,83,92]
# 2. Process
answer = my_add(input)
# 3. Output
print(f'answer: {answer}')