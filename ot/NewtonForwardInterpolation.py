def forward_interpolation(x, fx, f):
    n = len(x)

    fd = [[0] * n for _ in range(n)]

    for i in range(n):
        fd[i][0] = fx[i]

    for j in range(1, n):
        for i in range(n - j):
            fd[i][j] = fd[i+1][j-1] - fd[i][j-1]

    for i in range(n):
        print(fd[i])

    y0 = fd[0][0]
    xt = 1.0

    for i in range(1, n):
        xt *= (f - x[i-1]) / (x[i] - x[0])
        y0 += fd[0][i] * xt

    return y0

x = [1951, 1961, 1971, 1981]
fx = [35, 42, 58, 84]
f = 1955
print(f"x : {x}")
print(f"fx : {fx}\n")
print(f"\nValue : {forward_interpolation(x, fx, f)}")