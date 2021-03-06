#!/usr/bin/python
# -*- coding: utf-8 -*-


def quick_sort(data, left, right):
    start = left
    end = right

    if left >= right:
        return data

    # choose the first element to split list, there could be other choices
    tmp = data[left]
    while left < right:
        # find item that is left than tmp and move to left
        while left < right and data[right] >= tmp:
            right -= 1
        data[left] = data[right]

        # find item that is larger than tmp and move to right
        while left < right and data[left] <= tmp:
            left += 1
        data[right] = data[left]

    data[left] = tmp

    quick_sort(data, start, left - 1)
    quick_sort(data, left + 1, end)
    return data


def quick_sort_1(data, left, right):
    start = left
    end = right

    if left >= right:
        return data

    # choose the first element to split list, there could be other choices
    tmp = data[left]
    while left < right:
        # find item that is left than tmp and move to left
        while left < right and data[right] >= tmp:
            right -= 1
        # data[left] = data[right]

        # find item that is larger than tmp and move to right
        while left < right and data[left] <= tmp:
            left += 1

        data[left], data[right] = data[right], data[left]

    data[left] = tmp

    quick_sort(data, start, left - 1)
    quick_sort(data, left + 1, end)
    return data


def quick_sort_2(data, left, right):
    start = left
    end = right

    if left >= right:
        return data

    # choose the first element to split list, there could be other choices
    tmp = data[left]
    while left < right:
        # find item that is left than tmp
        while left < right and data[right] > tmp:
            right -= 1

        # find item that is larger than tmp
        while left < right and data[left] < tmp:
            left += 1

        # swap left and right to maintain left part contains elements <= tmp
        # right part contains elements >= tmp
        if left > right:
            break
        data[left], data[right] = data[right], data[left]
        left += 1
        right -= 1

    data[left] = tmp

    quick_sort(data, start, left - 1)
    quick_sort(data, left + 1, end)
    return data


def is_sorted(data):
    for i in range(1, len(data) - 1):
        if data[i-1] <= data[i]:
            continue
        else:
            return False
    return True


if __name__ == "__main__":
    from copy import deepcopy
    from random_list_generater import RandomListGenerator

    i = 0
    while i < 10000:
        i += 1

        # test_data = RandomListGenerator.random_list(10, 10)
        #
        # test_data_sort = deepcopy(test_data)
        # test_data_sort.sort()
        # test_data = [955, 785, 441, 878, 911, 967]
        # test_data = [7, 54, 7, 41, 8, 95]
        # test_data = [58, 91, 9, 63, 78, 61]
        # test_data = [66, 98, 49, 58, 93, 25]
        test_data = [5, 1, 9, 6, 3, 7, 4, 8, 2]

        # print("test data")
        # print(test_data)

        # sorted_data = quick_sort(test_data, 0, len(test_data) - 1)
        # sorted_data = quick_sort_1(test_data, 0, len(test_data) - 1)
        sorted_data = quick_sort_2(test_data, 0, len(test_data) - 1)
        print(is_sorted(sorted_data))

        # assert test_data_sort == sorted_data

        # print("result")
        # print(sorted_data)
