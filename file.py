def modify_content(content):
    # Example modification: convert text to uppercase
    return content.upper()

def main():
    # Ask for the filename
    filename = input("Enter the filename to read: ")

    try:
        # Attempt to open and read the file
        with open(filename, 'r') as file:
            content = file.read()

        # Modify the content
        modified_content = modify_content(content)

        # Define a new filename for the modified version
        new_filename = "modified_" + filename

        # Write the modified content to a new file
        with open(new_filename, 'w') as new_file:
            new_file.write(modified_content)

        print(f"Modified content has been written to {new_filename}")

    except FileNotFoundError:
        print("Error: The file does not exist.")
    except IOError:
        print("Error: The file could not be read or written to.")

if __name__ == "__main__":
    main()
