def div(x,y):
    try:
        division = x/y
    except TypeError:
        print("y should by non zero")
    else:
        print(f"The division is:{division}")
    finally:
        print('The solutiion done')

div(4,2)