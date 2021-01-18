def for_1(k, n):
    for i in range(k+1):
        print(n)
    

def for_2(a, b):
    n = 0
    for i in range(a,b+1):
        n += 1
        print(i)
    return n

def for_3(a, b):
    n = 0
    for i in range(b-1, a, -1):
        print(i)
        n += 1
    return n


def for_4(price, n):
    for i in range(1, n+1):
        print(i*price)


def for_5(price, n):
    for i in range(1,n+1):
        print((i*price)/10)

def for_6(price, n):
    for i in range(1, n, 2):
        print((i*price)/10 + 1)
    

def for_7(a, b):
    result = 0
    for i in range(a, b+1):
        result += i
    return result

def for_8(a, b):
    result = 1
    for i in range(a, b+1):
        result *= i
    return result 


def for_9(a,b):
    result = 0 
    for i in range(a, b+1):
        result += i**2 
    return result


def for_10(n):
    result = 0
    for i in range(1, n+1):
        result += 1/n


def for_11(n):
    result = 0
    for i in range(1,n+1):
        result += (n+i)**2
    return result


def for_12(n):
    result = 1
    for i in range(1, n+1):
        result *= (i+10) / 10
    return result 


def for_13(n):
    result = 0
    for i in range(1, n+1):
        result += ((i+10) / 10)*(-1)**(i+1)
    return result


def for_14(n):
    result = 0
    for i in range(1, 2*n+1, 2):
        result += i
    return result 


def for_15(a,n):
    result = 1
    for i in range(1,n+1):
        result *= a
    return result 


def for_16(a, n):
    for i in range(n+1):
        print(a**i)


def for_17(a,n):
    result = 0
    for i in range(n+1):
        result += a**i
    return result


def for_18(a,n):
    result = 0
    for i in range(n+1):
        result += (-a)**i   
    return result 


def for_19(n):
    result = 1 
    for i in range(1, n+1):
        result *= i
    return result 

def for_20(n):
    result = 0
    fact = 1
    for i in range(1, n+1):
        fact *= i
        result += fact
    return result


def for_21(n):
    result = 0
    fact = 1
    for i in range(1, n+1):
        fact *= i
        result += 1/fact
    return result 

#sprosit
def for_22(x,n):
    result = 1
    fact = 1
    x_n = 1
    for i in range(1,n+1):
        fact *= i
        x_n *= x
        result += x_n/fact
    return result 

#reshit
def for_23(x,n):
    result = x
    fact = 1
    sign = 1
    for i in range(3, n+1, 2):
        fact *= i * (i-1)
        div = ((x**i)/fact)
        sign *= -1
        result += div * sign
    return result


def for_25(x,n):
    result = 0
    for i in range(1, n+1):
        x = x/10
        p = ((x**i)/i) * (-1)**(i+1)
        result += p
    return result 


def for_33(n):
    f1 = 1
    f2 = 2
    result = [1,1]
    for i in range(n-2):
        f1,f2 = f2, f1+f2
        result.append(f2)
    return result

def for_36(n,k):
    result = 0
    for i in range(1, n+1):
        p = 1
        for j in range(1, k+1):
            p *= i
        result += p
    return result


def for_37(n):
    result = 0
    for i in range(1, n+1):
        p = 1
        for j in range(1, n+1):
            p *= i
        result += p
    return result 


def for_38(n):
    result = 0
    k = n 
    for i in range(1, n+1):
        p = 1
        for j in range(k):
            p *= i
        result += p
        k -= 1
    return result 


def for_39(a, b):
    for i in range(a, b+1):
        for j in range(1,i+1):
            print(i)


def for_40(a, b):
    counter = 1
    for i in range(a, b+1):
        for j in range(counter):
            print(i)
        counter += 1