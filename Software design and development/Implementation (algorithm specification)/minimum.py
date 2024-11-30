def find_minimum(scores):
    minimum = scores[0]
    for index in range(1, len(scores)):
        if scores[index] < minimum:
            minimum = scores[index]
            
    return minimum