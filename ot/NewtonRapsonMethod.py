import math
from sympy import *
 
def fc(eq, val):
    try:
        res = eval(eq, {'__bultins__':None}, {'x': val})
        return res
    except Exception as e:
        print(f"An error occured {str(e)}")
 
def find_derivative(function):
    try:
        x = symbols('x')
        expr = function.replace('^', '**') 
        expr = function.replace('coz(x)', 'math.cos(x)') 
        expr = eval(expr, {'__builtins__': None}, {'x': x})
        differentiation = diff(expr, x)
        return differentiation
    except (SympifyError, TypeError, NameError) as e:
        return f"An error occurred: {str(e)}"
 
fx = "x**4-x-10"
dx = str(find_derivative(fx))
list1 = []
sd = 0
count = 0
while True:
    s = fc(fx, count)
    list1.append(s)
    if len(list1) >= 2:
        if list1[count] >= 0 and list1[count-1] < 0:
            sd = (count+(count-1))/2
            break
    count += 1
print("Seed Point :", sd)
 
while True:
    x = sd - fc(fx, sd)/fc(dx,sd)
    sd1 = x
    if round(sd, 6) == round(sd1, 6):
        print("Root : ", sd)
        break
    sd = sd1