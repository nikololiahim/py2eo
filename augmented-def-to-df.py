df augmented(): # 1:0-26:-1
    x = 2  # 2:2-2:6
    x+=1  # 3:2-3:7
    plus = (x == 3  ) # 4:2-4:14
    x-=1  # 5:2-5:7
    minus = (x == 2  ) # 6:2-6:15
    x*=3  # 7:2-7:7
    mul = (x == 6  ) # 8:2-8:13
    x//=4  # 9:2-9:8
    div = (x == 1  ) # 10:2-10:13
    x<<=2  # 11:2-11:8
    shl = (x == 4  ) # 12:2-12:13
    x%=3  # 13:2-13:7
    mod = (x == 1  ) # 14:2-14:13
    x|=4  # 15:2-15:7
    orr = (x == 5  ) # 16:2-16:13
    x&=4  # 17:2-17:7
    andd = (x == 4  ) # 18:2-18:14
    x>>=1  # 19:2-19:8
    shr = (x == 2  ) # 20:2-20:13
    x**=4  # 21:2-21:8
    pow = (x == 16  ) # 22:2-22:14
    x^=24  # 23:2-23:13
    xorr = (x == 8  ) # 24:2-24:14
    return ((((((((((plus and minus) and mul) and div) and shl) and mod) and orr) and andd) and shr) and pow) and xorr) # 25:2-25:96