while(1):
    x: list[int] = []
    y = int(input("please inter a dicimal number :"))
    while y > 0:
        if y == 1:
            x.extend([1, 0])
            break
        if y==3:
            x.extend([1, 1])
            break
        else:
            while y != 0:
                if y % 2 == 0:
                    x.extend([0])
                if y % 2 == 1:
                    x.extend([1])
                y = int(y // 2)
            continue

    x.reverse()
    print(x)
