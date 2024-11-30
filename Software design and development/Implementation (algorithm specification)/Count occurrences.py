def count_occurrences(array, item):
    count = 0
    for element in array:
        if element == item:
            count += 1
            
    return count