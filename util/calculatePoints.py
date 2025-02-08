import math

def alphaNumericCalc(name):
    count = 0
    for c in name:
        if c.isalnum():
            count += 1
    return count

def roundDollar(total):
    return (float(total) * 100) % 100 == 0

def multiple25(price):
    return (float(price) * 100) % 25 == 0

def lenOfItemsCalc(items):
    return (len(items) // 2) * 5

def parseItems(items):
    res = 0
    for item in items:
        if len(item['shortDescription'].strip()) % 3 == 0:
            res += math.ceil(float(item['price']) * .2)
    return res

def getDayIsOdd(date):
    return int(date[-2:]) % 2 == 1


def checkTimes(time):
    return '14:00' <= time <= '16:00'