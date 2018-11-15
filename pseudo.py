#!/usr/bin/python

import string
from sys import argv

from tqdm import tqdm

#REF: http://www.csbio.sjtu.edu.cn/bioinf/PseAA/type1.htm

# USAGE: python PseAA.py <WeightFactor> <LambdaVal> <input fasta seq file> <output PseAAC file>
# It will generate input sequence log file (input_seq.log).
# Format: <seq serial num> <Class> <len seq(aa)> <seq(aa)>

printable = string.ascii_letters + string.digits + string.punctuation + ' '

#20 native amino acids according to the alphabetical order of their single-letter codes
aa_20 = [
    'A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R',
    'S', 'T', 'V', 'W', 'Y'
]


def aa_frequency(seq):
    aa_counts = {}
    for letter in seq:
        if letter in printable:
            aa_counts[letter] = aa_counts.get(letter, 0) + 1
    return aa_counts


def check_seq(seq):
    aa_freq = aa_frequency(seq)
    unknown_aa = []
    for key in aa_freq.keys():
        if key not in aa_20:
            unknown_aa.append(key)
    return unknown_aa


# The hydrophobicity values are from JACS, 1962, 84: 4240-4246. (C. Tanford).
H01 = {
    'A': 0.62,
    'C': 0.29,
    'D': -0.90,
    'E': -0.74,
    'F': 1.19,
    'G': 0.48,
    'H': -0.40,
    'I': 1.38,
    'K': -1.50,
    'L': 1.06,
    'M': 0.64,
    'N': -0.78,
    'P': 0.12,
    'Q': -0.85,
    'R': -2.53,
    'S': -0.18,
    'T': -0.05,
    'V': 1.08,
    'W': 0.81,
    'Y': 0.26
}
# Normalize (zero mean value; Eq. 4)
avg_H01Val = 0
for i1 in H01.keys():
    avg_H01Val += H01[i1] / 20

sum_diff_H01Val = 0
for i2 in H01.keys():
    sum_diff_H01Val += (H01[i2] - avg_H01Val)**2
sqrt_diff_H01Val = (sum_diff_H01Val / 20)**0.5

H1 = {}
for i3 in H01.keys():
    H1[i3] = (H01[i3] - avg_H01Val) / sqrt_diff_H01Val

# Check for "zero mean value"
#H1_sum=0
#for i in H1.values():
#    H1_sum += i
#print H1_sum/20

# The hydrophilicity values are from PNAS, 1981, 78:3824-3828 (T.P.Hopp & K.R.Woods).
H02 = {
    'A': -0.5,
    'C': -1.0,
    'D': 3.0,
    'E': 3.0,
    'F': -2.5,
    'G': 0.0,
    'H': -0.5,
    'I': -1.8,
    'K': 3.0,
    'L': -1.8,
    'M': -1.3,
    'N': 0.2,
    'P': 0.0,
    'Q': 0.2,
    'R': 3.0,
    'S': 0.3,
    'T': -0.4,
    'V': -1.5,
    'W': -3.4,
    'Y': -2.3
}
# Normalize (zero mean value; Eq. 4)
avg_H02Val = 0
for j1 in H02.keys():
    avg_H02Val += H02[j1] / 20

sum_diff_H02Val = 0
for j2 in H02.keys():
    sum_diff_H02Val += (H02[j2] - avg_H02Val)**2
sqrt_diff_H02Val = (sum_diff_H02Val / 20)**0.5

H2 = {}
for j3 in H02.keys():
    H2[j3] = (H02[j3] - avg_H02Val) / sqrt_diff_H02Val

# Check for "zero mean value"
#H2_sum=0
#for i in H2.values():
#    H2_sum += i
#print H2_sum/20

# The side-chain mass for each of the 20 amino acids.
M0 = {
    'A': 15.0,
    'C': 47.0,
    'D': 59.0,
    'E': 73.0,
    'F': 91.0,
    'G': 1.0,
    'H': 82.0,
    'I': 57.0,
    'K': 73.0,
    'L': 57.0,
    'M': 75.0,
    'N': 58.0,
    'P': 42.0,
    'Q': 72.0,
    'R': 101.0,
    'S': 31.0,
    'T': 45.0,
    'V': 43.0,
    'W': 130.0,
    'Y': 107.0
}
# Normalize (zero mean value; Eq. 4)
avg_M0Val = 0
for k1 in M0.keys():
    avg_M0Val += M0[k1] / 20

sum_diff_M0Val = 0
for k2 in M0.keys():
    sum_diff_M0Val += (M0[k2] - avg_M0Val)**2
sqrt_diff_M0Val = (sum_diff_M0Val / 20)**0.5

M = {}
for k3 in M0.keys():
    M[k3] = (M0[k3] - avg_M0Val) / sqrt_diff_M0Val

# Check for "zero mean value"
#M_sum=0
#for i in M.values():
#    M_sum += i
#print M_sum/20


# The correlation function is given by the Eq. 3
def theta_RiRj(Ri, Rj):
    return (
        (H1[Rj] - H1[Ri])**2 + (H2[Rj] - H2[Ri])**2 + (M[Rj] - M[Ri])**2) / 3


# Sequence order effect (Eq. 2)
def sum_theta_val(seq_len, LVal, n):
    sum_theta_RiRj = 0
    i = 0
    while i < (seq_len - LVal):
        sum_theta_RiRj += theta_RiRj(seq[i], seq[i + n])
        #print i, seq[i], i+n, seq[i+n], theta_RiRj(seq[i],seq[i+n])
        i += 1
    return sum_theta_RiRj / (seq_len - n)


# Check input param
if len(argv[1:]) != 4:
    print('Try again!')
else:
    WeightFactor = float(argv[1])
    LambdaVal = int(argv[2])
    infile = argv[3]
    outfile = argv[4]

    if (WeightFactor < 0.00) or (WeightFactor > 1.00):
        print('Check WeightFactor')
        print(
            'Please select any value within the region from 0.05 to 0.70 for the weight factor.'
        )
    else:
        fin = open(infile, 'r')
        with open(infile, 'r', encoding='utf-8') as scrape:
            fileContents = scrape.read()
        sequenceList = fileContents.split('\n')

        fasta_format = ''
        print('Clean sequences')
        for element in tqdm(sequenceList):
            Sequence = element.split(',')[0]
            formattedSeq = ''
            for char in Sequence:
                if char in aa_20:
                    formattedSeq = formattedSeq + char
            Sequence = formattedSeq
            if len(Sequence) <= LambdaVal:
                LambdaVal = len(Sequence) - 1
            Class = element.split(',')[1]
            fasta_format = fasta_format + '>' + Class + '\n' + Sequence + '\n'
        fout = open(outfile, 'w')
        flog = open('./output/input_seq.log', 'w')
        val1n = fasta_format.split('>')
        # create header
        header = ''
        for i in range(0, LambdaVal + 20):
            header = header + 'F' + str(i) + ','
        header = header + 'CLASS\n'
        fout.write(header)

        if val1n[0] != '':
            print('Check input sequence file format(FASTA).')
        else:
            seq_num = 1
            print('Build dataset')
            for m in tqdm(val1n[1:]):
                val2n = m.split('\n')
                Class = val2n[0]
                sequence_lines = []
                for n in val2n[1:]:
                    sequence_lines.append(n.replace(' ', ''))
                seq = str.join('', sequence_lines)
                seq = seq.upper()
                seq = seq.replace('\r', '')
                flog.write(
                    str(seq_num) + '\t' + Class + '\t' + str(len(seq)) +
                    'aa\t' + seq + '\n')

                # if len(check_seq(seq)) != 0:
                #     print(seq)
                #     unknown=check_seq(seq)
                #     print ('Sequence contains unknown amino acid:'), string.join((c if c in printable else r'\x{0:02x}'.format(ord(c)) for c in unknown), ', ')
                if (LambdaVal >= 0) and ((len(seq) - LambdaVal) > 0):
                    all_aa_freq = []
                    sum_all_aa_freq = 0
                    for aa in aa_20:
                        #normalized occurrence frequency of the 20 amino acids
                        aa_freq_val = float(aa_frequency(seq).get(
                            aa, 0)) / len(seq)
                        all_aa_freq.append(aa_freq_val)
                        sum_all_aa_freq += aa_freq_val

                    num = 1
                    all_theta_val = []
                    sum_all_theta_val = 0
                    while num < (int(LambdaVal) + 1):
                        tmpval = sum_theta_val(len(seq), LambdaVal, num)
                        all_theta_val.append(tmpval)
                        sum_all_theta_val += tmpval
                        num += 1

                    # Denominator of the Eq. 6
                    denominator_val = sum_all_aa_freq + (
                        WeightFactor * sum_all_theta_val)

                    all_PseAAC = []  # Eq. 5
                    for val1 in all_aa_freq:
                        all_PseAAC.append(
                            str(round((val1 / denominator_val), 5)))
                    for val2 in all_theta_val:
                        all_PseAAC.append(
                            str(
                                round(
                                    ((WeightFactor * val2) / denominator_val),
                                    5)))

                    #print all_PseAAC
                    fout.write(str.join(',', all_PseAAC) + ',' + Class + '\n')
                    seq_num += 1
                else:
                    print(
                        'Lambda must be non-Negative integer, such as 0, 1, 2, ...'
                    )
                    print(
                        'Lambda should NOT be larger than the length of input protein sequence.'
                    )
                    print(
                        'when Lambda=0, the output of PseAAC is the 20-D amino acid composition.'
                    )

        fin.close()
        fout.close()
        flog.close()
