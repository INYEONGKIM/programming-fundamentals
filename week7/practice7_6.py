def get_integer(message,i,j):
    number = input(message)
    while not (i>=1 and j<=4):
        number = input(message)
    return int(number)