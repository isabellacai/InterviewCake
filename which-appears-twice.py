arr = [1, 2, 3, 4, 4, 5]
def num_appear_twice():
    # hashmap = {} # key: number, value: number of times that number appears
    # for each_num in range(arr)
    # for each_num in range (1, n+1):
        # prev_num = None
        #
        # for each_num in arr:
        #     prev_num = each_num
        #     each_num =
        #     if each_num == prev_num:
        #         return each_num
    for i in arr:
        if arr[i] == arr[i+1]:
            return i


print(num_appear_twice())
