n, m = input().split()
arr = list(map(int, input().split()))
a = set(map(int, input().split()))
b = set(map(int, input().split()))

hap = 0
for i in arr:
    if i in a and i in b:
        pass
    elif i in a:
        hap += 1
    elif i in b:
        hap -= 1
    else:
        pass
print(hap)

