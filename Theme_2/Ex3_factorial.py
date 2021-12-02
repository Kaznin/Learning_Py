n = 9
m = n

f = 1


# N!! = N * (N - 2) * (N - 4)...

while n > 1:
    f = f * n
    n = n - 2

print(f'!!{m} = {f}')