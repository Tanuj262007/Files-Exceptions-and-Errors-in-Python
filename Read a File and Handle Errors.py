try:
    # Attempt to open and read the file
    with open('sample.txt', 'r') as file:
        print("If the file exists:")
        for line in file:
            print(line.strip())
except FileNotFoundError:
    # Handle the case when file doesn't exist
    print("If the file does not exist:")
    print("Error: Unable to find the file 'sample.txt'")
