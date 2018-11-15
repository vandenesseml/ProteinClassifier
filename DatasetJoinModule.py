import os
from sys import argv

from tqdm import tqdm


def join():
    dataset_1_filename = argv[1]
    dataset_2_filename = argv[2]
    os.chdir('./output')
    with open(dataset_1_filename, 'r', encoding='utf-8') as dataset:
        fileContents = dataset.read()
    dataset_1 = fileContents.split('\n')
    print('Create dataset 1')
    for index in tqdm(range(0, len(dataset_1))):
        dataset_1[index] = dataset_1[index].split(',')
        del dataset_1[index][(len(dataset_1[index]) - 1)]

    with open(dataset_2_filename, 'r', encoding='utf-8') as dataset:
        fileContents = dataset.read()
    dataset_2 = fileContents.split('\n')
    print('Create dataset 2')
    for index in tqdm(range(0, len(dataset_2))):
        dataset_2[index] = dataset_2[index].split(',')
    if len(dataset_1) == len(dataset_2):
        print('Join datasets')
        for index in tqdm(range(0, len(dataset_1))):
            dataset_1[index] = dataset_1[index] + dataset_2[index].copy()

        os.chdir('./../output/joins')
        base_1 = dataset_1_filename.split('.')[0]
        base_2 = dataset_2_filename.split('.')[0]
        fileOutput = open(
            'join_' + base_1 + '&' + base_2 + '.csv', 'w', encoding='utf-8')
        print('Save to file')
        for row in tqdm(dataset_1):
            for item in row:
                if row.index(item) == len(row) - 1:
                    fileOutput.write(str(item) + '\n')
                else:
                    fileOutput.write(str(item) + ',')


if __name__ == '__main__':
    join()
