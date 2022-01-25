#https://practice.geeksforgeeks.org/problems/ugly-numbers2254/1

def getNthUglyNo(n):
    # code here
    count = 1
    num = 1

    while count < n+1:
        if (num == 1 or num % 2 == 0 or num % 3 == 0 or num % 5 == 0):
            num += 1
            count += 1
        else:
            num += 1

    return num-1


print(getNthUglyNo(15))
print(getNthUglyNo(4))