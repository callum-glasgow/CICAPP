for counter in range(5):
    score[counter] = int(input('Please enter a score between 0 and 50: '))
    
    while not (0 <= score[counter] <= 50):
        score[counter] = int(input('You have not entered a score between 0 and 50. Please try again: '))
