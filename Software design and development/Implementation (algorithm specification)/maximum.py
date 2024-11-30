def find_maximum(scores):
    maximum = scores[0]
    for index in range(1, len(scores)):
        if scores[index] > maximum:
            maximum = scores[index]
            
    return maximum