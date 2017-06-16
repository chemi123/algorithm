# -*- coding: utf-8 -*-

from random import randint

def merge(left, right):
    merged_list = []
    left_pos, right_pos = 0, 0

    while left_pos < len(left) and right_pos < len(right):
        if left[left_pos] <= right[right_pos]:
            merged_list.append(left[left_pos])
            left_pos += 1
        else:
            merged_list.append(right[right_pos])
            right_pos += 1

    if left_pos < len(left):
        merged_list.extend(left[left_pos:])
    else:
        merged_list.extend(right[right_pos:])

    return merged_list


def merge_sort(list):
    if len(list) <= 1:
        return list

    mid = len(list) / 2
    left = list[:mid]
    right = list[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)


if __name__ == '__main__':
    unsorted_list = []
    for i in range(0, 100):
        unsorted_list.append(randint(1, 100))

    sorted_ist = merge_sort(unsorted_list)
    prev = 0
    for i in sorted_ist: 
        assert prev <= i
        prev = i
