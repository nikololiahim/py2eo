def nested_while_break1(): # 1:0-14:24
    i = 1  # 2:2-2:6
    j = 0  # 3:2-3:6
    res = [] # 4:2-4:9
    while ((i <= 4  )): # 5:2-14:1
        while ((j <= 3  )): # 6:4-12:3
            if ((j == 3  )): # 7:16-9:5 
                break # 8:8-8:12

            res.append((i * j)) # 9:6-9:22
            j-=1  # 10:6-10:11

        i-=1  # 12:4-12:9

    return (res == [0 , 1 , 2 ] ) # 14:2-14:24