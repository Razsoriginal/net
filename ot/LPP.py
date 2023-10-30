n = int(input("How many lines you have : "))
v = int(input("How many variables you have : "))
main = []
i = 1
while i < n + 1:
    an = []
    print("For line ", i, " :- ")
    for j in range(1, v + 1):
        print("Enter co-efficient of x", j, end = " : " )
        vv = int(input())
        an.append(vv)
    print("Enter value for line ", i, end = " : ")
    v1 = int(input())
    an.append(v1)
    main.append(an)
    i += 1

ans = []
for k in range(len(main)):
    eq = main[k]
    x = [eq[2]/eq[0], 0]
    y = [0, eq[2]/eq[1]]
    p = [x, y]
    ans.append(p)

for l in range(1, len(main) + 1):
    print("Points for line ", l, " :- ", ans[l-1])
