townname = []
try:
    with open('english_towns.txt', 'r') as english_towns:
        for counter in range(50):
            line = english_towns.readline()
            
            if not line:
                print(f"Reached end of file after reading {counter} towns.")
                break
            
            town = line.strip()
            townname.append(town)           
            print(f"townname[{counter}] = {town}")

except FileNotFoundError:
    print("The file 'english_towns.txt' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")