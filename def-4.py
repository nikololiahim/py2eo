def A(p1, p2): # 1:0-4:-1
    return (p1 < p2 ) # 2:2-2:15
def test(): # 4:0-5:38
    return (A(p1=1 , p2=3 ) != A(p2=1 , p1=3 ) ) # 5:2-5:38