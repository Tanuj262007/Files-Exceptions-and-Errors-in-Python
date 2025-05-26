try:
    # Write initial content to file
    initial_text = input("Enter text to write to file: ")
    with open('output.txt', 'w') as file:
        file.write(initial_text + '\n')
    print("Data successfully written output.txt")

    # Append additional content
    additional_text = input("Enter additional text to append: ")
    with open('output.txt', 'a') as file:
        file.write(additional_text + '\n')
    print("Data succesfully appended.")


    # Read and display file contents
    print("\nFile contents of output.txt:")
    with open('output.txt', 'r') as file:
        content = file.read()
        print(content)

except FileNotFoundError:
    print("Error: File not found")
except IOError:
    print("Error: Unable to perform file operation")
except Exception as e:
    print(f"An error occurred: {str(e)}")
