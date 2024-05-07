import os

def transform_file(input_path, output_path):
    total_words = 0  # Initialize the word counter
    with open(input_path, 'r') as file:
        lines = file.readlines()  # Read all lines into a list

    with open(output_path, 'w') as output:
        # Process all lines except the last one
        for line in lines[:-1]:  
            parts = line.split()
            if len(parts) >= 2:
                count = int(parts[0])
                word = ' '.join(parts[1:])
                repeated_word = (word + ' ') * count
                output.write(repeated_word + '\n')
                total_words += count * len(word.split())  # Multiply the count by the number of words in 'word'

    # Return total words count, excluding the last line
    return total_words

def process_directory(directory_path, output_directory):
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    for filename in os.listdir(directory_path):
        if filename.endswith(".txt"):
            input_path = os.path.join(directory_path, filename)
            output_path = os.path.join(output_directory, 'processed_' + filename)
            total_words = transform_file(input_path, output_path)
            print(f'Processed {filename} and saved in {output_directory}. Total words: {total_words}')
            print("\n")


directory_path = 'language_resources/corpus_crawler_text' 
output_directory = os.path.join(directory_path, '../processed_corpus_crawler')  # Output directory

process_directory(directory_path, output_directory)

