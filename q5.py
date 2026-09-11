def multi(x,y):
    try:
        mul_solution = int(x)*int(y)
    except TypeError:
        print("Do not use zero value")
    else:
        print(f"The value is:{mul_solution}")
    finally:
        print("u ve got final solution")

multi(23.45,67.89)
