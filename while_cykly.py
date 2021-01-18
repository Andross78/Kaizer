def while_1(a,b):
    while a >= b:
        a -= b
    return a 


def while_2(a,b):
    counter = 0
    while a >= b:
        a -= b
        counter += 1
    return counter


def while_3(n,k):
    counter = 0
    while n >= k:
        n -= k
        counter += 1
    return counter, n


def while_4(n):
    while n >= 3:
        n /= 3
    return n == 1


def while_5(n):
    k = 0
    while n >= 2:
        n /= 2
        k += 1
    return k
    

def while_6(n):
    k = n
    while n-2 >= 0:
        n -= 2
        k *= n
    return k


def while_7(n):
    k = 1
    while k**2 <= n:
        k += 1
    return k


def while_8(n):
    k = 1
    while k**2 < n:
        k += 1
    k -= 1
    return k


def while_9(n):
    k = 1
    while n >= 3**k:
        k += 1
    return k


def while_10(n):
    k = 1
    while n >= 3**k:
        k += 1
    k -= 1
    return k


def while_11(n):
    k = 0
    counter = 0 
    while n > k:
        counter += 1
        k += counter
    return 'k :', k, 'counter :', counter


def while_12(n):
    k = 0 
    counter = 0
    while n > k:
        counter += 1
        k += counter
    k -= counter 
    counter -= 1
    return 'k :', k, 'counter :', counter


def while_13(a):
    k = 1
    sum = 0
    while a >= sum:
        sum += 1/k
        k += 1
    return 'sum :', sum, 'k :', k


def while_14(a):
    k = 1
    sum = 0
    while a >= sum:
        sum += 1/k
        k += 1
    sum -= 1/k
    k -= 1
    return 'sum :', sum, 'k :', k


def while_17(n):
    div = 10
    result = []
    while n / div > 0:
        result.append(n % div)
        n -= n % div
        n //= 10
    return result


def while_20(n):
    div = 10
    while n / div > 0:
        ost = n % div
        if ost == 2:
            return True
        else:
            n -= ost
            n //= 10
    return False 


def while_21(n):
    div = 10
    while n / div > 0:
        ost = n % div
        if ost % 2 == 0:
            return True
        else:
            n -= ost
            n //= 10
    return False 


def while_22(n):
    div = 2
    while div <= n // 2:
        if n % div == 0:
            return False
        else:
            div += 1
    return True 


def while_23(a,b):
    while a != 0 and b != 0:
    if a > b:
        a %= b
    else:
        b %= a

    
    print(a+b)

def while_24(n):
    f1 = 1
    f2 = 1
    while f2 = n:
        f1,f2 = f2,f1+f2
    return f2 == n


def while_25(n):
    f1 = 1
    f2 = 1
    while f2 <= n:
        f1,f2 = f2,f1+f2
    return f2


def while_26(n):
    f1 = 1
    f2 = 1
    while f2 != n:
        f1,f2 = f2,f1+f2
    f_1 = f2
    f_2 = n+f2
    return f_1, f_2 


def while_27(n):
    f1 = 1
    f2 = 1
    counter = 0
    while f2 < n:
        f1,f2 = f2,f1+f2
        counter += 1
        if f2 == n:
            counter += 1
            return counter 
    return False  