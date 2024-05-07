from bs4 import BeautifulSoup
import re

# Read the HTML content from a file
with open('../language_resources/dialects/ancash_quechua/original/dictianario_ancash.txt', 'r', encoding='utf-8') as file:
    html_content = file.read()

# Use BeautifulSoup to parse the HTML
soup = BeautifulSoup(html_content, 'html.parser')

module = "bold"  # Change this to switch between parsing modules

if module == "bold":
    # Code for extracting sentences that do not contain bold text
    quechua_sentences = []
    paragraphs = soup.find_all('p')
    for paragraph in paragraphs:
        if not paragraph.find('b'):
            spans = paragraph.find_all('span')
            sentence_parts = [span.get_text() for span in spans]
            full_sentence = ' '.join(sentence_parts)
            clean_text = re.sub(r'\s+<o:p></o:p>\s*', '', full_sentence).strip()
            quechua_sentences.append(clean_text)

    with open('ayacucho_conversation_llullmi.txt', 'w', encoding='utf-8') as file:
        for sentence in quechua_sentences:
            file.write(sentence + '\n')

    print("Quechua sentences have been extracted and saved.")

elif module == "blue":
    # Code for extracting sentences with a specific blue color
    quechua_sentences = []
    spans = soup.find_all('span', style=lambda value: value and 'color:#1F497D' in value)
    for span in spans:
        text = span.get_text()
        clean_text = re.sub(r'\s+<o:p></o:p>\s*', '', text).strip()
        quechua_sentences.append(clean_text)

    with open('quechua_colored_sentences.txt', 'w', encoding='utf-8') as file:
        for sentence in quechua_sentences:
            file.write(sentence + '\n')

    print("Quechua sentences with specific blue color have been extracted and saved.")

elif module == "garamond":
    # New code for extracting sentences styled with Garamond font
    quechua_sentences = []
    spans = soup.find_all('span', style=lambda value: value and 'font-family:"Garamond"' in value)
    for span in spans:
        text = span.get_text()
        clean_text = re.sub(r'\s+<o:p></o:p>\s*', '', text).strip()
        quechua_sentences.append(clean_text)

    with open('quechua_garamond_sentences.txt', 'w', encoding='utf-8') as file:
        for sentence in quechua_sentences:
            file.write(sentence + '\n')

    print("Quechua sentences styled with Garamond font have been extracted and saved.")
