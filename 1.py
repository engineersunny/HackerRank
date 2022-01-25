import math

def calculateAmount(prices):
    # Write your code here
    sum = 0
    min = math.inf

    for idx, price in enumerate(prices):
        if idx == 0:
            sum += price
            min = price
        else:
            sum += max(price - min, 0)
            if price < min :
                min = price

    return sum

print(calculateAmount([4,9,2,3]))
print(calculateAmount([1,2,3,4]))
