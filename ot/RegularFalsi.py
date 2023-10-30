def fc(eq, val):
    try:
        res = eval(eq, {'__bultins__':None}, {'x': val})
        return res
    except Exception as e:
        print(f"An error occured {str(e)}")
        
fx = "x**3-2*x-5"
list1 = []
a = 0
b = 0
count = 0
while True:
    s = fc(fx, count)
    list1.append(s)
    if len(list1) >= 2:
        if list1[count] >= 0 and list1[count-1] < 0:
            a = count - 1
            b = count
            break
    count += 1

ans = []
while True:
    fx1 = fc(fx, a)
    fx2 = fc(fx, b)
    x = ((a * fx2) - (b * fx1))/(fx2 - fx1)
    ans.append(x)
    ffx = fc(fx, x)
    if ffx < 0:
        a = x
    if ffx > 0:
        b = x
    if len(ans) == 3:
        ans.pop(0)
        if round(ans[0], 6) == round(ans[1], 6):
            print("Root is : ", x)
            break  
    