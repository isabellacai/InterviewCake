arr = [1, 2, 3, 4, 4, 5, 6, 7, 8]
def num_appear_twice(array):
    n = len(arr)-1
    sum_no_dup = (n*(n+1))/2
    return sum(arr) - int(sum_no_dup)
    # hashmap = set() # key: number, value: number of times that number appears
    # for num in array:
    #     if num in hashmap:
    #         return num
    #     else:
    #         hashmap.add(num)
    # return None



    # for each_num in range (1, n+1):
        # prev_num = None
        #
        # for each_num in arr:
        #     prev_num = each_num
        #     each_num =
        #     if each_num == prev_num:
        #         return each_num
    # for i in arr[:n]:
    #     if arr[i] == arr[i+1]:
    #         return arr[i+1]

print(num_appear_twice(arr))
