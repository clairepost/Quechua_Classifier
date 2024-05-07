import xml.etree.ElementTree as ET
import os
import re


def extract_quechua_text(directory_path, output_directory):
    
    # Namespaces for parsing the Excel-formatted XML
    ns = {'ss': 'urn:schemas-microsoft-com:office:spreadsheet'}

    # Ensure the output directory exists
    os.makedirs(output_directory, exist_ok=True)
    
    # Regex to extract text strictly between quotes and ignore everything else on lines with quotes
    quote_regex = re.compile(r'.*?&quot;([^&quot;]+)&quot;.*')

    # Loop through each file in the directory
    for filename in os.listdir(directory_path):
        if filename.endswith('.xml'):
            xml_file_path = os.path.join(directory_path, filename)
            output_file_path = os.path.join(output_directory, filename.replace('.xml', '.txt'))

            # Parse the XML file
            tree = ET.parse(xml_file_path)
            root = tree.getroot()
            
            # Prepare to write extracted text
            lines_to_write = []
            
            # Iterate through each row in the Worksheet
            for row in root.findall('.//ss:Table/ss:Row', ns):
                for cell in row.findall('.//ss:Cell/ss:Data', ns):
                    if cell.text:
                        # Check if the line should be cleaned up based on dash count
                        if cell.text.count('-') < 3:
                            # Attempt to find a match for text within quotes
                            match = quote_regex.match(cell.text)
                            if match:
                                # If there is a match, append only the content within the quotes
                                lines_to_write.append(match.group(1) + '\n')
                            else:
                                # If there is no match, append the entire text
                                lines_to_write.append(cell.text + '\n')

            # Write all valid lines to the output file
            with open(output_file_path, 'w', encoding='utf-8') as output_file:
                output_file.writelines(lines_to_write)



def count_words_in_directory(directory):
    total_words = 0
    # Loop through all files in the directory
    for filename in os.listdir(directory):
        if filename.endswith('.txt'):
            file_path = os.path.join(directory, filename)
            # Read the contents of the file
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
                # Count words by splitting on whitespace
                words = content.split()
                total_words += len(words)
                print(f"{filename}: {len(words)} words")  # Optional: print word count per file

    print(f"Total words in directory: {total_words}")
    return total_words


directory_path = 'language_resources/dialects/bolivian_quechua/child_interviews'
output_directory = 'language_resources/dialects/bolivian_quechua/extracted_texts'
# extract_quechua_text(directory_path, output_directory)
count_words_in_directory(output_directory)
