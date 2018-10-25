import os

os.chdir('./input')
filename = 'sequences_training.txt'
with open(filename, 'r', encoding='utf-8') as scrape:
    fileContents = scrape.read()
sequenceList = fileContents.split('\n')
print(sequenceList)
