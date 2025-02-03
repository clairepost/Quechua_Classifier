import re

t = open('dialects/yauyos/pages_output.txt', "r").read()

m = re.split(r'(‘.*(\.|!|\?|(\n).*\.)’)', t)
f = re.findall(r'‘.*’[\n]', t)

# print(len(m), len(f))

resultFile = open('dialects/yauyos/results.txt', "w")
# resultFile.write(m[0])
for i in range(1, len(m), 4):
    # print("index is", i, m[i])
    # print("index is", m[i - 1] + m[i])
    # print("")
    # print(f[i])
    # resultFile.write(m[i])
    found = re.findall(r'\(.\)((.|\n)*)', m[i - 1] + m[i])
    if len(found) == 0:
        print("found", m[i - 1] + m[i])
    else:
        # print(found[0][0])
        resultFile.write(found[0][0] + "\n")
        resultFile.write("\n")
    # print("")
    
    #     print("found", m[i - 1] + m[i])
    # #     # print(found[0][0])
    #     resultFile.write(m[i])
    #     break
        # resultFile.write(f[i])
resultFile.close()
