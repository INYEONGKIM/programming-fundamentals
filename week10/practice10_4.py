class NegativeInteger(Exception): pass

def pascalTriangle(n,r):
    a=[[1],[1,1]]

    for i in range(2,n+1):
        for j in range(r+1):
            if j<=i:
                if j==0:
                    a.append([1])
                elif i==j:
                    a[i].append(1)
                else:
                    a[i].append(a[i-1][j-1]+a[i-1][j])
    return a[n][r]

def combination():
    print("This program computes combination of two natural numbers, n and r.")
    print("Press Control-C to quit.")
    print("Press Enter when you are ready.")
    while True:
        try:
            n=int(input("Enter n:"))
            r=int(input("Enter r:"))

            if n<0 or r<0: raise NegativeInteger

            assert r<=n

            print(n,"C",r," = ",pascalTriangle(n,r), sep="")

        except ValueError as e:
            print(e,"은 정수가 아닙니다.")

        except AssertionError:
            print("r <= n 을 만족하지 않습니다.")

        except NegativeInteger:
            if n<0:
                print("n >= 0 을 만족하지 않습니다.")
            else:
                print("r >= 0 을 만족하지 않습니다.")

        except KeyboardInterrupt:
            print("Goodbye!")
            break

combination()