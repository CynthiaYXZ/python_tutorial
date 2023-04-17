#
# Covariance for Python program
#
import statistics, math

def my_covariance(input_x, input_y):
    length = len(input_x)
    cov = 0 
    
    mean_x= statistics.mean(input_x)
    mean_y= statistics.mean(input_y)
    
    for x,y in zip(input_x,input_y):
        cov +=(int(x)-mean_x)*(int(y)-mean_y)
        
    cov = cov/length
    return cov

# 1. Input
input_x = [10,20,30]
input_y = [12,21,33]

# 2. Process
answer = my_covariance(input_x, input_y)
answer = round(answer, 2)

# 3. Output
print(f"Input X: {input_x}", f"Input Y: {input_y}")
print(f"Mean X: {statistics.mean(input_x)}", f"Mean Y: {statistics.mean(input_y)}")
print(f"Covariance: {answer}")
