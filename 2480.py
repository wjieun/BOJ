num = list(map(int, input().split()))
cnt = {i:0 for i in range(1, 7)}

for n in num:
    cnt[n] += 1

k = [k for k, v in cnt.items() if v == max(cnt.values())]
face = max(k)

if max(cnt.values()) == 3:
    print(10000 + face * 1000)
elif max(cnt.values()) == 2:
    print(1000 + face * 100)
elif max(cnt.values()) == 1:
    print(face * 100)