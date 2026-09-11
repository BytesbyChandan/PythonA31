def square(s):
    try:
        area = s*s
    except:
        print("only feed non zero value")
    else:
        print(f"The area is {area}")
    finally:
        print("congrats you ve got area")
square(0)