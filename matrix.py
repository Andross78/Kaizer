import random


def matrix_1(m,n):
    primary = []
    for i in range(1,m+1):
        secondary =[]
        for j in range(n):
            secondary.append(i*10)
        primary.append(secondary)
    return primary


def matrix_2(m,n):
    primary = []
    for i in range(m):
        secondary =[]
        for j in range(1,n+1):
            secondary.append(j*5)
        primary.append(secondary)
    return primary 


def matrix_3(m_arr,n):
    m = len(m_arr)
    primary =[]
    for i in range(m):
        secondary = []
        for j in range(n):
            secondary.append(m_arr[i])
        primary.append(secondary)
    return primary


def matrix_4(n_arr, m):
    n = len(n_arr)
    primary = []
    for i in range(m):
        secondary = []
        for j in range(n):
            secondary.append(n_arr[j])
        primary.append(secondary)
    return primary


def matrix_5(m_arr,n,d):
    m = len(m_arr)
    primary = []
    for i in range(m):
        secondary = []
        el = m_arr[i]
        for j in range(n):
            secondary.append(el)
            el += d
        primary.append(secondary)
    return primary


def matrix_6(n_arr,m,q):
    n = len(n_arr)
    prev = n_arr
    primary = [prev]
    for i in range(m-1):
        secondary = []
        for j in range(n):
            secondary.append(prev[j]*q)
        primary.append(secondary)
        prev = secondary
    return primary


def matrix_7(m,n,k):
    primary = []
    for i in range(m):
        secondary = []
        for j in range(n):
            secondary.append(j)
        primary.append(secondary)
    print(primary[k])


def matrix_8(m,n,k):
    primary = []
    for i in range(m):
        secondary = []
        for j in range(n):
            secondary.append(j)
        primary.append(secondary)
    for i in range(m):
        print(primary[i][k])


def matrix_9(m,n):
    primary = []
    for i in range(m):
        secondary = []
        for j in range(n):
            secondary.append(j)
        primary.append(secondary)
    for i in range(0,m,2):
        print(primary[i])
            

def matrix_10(m,n):
    primary = []
    for i in range(m):
        secondary = []
        for j in range(n):
            secondary.append(j)
        primary.append(secondary)
    for i in range(m):
        for j in range(1,n,2):
            print(primary[i][j])


def matrix_11(m,n):
    primary = []
    for i in range(m):
        secondary = []
        for j in range(n):
            secondary.append(j)
        primary.append(secondary)
    for i in range(m):
        if i % 2 == 0:
            print(primary[i])
        else:
            print(primary[i][::-1])


def matrix_12(m,n):
    primary = []
    for i in range(m):
        secondary = []
        for j in range(n):
            secondary.append(i)
        primary.append(secondary)
    for i in range(m):
        for j in range(n):
            if j % 2 == 0:
                print(primary[i][j])
            else:
                print(primary[m-1-i][j])


def matrix_13(m):
    k = 1
    primary = []
    for i in range(m):
        secondary = []
        for j in range(m):
            secondary.append(k)
            k += 1
        primary.append(secondary)
    for i in range(m):
        for j in range(m-i):
            print(primary[i][j])
        for k in range(i+1,m):
            print(primary[k][m-i-1])


def matrix_14(m):
    k = 1
    primary = []
    for i in range(m):
        secondary = []
        for j in range(m):
            secondary.append(k)
            k += 1
        primary.append(secondary)
    for i in range(m):
        for j in range(m-i):
            print(primary[j][i])
        for k in range(i+1,m):
            print(primary[m-i-1][k])

    
def matrix_15(m):
    k = 1
    primary = []
    for i in range(m):
        secondary = []
        for j in range(m):
            secondary.append(k)
            k += 1
        primary.append(secondary)
    for i in range(m):
        for j in range(i,m-i):
            print(primary[i][j])
        for j in range(i+1,m-i):
            print(primary[j][m-i-1])
        for j in range(m-i-2,i-1,-1):
            print(primary[m-i-1][j])
        for j in range(m-2-i,i,-1):
            print(primary[j][i])


def matrix_16(m):
    k = 1
    primary = []
    for i in range(m):
        secondary = []
        for j in range(m):
            secondary.append(k)
            k += 1
        primary.append(secondary)
    print(primary)
    for i in range(m):
        for j in range(i,m-i):
            print(primary[j][i])
        for j in range(i+1,m-i):
            print(primary[m-i-1][j])
        for j in range(m-i-2,i-1,-1):
            print(primary[j][m-i-1])
        for j in range(m-i-2,i,-1):
            print(primary[i][j])

##################
def matrix_17(m,n,k):
    _sum = 0
    prod = 1
    k = 1
    primary = []
    for i in range(m):
        secondary = []
        for j in range(n):
            secondary.append(k)
            k += 1
        primary.append(secondary)
    for i in primary[k]:
        _sum += i
        prod *= i
    return primary,_sum, prod

##################
def matrix_18(m,n,k):
    _sum = 0
    prod = 1
    k = 1
    primary = []
    for i in range(m):
        secondary = []
        for j in range(n):
            secondary.append(k)
            k += 1
        primary.append(secondary)
    for i in primary:
        _sum += i[k]
        prod *= i[k]
    return primary,_sum, prod


def matrix_19(m,n):
    k = 1
    primary = []
    for i in range(m):
        secondary = []
        for j in range(n):
            secondary.append(k)
            k += 1
        primary.append(secondary)
    summas = []
    for i in primary:
        _sum = 0
        for j in i:
            _sum += j
        summas.append(_sum)
    return summas


def matrix_20(m,n):
    k = 1
    primary = []
    for i in range(m):
        secondary = []
        for j in range(n):
            secondary.append(k)
            k += 1
        primary.append(secondary)
    prods = []
    for i in range(m):
        prod = 1
        for j in range(n):
            prod *= primary[i][j]
        prods.append(prod)
    return prods


def matrix_21(m,n):
    k = 1
    primary = []
    for i in range(m):
        secondary = []
        for j in range(n):
            secondary.append(k)
            k += 1
        primary.append(secondary)
    summas = []
    for i in range(1,len(primary),2):
        _sum = 0
        for j in primary[i]:
            _sum += j
        summas.append(_sum)
    return summas


def matrix_22(m,n):
    k = 1
    primary = []
    for i in range(m):
        secondary = []
        for j in range(n):
            secondary.append(k)
            k += 1
        primary.append(secondary)
    summas = []
    for i in range(m):
        _sum = 0
        for j in range(0,n,2):
            _sum += primary[i][j]
        summas.append(_sum)
    return summas   


def matrix_23(m,n):
    k = 1
    primary = []
    for i in range(m):
        secondary = []
        for j in range(n):
            secondary.append(k)
            k += 1
        primary.append(secondary)
    mins = []
    for i in range(m):
        _min = primary[i][0]
        for j in range(1,n):
            if _min > primary[i][j]:
                _min = primary[i][j]
        mins.append(_min)
    return mins 


def matrix_24(m,n):
    k = 1
    primary = []
    for i in range(m):
        secondary = []
        for j in range(n):
            secondary.append(k)
            k += 1
        primary.append(secondary)
    maxs = []
    for i in range(n):
        _max = primary[0][i]
        for j in range(m):
            if primary[j][i] > _max:
                _max = primary[j][i]
        maxs.append(_max)
    return maxs
        


def matrix_25(m,n)
    k = 1
    primary = []
    for i in range(m):
        secondary = []
        for j in range(n):
            secondary.append(k)
            k += 1
        primary.append(secondary)
    sum_max = None
    for i in range(m):
        _sum = 0
        for j in range(0,n,2):
            _sum += primary[i][j]
        if sum_max is None or sum_max < _sum:
            sum_max = _sum
            ind_sum_max = i
    return ind_sum_max,sum_max


def matrix_26(m,n):
    k = 1
    primary = []
    for i in range(m):
        secondary = []
        for j in range(n):
            secondary.append(k)
            k += 1
        primary.append(secondary)
    prods = []
    prod_min = None
    for i in range(n):
        prod = 1
        for j in range(m):
            prod *= primary[j][i]
        if prod_min is None or prod_min > prod:
            prod_min = prod
            ind_prod_min = i
    return ind_prod_min, prod_min


def matrix_27(m,n):
    k = 1
    primary = []
    for i in range(m):
        secondary = []
        for j in range(n):
            secondary.append(k)
            k += 1
        primary.append(secondary)
    mins = []
    for i in range(m):
        _min = primary[i][0]
        for j in range(1,n):
            if _min > primary[i][j]:
                _min = primary[i][j]
        mins.append(_min)
    return max(mins) 


def matrix_28(m,n):
    k = 1
    primary = []
    for i in range(m):
        secondary = []
        for j in range(n):
            secondary.append(k)
            k += 1
        primary.append(secondary)
    maxs = []
    for i in range(n):
        _max = primary[0][i]
        for j in range(m):
            if _max < primary[j][i]:
                _max = primary[j][i]
        maxs.append(_max)
    return min(maxs)


def matrix_29(m,n):
    k = 1
    primary = []
    for i in range(m):
        secondary = []
        for j in range(n):
            secondary.append(k)
            k += 1
        primary.append(secondary)
    output = []
    for i in primary:
        result = 0
        for j in i:
            if j < (sum(i)/n):
                result += 1
        output.append(result)
    return output


def matrix_30(m,n):
    k = 1
    primary = []
    for i in range(m):
        secondary = []
        for j in range(n):
            secondary.append(k)
            k += 1
        primary.append(secondary)
    output = []
    for i in range(n):
        _sum = 0
        result = 0
        for j in range(m):
            _sum += primary[j][i]
        average = _sum/m
        for j in range(m):
            if primary[j][i] > average:
                result += 1
        output.append(result)
    return output


def matrix_31(m,n):
    k = 0
    _sum = 0
    primary = []
    for i in range(m):
        secondary = []
        for j in range(n):
            k += 1
            _sum += k
            secondary.append(k)
        primary.append(secondary)
    average = _sum/k
    _min = abs(average - primary[0][0])
    int_i = 0
    int_j = 0
    for i in range(m):
        for j in range(n):
            if _min > abs(primary[i][j] - average):
                _min = abs(primary[i][j] - average)
                int_i,int_j = i,j
    return _min, int_i,int_j, average


def matrix_32(m,n):
    primary = []
    for i in range(m):
        secondary = []
        for j in range(n):
            secondary.append(random.randint(-5,5))
        primary.append(secondary)
    for i in range(m):
        above = 0
        below = 0
        for j in primary[i]:
            if j > 0:
                above += 1
            elif j < 0:
                below += 1
        if above == below:
            return i, primary
    return 0, primary


def matrix_33(m,n):
    primary = []
    for i in range(m):
        secondary = []
        for j in range(n):
            secondary.append(random.randint(-5,5))
        primary.append(secondary)
    int_i = 0
    for i in range(n):
        above = 0
        below = 0
        for j in range(m):
            if primary[j][i] > 0:
                above += 1
            elif primary[j][i] < 0:
                below += 1
        if below == above:
            int_i = i
    return int_i, primary

###################
def matrix_34(m,n):
    primary = []
    for i in range(m):
        secondary = []
        for j in range(n):
            secondary.append(random.randint(0,5))
        primary.append(secondary)
    int_i = 0
    for line in range(m):
        even = []
        for i in primary[line]:
            if i % 2 == 0:
                even.append(i)
        if len(even) == n:
            int_i = line
    if int_i:
        return int_i, primary
    else:
        return None, primary  


def matrix_35(m,n):
    primary = []
    for i in range(m):
        secondary = []
        for j in range(n):
            secondary.append(random.randint(0,5))
        primary.append(secondary)
    for i in range(n):
        odd = []
        for j in range(m):
            if primary[j][i] % 2 != 0:
                odd.append(primary[j][i])
        if len(odd) == m:
            return i, primary
    return None, primary


def matrix_36(m,n):
    primary = []
    for i in range(m):
        secondary = []
        for j in range(n):
            secondary.append(random.randint(0,100))
        primary.append(secondary)
    first = sorted(primary[0])
    c = 0
    for i in range(1,m):
        if first == sorted(primary[i]):
            c += 1
    return c, primary


def matrix_37(m,n):
    primary = []
    for i in range(m):
        secondary = []
        for j in range(n):
            secondary.append(random.randint(0,100))
        primary.append(secondary)
    arr_1 = []
    arrays = []
    first = True
    for i in range(n):
        arr = []
        for j in range(m):
            arr.append(primary[j][i])
        if first:
            arr_1 = sorted(arr)
            first = False
        else:
            arrays.append(sorted(arr))
    c = 0
    for i in range(len(arrays)):
        if arrays[i] == arr_1:
            c += 1
    return c, primary
    

def matrix_38(m,n):
    primary = []
    for i in range(m):
        secondary = []
        for j in range(n):
            secondary.append(random.randint(0,9))
        primary.append(secondary)
    c = 0
    for line in primary:
        if len(set(line)) == len(line):
            c += 1
    return c


def matrix_39(m,n):
    primary = []
    for i in range(m):
        secondary = []
        for j in range(n):
            secondary.append(random.randint(0,9))
        primary.append(secondary)
    arrays = []
    for i in range(n):
        arr = []
        for j in range(m):
            arr.append(primary[j][i])
        arrays.append(sorted(arr))
    c = 0
    for i in arrays:
        if len(i) == len(set(i)):
            c += 1
    return c


def matrix_40(m,n):
    primary = []
    for i in range(m):
        secondary = []
        for j in range(n):
            secondary.append(random.randint(0,9))
        primary.append(secondary)
    _max = len(primary[0]) - len(set(primary[0]))
    int_i = 0
    for i in range(m):
        if _max <= len(primary[i]) - len(set(primary[i])):
            _max = len(primary[i]) - len(set(primary[i]))
            int_i = i
    return int_i


def matrix_41(m,n):
    primary = []
    for i in range(m):
        secondary = []
        for j in range(n):
            secondary.append(random.randint(0,9))
        primary.append(secondary)
    arrays = []
    for i in range(n):
        arr = []
        for j in range(m):
            arr.append(primary[j][i])
        arrays.append(arr)
    _max = len(arrays[0]) - len(set(arrays[0]))
    int_i = 0
    for i in range(1,n):
        if _max < len(arrays[i]) - len(set(arrays[i])):
            _max = len(arrays[i]) - len(set(arrays[i]))
            int_i = i
    return int_i


def matrix_42(m,n):
    primary = []
    for i in range(m):
        secondary = []
        for j in range(n):
            secondary.append(random.randint(0,9))
        primary.append(secondary)
    counter = 0
    for i in range(m):
        arr = [primary[i][0]]
        for j in range(1,n):
            if primary[i][j] >= primary[i][j-1]:
                arr.append(primary[i][j])
        if arr == primary[i]:
            counter += 1
    return counter, primary


def matrix_43(m,n):
    primary = []
    for i in range(m):
        secondary = []
        for j in range(n):
            secondary.append(random.randint(0,9))
        primary.append(secondary)
    arrays = []
    for i in range(n):
        arr = []
        for j in range(m):
            arr.append(primary[j][i])
        arrays.append(arr)
    counter = 0
    for i in range(n):
        arr = [arrays[i][0]]
        for j in range(1,m):
            if arrays[i][j] <= arrays[i][j-1]:
                arr.append(arrays[i][j])
        if arr == arrays[i]:
            counter += 1
    return counter, primary


def matrix_44(m,n):
    primary = []
    for i in range(m):
        secondary = []
        for j in range(n):
            secondary.append(random.randint(0,9))
        primary.append(secondary)
    mins = []
    for i in primary:
        if i == sorted(i) or i == sorted(i)[::-1]:
            mins.append(min(i))
    return mins,primary


def matrix_45(m,n):
    primary = []
    for i in range(m):
        secondary = []
        for j in range(n):
            secondary.append(random.randint(0,9))
        primary.append(secondary)
    arrays = []
    for i in range(n):
        arr = []
        for j in range(m):
            arr.append(primary[j][i])
        arrays.append(arr)
    counter = 0
    maxs = []
    for i in arrays:
        if i == sorted(i) or i == sorted(i)[::-1]:
            maxs.append(max(i))
    return maxs, primary