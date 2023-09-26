# 1
for x in range(0, 150):
    print(x)
# 2
for x in range(5,1000,5):
    print(x)
# 3
for x in range(0, 100):
    if x % 10 == 0:
        print("Coding Dojo")
    elif x % 5 == 0:
        print("Coding")
    else:
        print(x)
# 4
count = 0
for x in range(0,500000):
    if (x % 2 == 1):
        count += x
print(count)
# 5
for x in range(2018, 0, -4):
    print(x)
# 6
low_num = 0
high_num = 100
mult = 3
for x in range(low_num, high_num):
    if (x % mult == 0):
        print(x)