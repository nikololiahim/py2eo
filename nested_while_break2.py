def nested_while_break2(): # 1:0-16:-1
    i = 1  # 2:2-2:6
    res = [] # 3:2-3:9
    while ((i <= 3  )): # 4:2-15:1
        j = 1  # 5:4-5:8
        while ((j <= 3  )): # 6:4-12:3
            if ((j == 2  )): # 7:16-9:5 
                break # 8:8-8:12

            res.append(j) # 9:6-9:18
            j+=1  # 10:6-10:11

        res.append(i) # 12:4-12:16
        i+=1  # 13:4-13:9

    return (res == [1 , 1 , 1 , 2 , 1 , 3 ] ) # 15:2-15:33