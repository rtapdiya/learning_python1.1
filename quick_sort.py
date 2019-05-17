def quick_sort(input_list):
    quick_sort_helper( input_list, 0, len(input_list)-1)


def quick_sort_helper(input_list, left_index, right_index):
    size = right_index-left_index + 1
    if size <=1:
        return
    pivot_index = find_pivot(input_list, left_index, right_index)
    right_index = pivot_index -1
    quick_sort_helper(input_list, left_index, right_index)
    left_index = pivot_index+1
    quick_sort_helper(input_list, left_index, right_index)


def find_pivot(input_list,left_index, right_index):
    pivot = input_list[left_index]
    pivot_index = left_index
    left_pointer = left_index + 1
    right_pointer = right_index
    while True:
        while left_pointer < right_pointer and input_list[left_pointer] <= pivot:
            left_pointer += 1
        while right_pointer >= left_pointer and input_list[right_pointer] >= pivot:
            right_pointer -= 1
        if left_pointer < right_pointer :
            input_list[left_pointer], input_list[right_pointer] = input_list[right_pointer], input_list[left_pointer]
        else:
            break
    input_list[pivot_index],input_list[right_pointer] = input_list[right_pointer], input_list[pivot_index]
    return right_pointer

input_list=[31,26,22,27,44,34,77,55,93]
# print find_pivot(input_list,1,5)
print quick_sort(input_list)
print input_list

