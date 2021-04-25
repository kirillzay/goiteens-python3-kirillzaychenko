#1 задача

import datetime
def datetimenow():
    i = datetime.datetime.now()
    print(i)

datetimenow()
# 2 задача
def num(a):
    return a + 100

print(num(10))

#3 задача
def multiply(i):
    for x in range(0,11):
        print(i," x ", x, " = ", i * x)

multiply(2)

# 4 задача

def iseven(k):
    if k % 2 == 0:
        return True
    else:
        return False

x = iseven(44)
print(x)