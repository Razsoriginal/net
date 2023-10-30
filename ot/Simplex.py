z = [5, 3, 7, 0, 0, 0]
var = ["B", "Cb", "x1", "x2", "x3", "S1", "S2", "S3", "Xb", "Ratio"]
top = ["Cj", "->"] + z + [" ", " "]
eq = [[1, 1, 2, 1, 0, 0, 22], [3, 2, 1, 0, 1, 0, 26], [1, 1, 1, 0, 0, 1, 18]]

ans = [top, var]
bot = []
for i in range(len(eq[0]) - 1):
    a = 0
    for j in range(len(eq)):
        a += (0*eq[j][i])
    bot.append(a - z[i])

fbot = ["Δj", "=", "Cj", "-Zj"] + bot
ratio = []
min1 = bot.index(min(bot))
for i in range(len(eq)):
    ratio.append(eq[i][-1]/eq[i][min1])
min2 = ratio.index(min(ratio))

for i in range(3):
    l = ["S" + str(i + 1), 0] + eq[i] + [ratio[i]]
    ans.append(l)
ans.append(fbot)

for i in range(len(ans)):
    for j in range(len(ans[0])):
        print(ans[i][j], end = " ")
    print()

print("\nPivot = ", eq[min2][min1])
