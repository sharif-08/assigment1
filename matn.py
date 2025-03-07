import math
#Task 1
user=int(input("entera number: "))

def factorial(user):
    result=1
    for i in range(1,user+1):
        result=result*i
    return result
print(f'factorial of {user} is:',factorial(user))

#task 2
user_input=int(input("enter a number: "))
square=math.sqrt(user_input)
print("square root: ",square)
log=math.log(user_input)
print("logrithum: ",log)
sin=math.sin(user_input)
print("sine: ",sin)