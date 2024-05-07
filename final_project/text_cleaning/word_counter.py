import os

def count_words_in_directory(directory):
    total_words = 0
    # Loop through each file in the directory
    for filename in os.listdir(directory):
        if filename.endswith('.txt'):
        # if filename.startswith('interview_san'):
            # Construct full file path
            filepath = os.path.join(directory, filename)
            # Open and read the file
            with open(filepath, 'r', encoding='utf-8') as file:
                content = file.read()
                # Count words in the file
                words = content.split()
                total_words += len(words)
                print(f"{filename}: {len(words)} words")
    print(f"Total words in directory: {total_words}")


directory_path = 'language_resources/dialects/yauyos_quechua/txt'
count_words_in_directory(directory_path)