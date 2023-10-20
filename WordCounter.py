from collections import defaultdict

def find_unique_words(file_path):
    """
    Function to read a text file and find unique words and their occurrences.

    Args:
    file_path (str): The path to the text file.

    Explanation:
    - This function takes a file path as an argument.
    - It initializes a defaultdict to store word occurrences, where the default value is set to 0.
    - The function attempts to open the file and read its content.
    - The text is split into words.
    - For each word in the text, the function updates the word count in the dictionary.
    - Finally, it prints the unique words and their occurrences.
    """

    word_counts = defaultdict(int)  # Dictionary to store word occurrences

    try:
        with open(file_path, 'r') as file:  # Open the file in read mode
            data = file.read()  # Read the content of the file
            words = data.split()  # Split the content into words

            # Iterate through each word and update the dictionary
            for word in words:
                word_counts[word] += 1

        # Print the unique words and their occurrences
        for word, count in word_counts.items():
            print(f"{word}: {count}")

    except FileNotFoundError:
        print(f"File not found at path: {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
file_path = r"C:/Users/kiran/Downloads/levitating.txt"  # your file path
find_unique_words(file_path)




