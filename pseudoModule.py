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

fasta_format = ''
print('Clean sequences')
for element in tqdm(sequenceList):
    Sequence = element.split(',')[0]
    Class = element.split(',')[1]
    fasta = '>' + Class + '\n' + Sequence + '\n'

print()






os.chdir('./../output')
fileOutput = open('pseudo_dataset.csv', 'w', encoding='utf-8')
print('Save to file')
for row in tqdm(dataset):
    for item in row:
        if row.index(item) == len(row) - 1:
            fileOutput.write(str(item) + '\n')
        else:
            fileOutput.write(str(item) + ',')
