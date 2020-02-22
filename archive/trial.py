def func(f=None):
    f = 20
    if f:
        x = 1
    else:
        x = 0
    print(x)

#func()

x = 20
#f = 30
for i in range(20):
    try:
        if x > f:
            print('{}: {} > {}'.format(i, x, f))
            pass
        else:
            print('{}: {} <= {}'.format(i, x, f))
            f += -20
    except:
        f = 100
        print('{}: f is defined as: {}'.format(i, f))