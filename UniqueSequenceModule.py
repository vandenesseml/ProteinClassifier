from difflib import SequenceMatcher
from collections import Counter

# Globals
filename = './input/sequences_training.txt'
missing_key = 0
dna = []
rna = []
drna = []
nondrna = []


def intake():
    with open(filename, 'r', encoding='utf-8') as sequences:
        for sequence in sequences:
            line = sequence.rstrip().split(',')

            if line[1] == "DNA":
                dna.append(line[0])
            elif line[1] == "RNA":
                rna.append(line[0])
            elif line[1] == "DRNA":
                drna.append(line[0])
            elif line[1] == "nonDRNA":
                nondrna.append(line[0])


def common_substring(sequence_list, file_writer):
    s = str(sequence_list)

    for n in range(1, len(s)):
        substring_counter = Counter(s[i: i + n] for i in range(len(s) - n))
        phrase, occurrence = substring_counter.most_common(1)[0]

        if occurrence > 3:
            print('Size: %3d:  Occurrences: %3d  Phrase: %r' % (n, occurrence, phrase))
            file_writer.write('Size: %3d:  Occurrences: %3d  Phrase: %r \n' % (n, occurrence, phrase))
        else:
            break


def check_count():
    print(len(dna))
    print(len(rna))
    print(len(drna))
    print(len(nondrna))
    print(missing_key)


def find_unique():
    text_file = open("output/unique/dna.txt", 'w+')
    common_substring(dna, text_file)
    text_file.close()

    text_file = open("output/unique/rna.txt", 'w+')
    common_substring(rna, text_file)
    text_file.close()

    text_file = open("output/unique/drna.txt", 'w+')
    common_substring(drna, text_file)
    text_file.close()

    text_file = open("output/unique/nondrna.txt", 'w+')
    common_substring(nondrna, text_file)
    text_file.close()


# Matches longest common sub string. Not needed at this moment since common_substring is being used.
def sequence_matcher():
    for sequence in dna:
        string1 = dna[0]
        string2 = dna[1]
        match = SequenceMatcher(None, string1, string2).find_longest_match(0, len(string1), 0, len(string2))
        initial_match = string1[match.a: match.a + match.size]


intake()
find_unique()
