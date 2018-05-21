len_m = input()
m = input()
len_n = input()
n = input()

m = set(list(map(int, m.split())))
n = set(list(map(int, n.split())))

m_n = set(m.difference(n))
n_m = set(n.difference(m))

s = sorted(m_n.union(n_m))
for _ in s:
    print(_)


