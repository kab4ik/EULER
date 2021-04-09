#Каков самый большой делитель числа 600851475143, являющийся простым числом?
def decor(func):
    def two():
        res1 = []
        res2 = []
        r = func()
        for i in r:
            for c in range(1, i+1):
                if i % c ==0:
                    res1.append(i)
            if len(res1) == 2:
                res2.append(c)

            res1 = []
        print(max(res2))
    return two

@decor
def one():
    res = []
    x = 600851475143
    z = 2
    while z*z < x:
        if x%z == 0:
            res.append(z)
            z +=1
        else:
            z+=1
    return res
one()