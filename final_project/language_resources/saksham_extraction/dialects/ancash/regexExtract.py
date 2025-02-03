import re

re_pattern = r'(\([0-9][0-9]*\)(.*\n.*)\{.*\}(.*\n.*\n.*?’))'

t = open('dialects/ancash/pages_output.txt', "r").read()

m = re.findall(re_pattern, t)
# print(m[0][0])
resultFile = open('dialects/ancash/results.txt' , "w")
# resultFile.write(m[0])
for i in range(len(m)):
    # print(m[i])
    resultFile.write(m[i][0] + '\n\n')
resultFile.close()
