grade = {"A+": 4.5, "A0": 4.0, "B+": 3.5, "B0": 3.0, "C+": 2.5, "C0": 2.0, "D+": 1.5, "D0": 1.0, "F": 0.0}

g_sum = 0
c_sum = 0
for _ in range(20):
    L = list(input().split())
    if L[2] != "P":
        c_sum += float(L[1])
        g_sum += float(grade[L[2]]) * float(L[1])

print(g_sum / c_sum)