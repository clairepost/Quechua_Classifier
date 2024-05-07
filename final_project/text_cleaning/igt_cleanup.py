import os

def extract_quechua_lines(source_directory, output_directory):
    # Ensure output directory exists
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # Process each file in the directory that ends with .txt
    for filename in os.listdir(source_directory):
        if filename.endswith(".txt"):
            source_file_path = os.path.join(source_directory, filename)
            output_file_path = os.path.join(output_directory, f"quechua_{filename}")

            with open(source_file_path, 'r', encoding='utf-8') as file:
                lines = file.readlines()

            quechua_lines = []
            i = 0
            while i < len(lines):
                line = lines[i].strip()
                if line == '' and i + 1 < len(lines):
                    quechua_line = lines[i + 1].strip()  # The next line should be Quechua
                    if quechua_line:  # Check if not empty
                        quechua_lines.append(quechua_line)
                    i += 5  # Skip the next 4 lines (translations and time) and the next blank line
                else:
                    i += 1

            with open(output_file_path, 'w', encoding='utf-8') as output_file:
                for line in quechua_lines:
                    output_file.write(line + '\n')

            print(f"Processed {filename} -> quechua_{filename}")


source_dir = 'language_resources/dialects/yauyos_quechua/original'
output_dir = 'language_resources/dialects/yauyos_quechua/txt'
extract_quechua_lines(source_dir, output_dir)
