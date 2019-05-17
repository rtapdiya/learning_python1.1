def quick_sort(input_list):
    quick_sort_helper( input_list, 0, len(input_list-1))


def quick_sort_helper(input_list, left_index, right_index):
    size = right_index-left_index + 1
    if size ==1:
        return
    pivot_index = find_pivot(input_list, left_index, right_index)
    quick_sort_helper(input_list, left_index, pivot_index-1)
    quick_sort_helper(input_list, pivot_index+1, right_index)


def find_pivot(input_list,left_index, right_index):
    pivot = input_list[left_index]
    pivot_index = left_index

    while left_index < right_index :
        while input_list[left_index] <= pivot:
            left_index += 1
        while input_list[right_index] >= pivot:
            right_index -= 1
        input_list[left_index], input_list[right_index] = input_list[right_index], input_list[left_index]
    input_list[pivot_index],input_list[right_index] = input_list[right_index], input_list[pivot_index]
    return right_index


