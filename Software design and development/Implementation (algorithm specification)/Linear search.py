def search_item(array, item):
    for index in range(len(array)):
        if array[index] == item:
            return index
        
    return -1