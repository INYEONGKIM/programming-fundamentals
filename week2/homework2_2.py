def front_ok(s):
    month = int(s[2:4])
    day = int(s[4:])

    if month>12 or day>31:
        return False
    else:
        if month==2:
            return day<29
        elif month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12:
            return day<32
        else:
            return day<31

def back_ok(s):
    return int(s[13])%10 == 11 - ((2*int(s[0]) + 3*int(s[1]) + 4*int(s[2]) + 5*int(s[3]) + 6*int(s[4]) + 7*int(s[5])
                                  + 8*int(s[7]) + 9*int(s[8]) + 2*int(s[9]) + 3*int(s[10]) + 4*int(s[11]) + 5*int(s[12]))%11)

def isRRN(s):
    (front, mid, back) = s.partition("-")
    return front_ok(front) and mid == "-" and back_ok(s)
