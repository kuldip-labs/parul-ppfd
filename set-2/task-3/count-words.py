def count_words_in_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            # Read the content
            content = file.read()

            # Split by whitespace to get individual words
            words = content.split()

            return len(words)

    except FileNotFoundError:
        return "Error: The file was not found."
    except Exception as e:
        return f"An error occurred: {e}"


# Usage
filename = 'sample.txt'
word_count = count_words_in_file(filename)

print(f"Total word count: {word_count}")