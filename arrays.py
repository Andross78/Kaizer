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


def array_19(array):
    int_i = 0
    n = len(array)
    for i in range(1,n-1):
        if array[i] > array[0] and array[i] < array[-1]:
            int_i = i
    return int_i


def array_20(array,k,l):
    result = 0
    for i in range(k,l+1):
        result += array[i]
    return result


def array_21(array,k,l):
    amount = 0
    summ = 0
    for i in range(k,l+1):
        summ += array[i]
        amount += 1
    return summ / amount


def array_22(array,k,l):
    n = len(array)
    result = 0
    for i in range(n):
        if i < k or i > l:
            result += array[i]
    return result


def array_23(array,k,l):
    n = len(array)
    summ = 0
    amount = 0
    for i in range(n):
        if i < k or i > l:
            summ += array[i]
            amount += 1
    return summ / amount


def array_24(array):
    n = len(array)
    _min = array[0]
    for i in range(n):
        for j in range(i+1,n):
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]
    sub = array[1]-array[0]
    for i in range(2,n):
        if array[i] - array[i-1] == sub:
            continue
        else:
            return 0
    return sub
        

def array_25(array):
    n = len(array)
    _min = array[0]
    for i in range(n):
        for j in range(i+1,n):
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]
    div = array[1] // array[0]
    for i in range(2,n):
        if array[i] // array[i-1] == div:
            continue
        else:
            return 0
    return div


def array_26(array):
    n = len(array)
    for i in range(1,n):
        if (array[i] - array[i-1]) % 2 != 0:
            continue
        else:
            return i
    return 0


def array_27(array):
    n = len(array)
    for i in range(1,n):
        if (array[i] > 0) != (array[i-1] > 0):
            continue
        else:
            return i
    return 0


def array_28(array):
    n = len(array)
    _min = array[0]
    for i in range(2,n,2):
        if _min > array[i]:
            _min = array[i]
    return _min
    

def array_29(array):
    n = len(array)
    _max = array[1]
    for i in range(3,n,2):
        if _max < array[i]:
            _max = array[i]
    return _max


def array_30(array):
    n = len(array)
    amount = 0
    ids = []
    for i in range(1,n):
        if array[i] < array[i-1]:
            amount += 1
            ids.append(i-1)
    return ids


def array_31(array):
    n = len(array)
    amount = 0
    ids = []
    for i in range(1,n):
        if array[i] > array[i-1]:
            amount += 1
            ids.append(i)
    return ids[::-1]


def array_32(array):
    n = len(array)
    for i in range(1,n):
        if array[i] < array[i-1] and array[i] < array[i+1]:
            return i


def array_33(array):
    n = len(array)
    for i in range(1,n):
        if array[i] > array[i-1] and array[i] > array[i+1]:
            return i


def array_34(array):
    n = len(array)
    _max = None
    for i in range(1,n-1):
        if array[i] < array[i-1] and array[i] < array[i+1]:
            if _max is None or _max < array[i]:
                _max = array[i]
    return _max


def array_35(array):
    n = len(array)
    _min = None
    for i in range(2,n-1):
        if array[i] > array[i-1] and array[i] > array[i+1]:
            if _min is None or _min > array[i]:
                _min = array[i]
    return _min




