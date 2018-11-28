import difflib

filename = './input/sequences_training.txt'
missing_key = 0
dna = []
rna = []
drna = []
nondrna = []
index = 0


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


def intake_target(src):
    with open(src, 'r', encoding='utf-8') as sequences:
        for sequence in sequences:
            result = similarity(sequence)
            text_file.write("matched: {} similarity: {}\n".format(result[0], str(result[1])))


# Only use for testing training data
def intake_target_test(src):
    global index
    with open(src, 'r', encoding='utf-8') as sequences:
        current = 0
        for sequence in sequences:
            if current != index:
                result = similarity(sequence)
                text_file.write("matched: {} similarity: {}\n".format(result[0], str(result[1])))
                index += 1
            else:
                pass
            current += 1


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

    print("Match: {} Best: {}".format(match, best))
    return [match, best]


def similarity_index(original, target):
    seq = difflib.SequenceMatcher()
    seq.set_seqs(original.lower(), target.lower())
    d = seq.ratio() * 100
    return d


def check_count():
    print(len(dna))
    print(len(rna))
    print(len(drna))
    print(len(nondrna))
    print(missing_key)


intake()
text_file = open("output/similarity/report1.txt", 'w+')
# intake_target("input/sequences_test.txt")
# intake_target_test(filename)
text_file.close()

# Test
similarity("ACDVSIEGNDSMQFNTKSIVVDKTCKEFTINLKHTGKLPKAAMGHNVVVSKKSDESAVATDGMKAGLNNDYVKAGDERVIAHTSVIGGGETDSVTFDVSKLKEGEDYAFFCSFPGHWSIMKGTIELGS")
