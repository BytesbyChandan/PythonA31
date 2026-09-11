def conve(m):
    try:
        new_value = int(m)
    except:
        print("Enter any numerical value")
    else:
        print(f"The final value is: {new_value}")
    finally:
        print("The value is converted")  

print(conve(45.78))
