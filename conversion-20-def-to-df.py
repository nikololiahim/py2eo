df test(): # 1:0-6:71
    x = 5  # 2:2-2:6
    y = 3  # 3:2-3:6
    z = (y ** complex(x, y)) # 5:2-5:23
    return ((z.__class__ == complex ) and (z.imag.__class__ == z.real.__class__ )) # 6:2-6:71