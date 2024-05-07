from bs4 import BeautifulSoup
import re

file = "txt"

if file == "html":
    # Read the HTML content from a file
    with open('dialects/yauyos_quechua/SYQ_stories_compilation.txt', 'r', encoding='utf-8') as file:
        html_content = file.read()

    # Use BeautifulSoup to parse the HTML
    soup = BeautifulSoup(html_content, 'html.parser')

    module = "blue"

    if module is "bold":
        # Find all paragraphs
        paragraphs = soup.find_all('p')

        # Filter out paragraphs that contain bold tags and extract text from the others
        quechua_sentences = []
        for paragraph in paragraphs:
            if not paragraph.find('b'):
                # Extract text from each span within the paragraph
                spans = paragraph.find_all('span')
                sentence_parts = [span.get_text() for span in spans]
                full_sentence = ' '.join(sentence_parts)
                # Clean up any residual HTML entities or tags
                clean_text = re.sub(r'\s+<o:p></o:p>\s*', '', full_sentence).strip()
                quechua_sentences.append(clean_text)

        # Output to a text file
        with open('dialects/yauyos_quechua/txt/glossed_stories_compilation.txt', 'w', encoding='utf-8') as file:
            for sentence in quechua_sentences:
                file.write(sentence + '\n')

        print("Quechua sentences have been extracted and saved to 'quechua_sentences.txt'.")

    elif module is "blue":
        # Find all spans with the specific color style
        quechua_sentences = []
        spans = soup.find_all('span', style=lambda value: value and 'color:#C4000A' in value)

        for span in spans:
            text = span.get_text()
            # Clean up any residual HTML entities or tags
            clean_text = re.sub(r'\s+<o:p></o:p>\s*', '', text).strip()
            quechua_sentences.append(clean_text)

        # Output to a text file
        with open('dialects/yauyos_quechua/txt/SYQ_stories_compilation.txt', 'w', encoding='utf-8') as file:
            for sentence in quechua_sentences:
                file.write(sentence + '\n')

        print("Quechua sentences with specific blue color have been extracted and saved to 'quechua_colored_sentences.txt'.")


    elif module is "grey":
        # Find all spans with the specific color style
        quechua_sentences = []
        spans = soup.find_all('span', style=lambda value: value and 'color:#666767' in value)

        for span in spans:
            text = span.get_text()
            # Clean up any residual HTML entities or tags
            clean_text = re.sub(r'\s+<o:p></o:p>\s*', '', text).strip()
            quechua_sentences.append(clean_text)

        # Output to a text file
        with open('constitution.txt', 'w', encoding='utf-8') as file:
            for sentence in quechua_sentences:
                file.write(sentence + '\n')

        print("Quechua sentences with specific blue color have been extracted and saved to 'quechua_colored_sentences.txt'.")


    elif module is "bold_under":
        # Find all bold tags that are nested within underline tags
        quechua_words = []
        bold_tags = soup.find_all('b')

        for b in bold_tags:
            if b.find('u'):  # Check if the bold tag contains an underline tag
                text = b.get_text()
                # Clean up any residual HTML entities or tags
                clean_text = re.sub(r'\s+<o:p></o:p>\s*', '', text).strip()
                quechua_words.append(clean_text)

        # Output to a text file
        with open('quechua_bold_words.txt', 'w', encoding='utf-8') as file:
            for word in quechua_words:
                file.write(word + '\n')

        print("Quechua words in bold have been extracted and saved to 'quechua_bold_words.txt'.")

    elif module is "white_space":
        # Split the content into lines assuming each line is a separate word
        lines = html_content.split('\n')

        # Remove all types of whitespace within each line to form words
        processed_lines = [''.join(line.split()) for line in lines if line.strip() != '']

        # Join the processed lines with newline characters to form the final output
        final_output = '\n'.join(processed_lines)

        # Write the processed lines back to a file
        with open('output_text.txt', 'w', encoding='utf-8') as file:
            file.write(final_output)

        print("Processed text has been saved to 'output_text.txt'.")
    elif module == "garamond":

        # Find all spans with the font-family set to Garamond
        quechua_text = []
        spans = soup.find_all('span', style=lambda value: value and 'font-family:"Garamond"' in value)

        for span in spans:
            text = span.get_text()
            # Clean up any residual HTML entities or tags
            clean_text = re.sub(r'\s+<o:p></o:p>\s*', '', text).strip()
            if clean_text:  # Ensure only non-empty text is added
                quechua_text.append(clean_text)

        # Output to a text file
        with open('quechua_garamond_text.txt', 'w', encoding='utf-8') as file:
            for text in quechua_text:
                file.write(text + '\n')

        print("Quechua text formatted with Garamond has been extracted and saved to 'quechua_garamond_text.txt'.")

elif file == "txt":
    module = "times"
    if module == "trad":
        # Read the text from the file
        with open('dialects/bolivian_quechua/original/interview_santusa3.txt', 'r', encoding='utf-8') as file:
            lines = file.readlines()

        # Filter out lines that start with the '%trad' tag
        filtered_lines = [line for line in lines if not line.strip().startswith('%trad')]

        # Write the filtered lines back to a new file
        with open('dialects/bolivian_quechua/txt/interview_santusa3.txt', 'w', encoding='utf-8') as file:
            file.writelines(filtered_lines)

        print("Lines containing '%trad' have been removed and the cleaned text has been saved to 'output_text.txt'.")
    
    elif module == "times":
        # Read the text from the file
        with open('dialects/yauyos_quechua/transcripts.txt', 'r', encoding='utf-8') as file:
            lines = file.readlines()

        # Initialize a list to hold the Quechua lines
        quechua_lines = []

        # Iterate over lines in the file to detect timestamps and capture the following line
        for i in range(len(lines) - 1):  # Subtract 1 to prevent index error on last line
            # Check if the current line contains a timestamp pattern
            if re.search(r'\d{2}:\d{2}:\d{2}\.\d{3}', lines[i]):
                # Append the next line to the list, which should be the Quechua text
                quechua_lines.append(lines[i + 1].strip())  # Use strip to remove any leading/trailing whitespace

        # Write the Quechua lines to a new file
        with open('dialects/bolivian_quechua/txt/SYQ_stories_compilation.txt', 'w', encoding='utf-8') as file:
            for line in quechua_lines:
                file.write(line + '\n')

        print("Quechua lines have been extracted and saved to 'output_quechua_lines.txt'.")