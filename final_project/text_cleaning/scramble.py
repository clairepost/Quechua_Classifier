import os
import random

def transform_file(input_path, output_path):
    total_words = 0  # Initialize the word counter
    words_to_shuffle = []  # List to hold all words for shuffling

    with open(input_path, 'r') as file:
        lines = file.readlines()  # Read all lines into a list

    with open(output_path, 'w') as output:
        # Process all lines except the last one
        for line in lines[:-1]:  
            parts = line.split()
            if len(parts) >= 2:
                count = int(parts[0])
                word = ' '.join(parts[1:])
                words_to_shuffle.extend([word] * count)  # Append the word 'count' times

        # Shuffle the list of words
        random.shuffle(words_to_shuffle)
        output.write(' '.join(words_to_shuffle) + '\n')  # Write all shuffled words as a single line

        total_words = len(words_to_shuffle)  # Update the total word count after shuffling

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

# Specify the directory path
directory_path = 'language_resources/corpus_crawler_text' 
output_directory = os.path.join(directory_path, '../scrambled_corpus_crawler')  # Output directory

process_directory(directory_path, output_directory)