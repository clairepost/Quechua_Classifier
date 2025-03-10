import re

t = open('tena_lowland/pages_output.txt', "r", encoding='utf-8').read()

r_expression = r'(\([0-9]\.*[0-9]*\)\n.*\n.*\n.*\n.*’)'

# print(len(m), len(f))

resultFile = open('tena_lowland/results.txt', "w+")

results = re.findall(r_expression, t)

for r in results:
    resultFile.write(re.sub(r'([A-Z]: )', '', re.sub(r'(\([0-9]\.*[0-9]*\))', '', r)))
    resultFile.write('\n')

resultFile.close()
