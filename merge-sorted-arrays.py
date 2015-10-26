my_array = [3, 4, 6, 10, 11, 15]
alices_array = [1, 5, 8, 12, 14, 19]


def merge_arrays(arr1, arr2):
    merged_array_size = len(arr1) + len(arr2)
    merged_array = [None] * merged_array_size

    head_of_arr1 = arr1[0]
    head_of_arr2 = arr2[0]

    if head_of_arr1 < head_of_arr2:
        merged_array[0] = head_of_arr1

    else:
        merged_array[0] = head_of_arr2
        



# def merge_arrays(array1, array2):
#     return sorted(array1+array2)
#
#
# print(merge_arrays(my_array, alices_array))
#



# merged_array = []


# def merge_arrays(array1, array2):
#     for x in array1:
#         for y in array2:
#             if x < y:
#                 merged_array.append(x)
#                 merged_array.append(y)
#             if x > y:
#                 merged_array.append(y)
#                 merged_array.append(x)
#     return merged_array
#
# print(merge_arrays(my_array, alices_array))
