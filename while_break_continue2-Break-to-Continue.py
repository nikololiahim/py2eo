def continue_continue6(): # 1:0-12:33
    res = [] # 2:2-2:9
    n = 10  # 3:2-3:7
    while ((n > 0  )): # 4:2-12:1
        n-=1  # 5:4-5:9
        if ((n == 5  )): # 6:14-8:3 
            continue # 7:6-7:13
        elif ((n == 2  )): # 8:16-11:3 
            continue # 9:6-9:10

        res.append(n) # 11:4-11:16

    return (res == [9 , 8 , 7 , 6 , 4 , 3 ] ) # 12:2-12:33