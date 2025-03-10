from pdfminer.high_level import extract_pages
from pypdf import PdfReader

dir = "lambayeque/"
fInput = "Taylor_Breve_Morfologia.pdf"

# pages = extract_pages(dir + fInput, maxpages=1)

# for p in pages:
#     text_boxes = p.groups

# print(text_boxes[0].get_text().replace('\n', ' '))

reader = PdfReader(dir + fInput)
number_of_pages = len(reader.pages)
fOutput = open(dir + fInput[:-3]+ "_pages_output.txt", "w")

for i in range(number_of_pages):
    page = reader.pages[i]
    text = page.extract_text()

    fOutput.write(text + '\n')

fOutput.close()