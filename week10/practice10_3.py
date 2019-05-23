def input_float_one():
    while True:
        try:
            x=float(input("Put float : "))
            assert -1<x<1
            a,b,c=str(x).partition(".")
            if c=="0":
                return a
            else:
                return str(x)
        except ValueError as e:
            print(e,"is not float type")
        except AssertionError as e:
            print(x,"is not in -1.0~1.0")
print(input_float_one())