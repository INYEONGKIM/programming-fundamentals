def input_float():
    while True:
        try:
            x=float(input("Put float : "))
            a,b,c=str(x).partition(".")
            if c=="0":
                return a
            else:
                return str(x)
        except ValueError as e:
            print(e,"is not float type")
print(input_float())