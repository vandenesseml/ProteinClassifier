import os

from tqdm import tqdm

classes = ['DNA', 'RNA', 'DRNA', 'nonDRNA']
os.chdir('./output')
filename = 'pseudo_dataset0.0.1.csv'
# read in the original, full dataset
with open(filename, 'r', encoding='utf-8') as scrape:
    fileContents = scrape.read()
dataset = fileContents.split('\n')
# change dir to output dir
os.chdir('./separated_class_datasets')
# create 2d array
print('Create 2D array')
for index in tqdm(range(0, len(dataset))):
    dataset[index] = dataset[index].split(',')
classIndex = len(dataset[0]) - 1
# build separate datasets for each class
for Class in classes:
    print('Build ' + Class + ' dataset')
    classSpecificDataset = []
    classSpecificDataset.append(dataset[0].copy())
    for index in tqdm(range(1, len(dataset))):
        classSpecificDataset.append(dataset[index].copy())
    print('Reduce ' + Class + ' dataset')
    for index in tqdm(range(1, len(classSpecificDataset))):
        try:
            if classSpecificDataset[index][classIndex] != Class:
                classSpecificDataset[index][classIndex] = 'False'
        except:
            del classSpecificDataset[index]
    # Write to file
    fileOutput = open(Class + '_dataset.csv', 'w', encoding='utf-8')
    print('Write ' + Class + ' dataset to file')
    for row in tqdm(classSpecificDataset):
        for item in row:
            if row.index(item) == len(row) - 1:
                fileOutput.write(str(item) + '\n')
            else:
                fileOutput.write(str(item) + ',')
