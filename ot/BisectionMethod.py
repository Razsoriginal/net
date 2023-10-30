import math
 
n = int(input("How many constraint you have : "))
lc = []
lp = []
for i in range(n):
    print("Enter coefficient ", i+1, end = " : ")
    c = int(input())
    lc.append(c)
    print("Enter its power : ", end = " ")
    p = int(input())
    lp.append(p)
 
list1 = []
roots = []
count = 0
while True:
    s = 0
    for i in range(n-1):
        s += lc[i] * (math.pow(count, lp[i]))
    s = s + lc[len(lc) - 1]
    list1.append(s)
    if len(list1) >= 2:
        if list1[count] >= 0 and list1[count-1] < 0:
            roots  = [count-1, count]
            break 
    count += 1
print("Roots lies between ", roots)
 
i = 0
while True:
    x = (roots[0] + roots[1])/2
    s = 0
    for j in range(n - 1):
        s += lc[j] * (math.pow(x, lp[j]))
    s = s + lc[len(lc) - 1]
    if s > 0:
        roots.remove(roots[1])
        roots.append(x)
        roots.sort()
    if s < 0:
        roots.remove(roots[0])
        roots.append(x)
        roots.sort()
    print("Roots lies between ", roots)
    i += 1
    if round(roots[0], 6) == round(roots[1], 6):
        break