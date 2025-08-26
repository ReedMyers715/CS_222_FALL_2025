def Main():
    sum = 0
    for i in range(102):
        if i % 2 == 0:
            sum = sum + i
    print(str(sum))
