base = [[1, 2, 3], [4, 2, 9], [1, 2, 6]]

final_list = []
for item in base:
    for i in item:
        if i not in final_list:
            final_list.append(i)


def insertion_sort(arr):
    for i in range(1, len(arr)):
        temp_key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > temp_key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = temp_key
    return arr


print("the final list is", final_list)
print(insertion_sort(final_list))
