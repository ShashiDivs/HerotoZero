def sum(a,b):
    return a+b

#print(sum(20,30))

def sums(*args):
    res = 0
    for i in args:
        res += i
    return res

print(sums(20,30,40,50))