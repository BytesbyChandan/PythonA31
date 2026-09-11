def power(x,y):
    try:
        f = x**y
    except TypeError:
        print("not use zero")
    else:
        print(f"The power is {y} on {x} is :{f}")
    finally:
        print("You ve got result")
power(34,3)
