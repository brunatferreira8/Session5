for i in range(1, 10):
    print(i)

s = 0
for i in range(1, 11):
    s += i
    # s = s + 1
print(s)

i = 1
s = 0
while i <= 10:
    s += i
    i += 1 # this will break the loop!
    print("sum using while is also", s)


