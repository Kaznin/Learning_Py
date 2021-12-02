a = [2, 1, 5, 1]

b = a.copy()
b.sort() # [1, 1, 2, 5]

min_value = b[0] # 1
max_value = b[-1] # 5

c = a.index(min_value) # 1
print(c)
e = a.index(max_value) # 2
print(e)

a.remove(min_value)
a.remove(max_value)

a.insert(c, max_value)
a.insert(e, min_value)

print(a)