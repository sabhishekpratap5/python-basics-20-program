# Fibonacci number

def fibonacci(num):
    if num == 0: 
        return 0
    elif num == 1:
        return 1
    # Recursive case
    else :
        return fibonacci(num-1) + fibonacci(num-2)
    
print(fibonacci(10))