def check(): # 1:0-9:33
    a : Int = 5 
    if ((a > 5  )): # 3:31-6:3 
        a = 7  # 4:8-4:12
        print("Hey!") # 5:8-5:20
    else: # 6:20-9:3
        a = 2  # 7:8-7:12
        print("Hi!") # 8:8-8:19
    return (a == 1  ) # 9:4-9:20