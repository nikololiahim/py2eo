
def testFib1():
    f0 = 0
    f1 = 1
    ii = 0
    while (ii < 10):
        f2 = f0 + f1
        ii = ii + 1
        f0 = f1
        f1 = f2
        if ii == 9: break
    print(f0)
    return (34 == f0)
