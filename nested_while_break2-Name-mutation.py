def nested_while_break2(): # 1:0-16:57
    i = 1  # 2:4-2:8
    res2 = [] # 3:4-3:11
    while ((i <= 3  )): # 4:4-16:3
        j = 1  # 5:8-5:12
        while ((j <= 3  )): # 6:8-13:7
            if ((j == 2  )): # 7:40-10:11 
                break # 8:16-8:20

            res.append(j) # 10:12-10:24
            j+=1  # 11:12-11:15

        res.append(i) # 13:8-13:20
        i+=1  # 14:8-14:11

    return (res == [1 , 1 , 1 , 2 , 1 , 3 ] ) # 16:4-16:44