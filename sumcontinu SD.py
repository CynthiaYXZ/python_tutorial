#
# Covariance for Python program
#
import statistics, math

def my_sd(input):
    print(f'input : {input}')
    length = len(input)
    sum = 0
    mean = statistics.mean(input)
    print(f'mean : {mean}')
    for x in input:
        sum += (int(x) - mean)**2
    sum = sum / length
    output = math.sqrt(sum)
    return output
    
# 1.input
input = [10,20,30]
# 2. Process
answer = my_sd(input)
answer = round (answer, 3)
# 3. Output
print(f'answer: {answer}')