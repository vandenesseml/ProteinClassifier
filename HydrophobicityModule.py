import os
from tqdm import tqdm

dataset = [[
    'POLAR', 'NEUTRAL', 'HYDROPHOBIC', 'Class'
]]
letters = [
    'A', 'R', 'N', 'D', 'C', 'E', 'Q', 'G', 'H', 'I', 'L', 'K', 'M', 'F', 'P',
    'S', 'T', 'W', 'Y', 'V'
]
polar = ['R', 'K', 'E', 'D', 'Q', 'N']
neutral = ['G', 'A', 'S', 'T', 'P', 'H', 'Y']
hydrophobic = ['C', 'V', 'L', 'I', 'M', 'F', 'W']

os.chdir('./input')
filename = 'sequences_training.txt'
with open(filename, 'r', encoding='utf-8') as scrape:
    fileContents = scrape.read()
sequenceList = fileContents.split('\n')

print('Clean sequences')
for element in tqdm(sequenceList):
    Sequence = element.split(',')[0]
    Class = element.split(',')[1]
    currentHydrophobicityList = [0, 0, 0]
    for char in Sequence:
        if char in letters:
            if char in polar:
                currentHydrophobicityList[0] = currentHydrophobicityList[0] + 1
            elif char in neutral:
                currentHydrophobicityList[1] = currentHydrophobicityList[1] + 1
            elif char in hydrophobic:
                currentHydrophobicityList[2] = currentHydrophobicityList[2] + 1
    list = []
    for element in currentHydrophobicityList:
        list.append(int(element) / len(Sequence))
    list.append(Class)
    dataset.append(list)

os.chdir('./../output')
fileOutput = open('hydrophobic_dataset.csv', 'w', encoding='utf-8')
print('Save to file')
for row in tqdm(dataset):
    for item in row:
        if row.index(item) == len(row) - 1:
            fileOutput.write(str(item) + '\n')
        else:
            fileOutput.write(str(item) + ',')
