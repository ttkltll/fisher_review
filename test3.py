while True:
    try:
       str = input()
       list = str.split()
       print(len(list))
       for i in list:
           print(i)
    except:
        break