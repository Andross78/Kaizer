def minmax_1(array):
    if not array:
        return (None,None)
    n = len(array)
    min_int = array[0]
    for i in range(1,n):
        next_int = array[i]
        if min_int > next_int:
            min_int = next_int
    max_int = array[0]
    for i in range(1,n):
        next_int = array[i]
        if max_int < next_int:
            max_int = next_int
    return(min_int, max_int)    


def minmax_2(array):
    n = len(array)
    area_list = []
    for i in array:
        area_list.append(i[0]*i[1])
    min_area = area_list[0]
    for i in range(1,n):
        next_area = area_list[i]
        if min_area > next_area:
            min_area = next_area
    return area_list, min_area


def minmax_3(array):
    n = len(array)
    p_list = []
    for i in array:
        p_list.append(2*(i[0]+i[1]))
    max_p = p_list[0]
    for i in range(1,n):
        next_p = p_list[i]
        if max_p < next_p:
            max_p = next_p
    return p_list, max_p


def minmax_4(array):
    n = len(array)
    min_int = array[0]
    i_int = 0
    for i in range(1,n):
        if array[i] < min_int:
            min_int = array[i]
            i_int = i
    return array, i_int


def minmax_5(array)
    '''prosto'''
    ...


def minmax_6(array):
    n = len(array)
    min_int = array[0]
    max_int = array[0]
    for i in range(1,n):
        if array[i] < min_int:
            min_int = array[i]
            min_i = i
        elif array[i] > max_int:
            max_int = array[i]
            max_i = i
    return min_i, min_int, max_i, max_int 

def minmax_8(array):
    n = len(array)
    _min = array[0]
    int_1 = 0
    int_2 = 0
    for i in range(1,n):
        if array[i] < _min:
            _min = array[i]
            int_1 = i
            int_2 = i
        if array[i] == _min:
            int_2 = i
    return int_1, int_2



def minmax_12(array):
    n = len(array)
    max_int = array[0]
    for i in range(1,n):
        if max_int < array[i]:
            max_int = array[i]
    if max_int <= 0:
        return 0
    else:
        return max_int


def minmax_13(array):
    n = len(array)
    max_int = None
    max_i = 0
    for i in range(1,n):
        if array[i] % 2 != 0:
            if max_int is None or max_int < array[i]:
                max_int = array[i]
                max_i = i
    return max_i


def minmax_16(array):
    min_int = min(array)
    index_i = array.index(min_int)
    for i in range(0, index_i):
        print(array[i])


def minmax_22(array):
    n = len(array)
    min_1 = array[0]
    min_2 = array[0]
    for i in range(1,n):
        if min_1 >= array[i]:
            min_1,min_2 = array[i], min_1
    return min_1,min_2

def minmax_24(array):
    n = len(array)
    max_sum = array[0]+ array[1]
    for i in range(2,n):
        sum = array[i-1] + array[i]
        if sum > max_sum:
            max_sum = sum
    return max_sum

# *****************************************************

def minmax_7(array):
    n = len(array)
    max_digit = array[0]
    min_digit = array[0]
    max_i = 0
    min_i = 0
    for i in range(1,n):
        if max_digit <= array[-i]:
            max_digit = array[-i]
            max_i = n-i
        if min_digit >= array[i]:
            min_digit = array[i]
            min_i = i
    return max_i, min_i


def minmax_8(array):
    n = len(array)
    f_i = 0
    l_i = 0
    min_el = array[0]           
    for i in range(1,n):
        if min_el > array[i]:
            min_el = array[i]
            l_i = i
        if array[i] == min_el:
            l_i = i
    return f_i, l_i


def minmax_9(array):
    n = len(array)
    f_i = 0
    l_i = 0
    max_el = array[0]
    for i in range(1,n):
        if max_el < array[i]:
            max_el = array[i]
            f_i = i
        if array[i] == max_el:
            l_i = i
    return f_i, l_i

def minmax_10(array):
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
    if min_i < max_i:
        return min_i
    else:
        return max_i

def minmax_11(array):
    n = len(array)
    _min = array[0]
    _max = array[0]
    min_i = 0
    max_i = 0
    for i in range(1,n):
        if _min >= array[i]:
            _min = array[i]
            min_i = i
        if _max <= array[i]:
            _max = array[i]
            max_i = i
    if min_i > max_i:
        return min_i
    else:
        return max_i


def minmax_12(array):
    n = len(array)
    new_arr = []
    for i in array:
        if array[i] >= 0:
            new_arr.append(array[i])
    if new_arr == []:
        return 0
    n = len(new_arr)
    _min = new_arr[0]
    for i in range(1,n):
        if _min > new_arr[i]:
            _min = new_arr[i]
    return _min

def minmax_13(array):
    n = len(array)
    max_i = 0
    max_int = None
    for i in range(n):
        if array[i] % 2 != 0:
            if max_int is None or max_int < array[i]:
                max_int = array[i]
                max_i = i
    if max_i == None:
        return 0
    return max_i


def minmax_14(array,b):
    _min = None 
    n = len(array)
    min_i = 00
    for i in range(n):
        if array[i] > b:
            if _min is None or _min > array[i]:
                _min = array[i]
                min_i = i
    return min_i 


def minmax_15(array,b,c):
    _max = None
    n = len(array)
    max_i = 0
    for i in range(n):
        if array[i] > n and array[i] < c:
            if _max is None or _max < array[i]:
                _max = array[i]
                max_i = i
    return max_i 


def minmax_16(array):
    n = len(array)
    _min = array[0]
    min_i = 0
    for i in range(1,n):
        if _min > array[i]:
            _min = array[i]
            min_i = i
    return len(array[:min_i])


def minmax_17(array):
    n = len(array)
    _max = array[0]
    max_i = 0
    for i in range(1,n):
        if _max <= array[i]:
            _max = array[i]
            max_i = i
    return len(array[max_i:])


def minmax_18(array):
    n = len(array)
    _max = array[0]
    m_1 = None
    m_2 = None
    for i in range(1,n):
        if _max < array[i]:
            _max = array[i]
            m_1 = i
        if array[i] == _max:
            m_2 = i
    return len(array[m_1+1:m_2])


def minmax_19(array):
    n = len(array)
    _min = array[0]
    counter = 1
    for i in range(1,n):
        if _min > array[i]:
            _min = array[i]
            counter = 0
        if array[i] == _min:
            counter += 1
    return counter

#/////////////////////
def minmax_20(array):
    n = len(array)
    _min = array[0]
    _max = array[0]
    c_min = 1
    c_max = 1
    for i in range(1,n):
        if _min > array[i]:
            _min = array[i]
            c_min = 0
        if _max < array[i]:
            _max = array[i]
            c_max = 0
        if array[i] == _max:
            c_max += 1
        if array[i] == _min:
            c_min += 1
    return c_min+c_max 


# def minmax_21(array):
#     n = len(array)
#     summ = 0
#     counter = 0
#     _min = array[0]
#     _max = array[0]
#     for i in range(1,n):
#         if _min > array[i]:
#             counter += 1
#             summ += _min
#             _min = array[i]
#         if _max < array[i]:
#             counter += 1
#             summ += _max
#             _max = array[i]
#         else:
#             counter +=1
#             summ += array[i]


def minmax_22(array):
    n = len(array)
    min_1 = array[0]
    min_2 = array[0]
    for i in range(1,n):
        if min_1 > array[i]:
            min_2 = min_1
            min_1 = array[i]
    return min_1, min_2


def minmax_23(array):
    n = len(array)
    max_1 = array[0]
    max_2 = array[0]
    max_3 = array[0]
    for i in range(1,n):
        if max_1 < array[i]:
            max_3,max_2,max_1 = max_2,max_1,array[i]
        elif max_1 > array[i] and max_2 < array[i]:
            max_3, max_2 = max_2, array[i]
    return max_1, max_2, max_3

def minmax_25(array):
    n = len(array)
    prod = array[0]*array[1]
    i_1 = 0
    i_2 = 0
    for i in range(2,n):
        if prod > array[i-1]*array[i]:
            prod = array[i-1]*array[i]
            i_1 = i-1
            i_2 = i
    return i_1, i_2


