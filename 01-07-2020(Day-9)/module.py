def isleap(year):
    if year%400 == 0 or (year%4 == 0 and year%100 != 0):
        return True
    return False


def hello(name):
    return "Hello  "+name+"  How do you do.. !"