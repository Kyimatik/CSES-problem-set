n = int(input())
total_sum = (n * (n + 1)) // 2
if total_sum % 2 == 0:
    print("YES")
    mid = total_sum // 2
    set1 = []
    set2 = []
    for i in range(n, 0, -1):
        if i <= mid:
            set1.append(i)
            mid -= i
        else:
            set2.append(i)
    print(len(set1))
    print(" ".join(map(str, set1)))
    print(len(set2))
    print(" ".join(map(str, set2)))
else:
    print("NO")