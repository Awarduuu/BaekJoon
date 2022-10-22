from bisect import bisect_left, bisect_right

n, x = map(int, input().split())

array = list(map(int, input().split()))

def count_x(array, x) :
    if x in array: 
        left_index = bisect_left(array,x)
        right_index = bisect_right(array,x)
        count = right_index - left_index
    else : 
        count = -1
    return count


print(count_x(array ,x))