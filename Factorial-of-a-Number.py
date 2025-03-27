# Factorial of a Number
def factorial(num):
    result = 1
    for i in range(2, num+1):
        result  *=i
    return result

num = int(input("Enter the number: "))

factorial = factorial(num)
print(factorial)



