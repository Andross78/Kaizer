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


def array_36(array):
    n = len(array)
    l_min = None 
    l_max = None
    _max = array[0]
    for i in range(1,n-1):
        if array[i] > array[i-1] and array[i] > array[i+1] or array[i] < array[i-1] and array[i] < array[i+1]:
            continue
        elif _max < array[i]:
            _max = array[i]
    if _max < array[-1]:
        return array[-1]
    return _max

##########################
def array_37(array):
    n = len(array)
    if n < 0:
        return 0

    counter = 0
    _raise = False
    for i in range(1,n):
        print(_raise)
        if array[i] > array[i-1]:
            if not _raise:
                counter += 1
                _raise = True 
        else:
            _raise = False 

    return counter

#do 39
##############
def array_40(array, r):
    n = len(array)
    el = array[0]:
    el_i = 0
    for i in range(1,n):
        if abs(el - r) > abs(array[i] - r):
            el = array[i]
            el_i = i
    return el_i


def array_41(array):
    n = len(array)
    int_1 = array[0]
    int_2 = array[1]
    _sum = int_1+int_2 
    for i in range(2,n):
        if _sum < array[i]+array[i-1]:
            _sum = array[i]+array[i-1]
            int_1, int_2 = array[i-1],array[i]
    return int_1, int_2


def array_42(array,r):
    n = len(array)
    int_1 = array[0]
    int_2 = array[1]
    _sum = int_1 + int_2
    for i in range(2,n):
        if abs(_sum - r) > abs((array[i-1]+array[i]) - r):
            _sum = array[i-1] + array[i]
            int_1,int_2 = array[i-1],array[i]
    return int_1,int_2
 

def array_47(array):
    n = len(array)
    uniq = n
    for i in range(n):
        for j in range(i+1,n):
            if array[i] == array[j]:
                uniq -= 1
                break
    return uniq


def array_44(array):
    n = len(array)
    for i in range(n):
        for j in range(i+1,n):
            if array[i] == array[j]:
                return i,j
    return 0


def array_45(array):
    n = len(array)
    int_1 = array[0]
    int_2 = array[1]
    sub = abs(int_1 - int_2)
    for i in range(n):
        for j in range(i+1,n):
            if sub > abs(array[i]-array[j]):
                sub = abs(array[i]-array[j])
                int_1,int_2 = array[i],array[j]
    return int_1,int_2


def array_46(array,r):
    n = len(array)
    int_1 = array[0]
    int_2 = array[1]
    _sum = int_1 + int_2
    for i in range(n):
        for j in range(i+1,n):
            if abs(_sum - r) > abs((array[i]+array[j]) - r):
                _sum = array[i]+array[j]
                int_1, int_2 = array[i],array[j]
    return int_1,int_2


def array_47(array):
    n = len(array)
    uniq = n
    for i in range(n):
        for j in range(i+1,n):
            if array[i] == array[j]:
                uniq -= 1
                break
    return uniq


def array_48(array):
    n = len(array)
    uniq = n
    first = True
    for i in range(n):
        for j in range(i+1,n):
            if array[i] == array[j]:
                if first:
                    uniq -= 2
                    first = False
                else:
                    uniq -= 1
                break
    return n-uniq


def array_49(array):
    n = len(array)
    for i in range(n):
        if array[i] < 0 or array[i] > n:
            return i
    return 0


def array_50(array):
    n = len(array)
    amount = 0
    for i in range(n-1):
        for j in range(i+1,n):
            if array[i]> array[j]:
                amount += 1
    return amount


def array_51(arr_a, arr_b):
    n = len(arr_a)
    for i in range(n):
        arr_a[i],arr_b[i] = arr_b[i],arr_a[i]
    return arr_a,arr_b


def array_52(array):
    n = len(array)
    new_arr = []
    for i in range(n):
        if i < 5:
            new_arr.append(array[i]*2)
        else:
            new_arr.append(array[i]/2)
    return new_arr


def array_53(arr_a, arr_b):
    n = len(arr_a)
    arr_c = []
    for i in range(n):
        if arr_a[i] > arr_b[i]:
            arr_c.append(arr_a[i])
        else:
            arr_c.append(arr_b[i])
    return arr_c


def array_54(array):
    '''prosto'''


def array_55(array):
    '''prosto'''


def array_56(array):
    '''prosto'''


def array_57(array):
    '''prosto'''


def array_58(array):
    n = len(array)
    new_arr = []
    int_i = 0
    for i in range(n):
        int_i += array[i]
        new_arr.append(int_i)
    return int_i


def array_59(array):
    n = len(array)
    new_arr = []
    int_i = 0
    for i in range(n):
        int_i += array[i]
        new_arr.append(int_i/(i+1))
    return new_arr


def array_60(array):
    n = len(array)
    new_arr = []
    for i in range(n):
        int_i = array[i]
        for j in range(i+1,n):
            int_i += array[j]
        new_arr.append(int_i)
    return new_arr

def array_61(array):
    n = len(array)
    new_arr = []
    for i in range(n):
        int_i = array[i]
        div = 1
        for j in range(i+1,n):
            int_i += array[j]
            div += 1
        new_arr.append(int_i/div)
    return new_arr


def array_62(array):
    '''prosto'''

############################
def array_63(arr_a, arr_b):
    arr_c = []
    n = len(arr_a)
    i = 0
    j = 0
    while i < n and j < n:
        if arr_a[i]>arr_b[j]:
            arr_c.append(arr_b[j])
            j += 1
        else:
            arr_c.append(arr_a[i])
            i += 1
    if i == 5:
        arr_c += arr_b[j:]
    else:
        arr_c += arr_a[i:]
    return arr_c
        
###########################
#array64

def array_65(array,k):
    n = len(array)
    for i in range(n):
        array[i] += k
    return array


def array_66(array):
    n = len(array)
    first = True
    for i in range(n):
        if array[i] % 2 == 0:
            if first:
                even = array[i]
                first = False
                array[i] += even
            else:
                array[i] += even
    return array

######################
def array_67(array):
    n = len(array)
    first = True
    for i in range(n-1,-1,-1):
        if array[i] % 2 != 0:
            if first:
                odd = array[i]
                first = False
                array[i] += odd
            else:
                array[i] += odd
    return array


def array_68(array):
    n = len(array)
    _min = array[0]
    _max = array[0]
    min_i = 0
    max_i = 0
    for i in range(1,n):
        if _min > array[i]:
            _min = array[i]
            min_i = i
        if _max < array[i]:
            _max = array[i]
            max_i = i
    array[min_i] = _max
    array[max_i] = _min 
    return array        


def array_69(array):
    n = len(array)
    for i in range(0,n,2):
        array[i], array[i+1] = array[i+1], array[i]
    return array


def array_70(array):
    n = len(array)
    half = n//2
    array = array[half:]+array[:half]
    return array


def array_71(array):
    return array[::-1]


def array_72(array,k,l):
    return array[:k-1]+array[l-1:k-2:-1]+array[l:]


def array_73(array,k,l):
    return array[:k]+array[l-2:k-1:-1]+array[l-1:]


def array_74(array):
    n = len(array)
    _min = array[0]
    _max = array[0]
    min_i = 0
    max_i = 0
    for i in range(1,n):
        if _min > array[i]:
            _min = array[i]
            min_i = i
        if _max < array[i]:
            _max = array[i]
            max_i = i
    if max_i > min_i:
        array = array[:min_i+1]+[0]*(max_i-min_i-1)+array[max_i:]
    else:
        array = array[:max_i+1]+[0]*(min_i-max_i-1)+array[min_i:]
    return array


def array_75(array):
    n = len(array)
    _min = array[0]
    _max = array[0]
    min_i = 0
    max_i = 0
    for i in range(1,n):
        if _min > array[i]:
            _min = array[i]
            min_i = i
        if _max < array[i]:
            _max = array[i]
            max_i = i
    if max_i > min_i:
        array = array[:min_i]+array[max_i:min_i-1:-1]+array[max_i+1:]
    else:
        array = array[:max_i]+array[min_i:max_i-1:-1]+array[min_i+1:]
    return array


def array_76(array):
    n = len(array)
    for i in range(1,n-1):
        if  array[i] > array[i-1] and array[i]> array[i+1]:
            array[i] = 0
    return array


def array_77(array):
    '''prosto'''


def array_78(array):
    n = len(array)
    for i in range(n):
        if i == 0:
            array[i] = (array[i]+array[i+1])/2
        elif i == n-1:
            array[i] = (array[i]+array[i-1])/2
        else:
            array[i] = (array[i]+array[i+1]+array[i-1])/3
    return array


def array_79(array):
    n = len(array)
    for i in range(1,n):
        array[-i] = array[-i-1]
    array[0] = 0
    return array


def array_80(array):
    n = len(array)
    for i in range(n-1):
        array[i]=array[i+1]
    array[n-1] = 0
    return array
    
############################
def array_81(array,k):
    n = len(array)
    array = [0]*k + a[:n-k]
    return array

##############################
def array_82(array,k):
    n = len(array)
    array = array[k:]+[0]*k
    return array

##############################
def array_83(array):
    n = len(array)
    last = array[n-1]
    for i in range(n-1,0,-1):
        array[i] = array[i-1]
    array[0]  = array[last]   
    # return [0]+array[:n-1]

#############################
def array_84(array):
    n = len(array)
    return array[1:n]+[0]


#############################3
def array_85(array,k):
    ...


#############################3
def array_86(array,k):
    ...


def array_87(array):
    n = len(array)
    digit = array[0]
    if digit > array[-1]:
            array = array[1:]+[digit]
    for i in range(2,n):
        if digit > array[i-1] and digit < array[i]:
            array = array[1:i]+[digit]+array[i:]
            return array
    return array


def array_88(array):
    n = len(array)
    digit = array[-1]
    if digit < array[0]:
        array = [digit]+array[:-1]
    for i in range(1,n-1):
        if digit < array[i] and digit > array[i-1]:
            array = array[:i]+[digit]+array[i:-1]
            return array
    return array
    

def array_89(array):
    n = len(array)
    digit_i = 0
    for i in range(1,n):
        if array[i]> array[i-1]:
            digit = array[i]
            digit_i = i
            break
    for i in range(n-1):
        if digit > array[i]:
            array = array[:i] + [digit] + array[i:digit_i] + array[digit_i+1:]
            return array


def array_90(array,k):
    array.remove(array[k])
    return array


def array_91(array,k,l):
    del array[k-1:l]
    return array


def array_92(array):
    n = len(array)
    for i in range(n):
        if array[i] % 2 == 0:
            array.remove[array[i]]
    return len(array), array


def matrix_1(m,n):
    primary = []
    for i in range(1,m+1):
        secondary =[]
        for j in range(n):
            secondary.append(i*10)
        primary.append(secondary)
    return primary
            