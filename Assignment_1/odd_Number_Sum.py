def Main():
    sum = 0
    for i in range(100):
        if i % 2 != 0:
            sum = sum + 1
    print(str(sum))