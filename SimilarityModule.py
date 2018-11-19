from difflib import SequenceMatcher
from collections import Counter

filename = './input/sequences_training.txt'
missing_key = 0
dna = []
rna = []
drna = []
nondrna = []
dna_sub = []
rna_sub = []
drna_sub = []
nondrna_sub = []
master = []
final = []


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


def check_count():
    print(len(dna))
    print(len(rna))
    print(len(drna))
    print(len(nondrna))
    print(missing_key)


def common_substring(sequence_list, empty_list):
    s = str(sequence_list)
    for n in range(1, len(s)):
        substring_counter = Counter(s[i: i + n] for i in range(len(s) - n))
        phrase, occurrence = substring_counter.most_common(1)[0]
        if occurrence > 5:
            print('Size: %3d:  Occurrences: %3d  Phrase: %r' % (n, occurrence, phrase))
            empty_list.append(phrase)
        else:
            break


def sequence_matcher():
    for sequence in dna:
        string1 = dna[0]
        string2 = dna[1]
        match = SequenceMatcher(None, string1, string2).find_longest_match(0, len(string1), 0, len(string2))
        initial_match = string1[match.a: match.a + match.size]


intake()
common_substring(dna, master)
common_substring(rna, master)
common_substring(drna, master)
common_substring(nondrna, master)
common_substring(master, final)

print(final)
