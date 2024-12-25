from itertools import combinations


def stockPairs(stocksProfit, target):
    count = 0
    removed_duplicates = list(set(stocksProfit))
    new_sets = set(combinations(removed_duplicates, 2))
    for item in new_sets:
        if item[0] + item[1] == target:
            count += 1
    return count


profit_array = [7, 6, 6, 3, 9, 3, 5, 1]

target = 12


ds = stockPairs(profit_array, target)

print("the count is", ds)
