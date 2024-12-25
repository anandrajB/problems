# smallesst subsring


def substring(n, arr):
    if n == 0:
        return 0

    # Find the minimum and maximum values
    min_val = min(arr)
    max_val = max(arr)

    # If min and max are same, return 1
    if min_val == max_val:
        return 1

    min_index = -1
    max_index = -1
    result = n

    # Iterate through array
    for i in range(n):
        if arr[i] == min_val:
            min_index = i
            # If we have found a max before this min
            if max_index != -1:
                result = min(result, abs(max_index - min_index) + 1)

        if arr[i] == max_val:
            max_index = i
            # If we have found a min before this max
            if min_index != -1:
                result = min(result, abs(max_index - min_index) + 1)

    return result


# Example usage:
n = 1
arr = [1, 5, 10, 7, 1, 9, 4]
print(substring(n, arr))
