def floo(x,y):
    try:
        div_value = x//y
    except ZeroDivisionError:
        print("Do not use zero")
    else:
        print(f"The final value is:{div_value}")
    finally:
        print("Floor Division Done.....!!!")

floo(5534546,34)
