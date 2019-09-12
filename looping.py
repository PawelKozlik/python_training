for i in range(1, 5):
    for j in range(1, 6):
        if i == j:
            print("[{:>4}]".format("*"), end='')
        elif i > j:
            print("[{:>4}]".format(">"), end='')
        else:
            print("[{:>4}]".format(i * j), end='')
    print()
