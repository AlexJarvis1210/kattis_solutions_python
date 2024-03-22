with open('coding_qual_input.txt', 'r') as file:
    # Read the content of the file
    content = file.read()


def decode(message_file: str) -> str:
    """
    Returns the decoded message from a given text file.

    Input:
    - message_file: A string representing the path to a .txt file.

    Preconditions:
    - The text file is in the correct format, with each line containing a number followed by a word.
    - The file contains at least one line.

    Output:
    - A string representing the decoded message, with words corresponding to the numbers at the end of each pyramid line.

    Postconditions:
    - The function reads the file and creates a dictionary mapping numbers to words.
    - It then calculates the pyramid structure based on the assumption that each line in the pyramid has one more number than the previous line.
    - The function returns the concatenated words that correspond to the numbers at the end of each pyramid line.
    """

    # Open the file and read the lines
    with open(message_file, 'r') as file:
        lines = [line.strip() for line in file if line.strip()]

    # Process the lines to create a dictionary of numbers to words
    word_dict = {int(line.split(' ')[0]): line.split(' ')[1] for line in lines}

    # Initialise variables to calculate the pyramid structure
    pyramid_numbers = []
    next_number = 1
    i = 1  # Start with the 1st line of the pyramid

    # While the next number is in the dictionary, continue building the pyramid
    while next_number in word_dict:
        pyramid_numbers.append(next_number)
        i += 1  # Increment to move to the next line of the pyramid
        next_number += i  # Calculate the last number for the next line of the pyramid

    # Decode the message using the pyramid numbers
    decoded_message = ' '.join(word_dict[number] for number in pyramid_numbers)

    return decoded_message



decode(content)


