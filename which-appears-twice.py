arr = [1, 2, 3, 4, 4, 5]
def num_appear_twice(n):
    # hashmap = {} # key: number, value: number of times that number appears

    for each_num in range (1, n+1):
        for each_num in arr:
            if each_num+1 == each_num:
                return each_num

print(num_appear_twice(6))
