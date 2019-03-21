def isleapyear(year):
    if year >= 0:
        return year%4==0 and not(year%100==0 and not(year%400==0))

    else:
        return None

# print(isleapyear(0))
# print(isleapyear(1))
# print(isleapyear(4))
#
# print(isleapyear(2010))
# print(isleapyear(2011))
# print(isleapyear(2012))
# print(isleapyear(2013))
# print(isleapyear(2016))
# print(isleapyear(1900))
# print(isleapyear(2000))
# print(isleapyear(2100))
# print(isleapyear(2200))
# print(isleapyear(2400))
#
# print(isleapyear(-2400))
