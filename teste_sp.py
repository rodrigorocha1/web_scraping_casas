def loop_teste():
    a = [1, 2]
    b = [2, 4]
    return zip(a, b)


for e in loop_teste():
    print(e, type(e))