import os

from tqdm import tqdm

dataset = [[
    'A', 'R', 'N', 'D', 'C', 'E', 'Q', 'G', 'H', 'I', 'L', 'K', 'M', 'F', 'P',
    'S', 'T', 'W', 'Y', 'V', 'Class'
]]
letters = [
    'A', 'R', 'N', 'D', 'C', 'E', 'Q', 'G', 'H', 'I', 'L', 'K', 'M', 'F', 'P',
    'S', 'T', 'W', 'Y', 'V'
]
os.chdir('./input')
filename = 'sequences_training.txt'
with open(filename, 'r', encoding='utf-8') as scrape:
    fileContents = scrape.read()
sequenceList = fileContents.split('\n')

print('Clean sequences')
for element in tqdm(sequenceList):
    Sequence = element.split(',')[0]
    Class = element.split(',')[1]
    currentSequenceList = [
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
    ]
    for char in Sequence:
        if char in letters:
            if currentSequenceList[letters.index(char)] == 0:
                currentSequenceList[letters.index(char)] = 1
            else:
                currentSequenceList[letters.index(
                    char)] = currentSequenceList[letters.index(char)] + 1
    list = []
    for element in currentSequenceList:
        list.append(int(element) / len(Sequence))
    list.append(Class)
    dataset.append(list)

os.chdir('./../output')
fileOutput = open('dataset.csv', 'w', encoding='utf-8')
print('Save to file')
for row in tqdm(dataset):
    for item in row:
        if row.index(item) == len(row)-1:
            fileOutput.write(str(item) + '\n')
        else:
            fileOutput.write(str(item) + ',')
