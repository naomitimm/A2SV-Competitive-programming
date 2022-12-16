def sortColors(colors):
    red = 0
    white = 0
    blue = 0

    for color in colors:
        if color == 0:
            red += 1
        elif color == 1:
            white += 1
        elif color == 2:
            blue += 1

    sorted = []
    for _ in range(red):
        sorted.append(0)
    for _ in range(white):
        sorted.append(1)
    for _ in range(blue):
        sorted.append(2)


    print(sorted)



sortColors([2, 0, 1])