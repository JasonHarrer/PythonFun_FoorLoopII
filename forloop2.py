def run_test(testnum, testname, function, array):
    print(f'Test #{testnum}:\t{testname}')
    print(f'Starting Array: {array}')
    result = function(array)
    print(f'Ending  Result: {result}')
    print(f'Ending   Array: {array}')
    print()



def biggie_size(array):
    for i in range(len(array)):
        if array[i] > 0:
            array[i] = "big"


def count_positives(array):
    sum = 0
    for i in range(len(array)):
        if array[i] > 0:
            sum = sum + 1
    array[len(array)-1] = sum


def sum_total(array):
    sum = 0
    for i in array:
        sum = sum + i
    return sum


def average(array):
    sum = sum_total(array)
    return sum / len(array)


def length(array):
    return len(array)


def minimum(array):
    if len(array) == 0:
        return False

    minimum = array[0]
    for i in array:
        if(i < minimum):
            minimum = i
    return minimum


def maximum(array):
    if len(array) == 0:
        return False

    maximum = array[0]
    for i in array:
        if(i > maximum):
            maximum = i
    return maximum


def ultimate_analysis(array):
    analysis = {}
    analysis['sumTotal'] = sum_total(array)
    analysis['average'] = average(array)
    analysis['minimum'] = minimum(array)
    analysis['maximum'] = maximum(array)
    analysis['length'] = length(array)
    return analysis


def reverse(array):
    for i in range(int(len(array) / 2)):
        temp = array[i]
        array[i] = array[len(array)-i-1]
        array[len(array)-i-1] = temp


test_array_1 = [-3, 4, 0, 12, -14, 1]
test_array_2 = [-3, 4, 0, 12, -14, 1]
test_array_3 = [-3, 4, 0, 12, -7, 3]
test_array_4 = [-3, 4, 0, 12, -7, 3]
test_array_5 = [1, 7, 2, 3, 5, 7, 9, 1, 2, 78]
test_array_6 = [1, 7, 2, 3, -5, 7, 9, -13, 2, 78]
test_array_7 = [1, 7, 2, 3, -5, 7, 9, -13, 2, 78]
test_array_8 = [1, 7, 2, 3, -5, 7, 9, -13, 2, 78]
test_array_9_1 = [-3, 4, 0, 5, 12, -7, 3]
test_array_9_2 = [1, 7, 2, 3, -5, 7, 9, -13, 2, 78]


run_test(1, "Biggie Size", biggie_size, test_array_1)
run_test(2, "Count Positives", count_positives, test_array_2)
run_test(3, "Sum Total", sum_total, test_array_3)
run_test(4, "Average", average, test_array_4)
run_test(5, "Length", length, test_array_5)
run_test(6, "Minimum", minimum, test_array_6)
run_test(7, "Maximum", maximum, test_array_7)
run_test(8, "Ultimate Analysis", ultimate_analysis, test_array_8)
run_test(9, "Reverse (1)", reverse, test_array_9_1)
run_test(9, "Reverse (2)", reverse, test_array_9_2)
