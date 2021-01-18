def array_1(n):
    result = []
    for i in range(n):
        result.append(i*2+1)
    return result


def array_2(n):
    result = []
    for i in range(1,n+1):
        result.append(2**i) 
    return result 


def array_3(n,a,d):
    result = []
    for i in range(n):
        result.append(a + d*i)
    return result


def array_4(n,a,d):
    result = []
    for i in range(n):
        result.append(a*d**i)
    return result


def array_5(n):
    result = [1,1]
    f1 = 1
    f2 = 1
    for i in range(n-2):
        f1,f2 = f2,f1+f2
        result.append(f2)
    return result


def array_6(n,a,b):
    result = [a,b]
    for i in range(n-2):
        summ = 0
        for j in (result):
            summ += j
        result.append(summ)
    return result


def array_7(array):
    for i in array:
        return array[::-1]


def array_8(array):
    result = []
    for i in array:
        if i % 2 != 0:
            result.append(i)
    return result, len(result)


def array_9(array):
    result = []
    for i in array[::-1]:
        if i % 2 == 0:
            result.append(i)
    return result, len(result)


def array_10(array):
    result = []
    for i in array:
        if i % 2 == 0:
            result.append(i)
    for i in array[::-1]:
        if i % 2 != 0:
            result.append(i)
    return result


def array_11(array, k):
    i = k
    while i < len(array):
        print(array[i])
        i += k  

def array_12(array):
    n = len(array)
    i = 2
    while i < n:
        print(array[i])
        i += 2


def array_13(array):
    n = len(array)-1
    while n > 0:
        print(array[n])
        n -= 2


def array_14(array):
    n = len(array) - 1
    i = 2
    while i < n:
        print(array[i])
        i += 2
    j = 1
    while j < n:
        print(array[j])
        j += 2


def array_15(array):
    n = len(array) - 1
    i = 1
    while i < n:
        print(array[i])
        i += 2
    while n > 0:
        print(array[n])
        n -= 2


def array_16(array):
    n = len(array)-1
    for i in range((n//2)+1):
        print(array[i])
        print(array[n-i])


def array_17(array):
    n = len(array)-1
    for i in range(n//2):
        print(array[i*2])
        print(array[i*2+1])
        print(array[n-(i*2)-1])
        print(array[n-(i*2)-2])


def array_18(array):
    for i in array:
        if i < array[-1]:
            return i
    return 0