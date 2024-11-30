try:
    with open('english_towns.txt', 'w') as english_towns:
        for counter in range(50):
            town = townname[counter]
            english_towns.write(town + '\n')