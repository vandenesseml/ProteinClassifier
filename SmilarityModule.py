import difflib

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


def similarity(original):
    best = 0.0
    match = "dna"

    for sequence in dna:
        value = similarity_index(sequence, original)

        if value > best:
            best = value
            match = "dna"

    for sequence in rna:
        value = similarity_index(sequence, original)

        if value > best:
            best = value
            match = "rna"

    for sequence in drna:
        value = similarity_index(sequence, original)

        if value > best:
            best = value
            match = "drna"

    for sequence in nondrna:
        value = similarity_index(sequence, original)

        if value > best:
            best = value
            match = "nondrna"

    print("matched: " + match)
    print("similarity: " + best)


def similarity_index (original, target):
    seq = difflib.SequenceMatcher()
    seq.set_seqs(original.lower(), target.lower())
    d = seq.ratio() * 100
    return d


intake()
similarity("MAARVGAFLKNAWDKEPVLVVSFVVGGLAVILPPLSPYFKYSVMINKATPYNYPVPVRDDGNMPDVPSHPQDPQGPSLEWLKKL")
