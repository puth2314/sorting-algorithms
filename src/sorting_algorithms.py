def bubble_sort(unsorted_arr):
    """
    Worst: O(n^2)
    Average: O(n^2)
    """
    copy_arr = list(unsorted_arr)
    arr_length = len(unsorted_arr)

    for iteration in range(arr_length - 1):
        for comparison in range(arr_length - 1 - iteration):
            if copy_arr[comparison] > copy_arr[comparison + 1]:
                copy_arr[comparison], copy_arr[comparison + 1] = copy_arr[comparison + 1], copy_arr[comparison]

    return copy_arr


# def insertion_sort(l):  # Worst:O(n^2), Average:O(n^2)
#     s = len(l)
#     for i in range(s-1):
#         for c in range(i+1, 0, -1):
#             if l[c] < l[c-1]:
#                 l[c], l[c-1] = l[c-1], l[c]
#             else:
#                 break
#     return l
#
#
# def selection_sort(l):
#     s = len(l)
#     for i in range(s-1):
#         m = i
#         for c in range(i+1, s):
#             if l[c] < [m]:
#                 m = c
#         l[i], l[m] = l[m], l[i]
#     return l

# TODO: merge_sort()

if __name__ == '__main__':
    pass
