import sys

START_CODONES = ['ATG']
STOP_CODONES  = ['TAA', 'TAG', 'TGA']

def reverse_complimentary(seq):
    comp = lambda n: {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}[n]
    return ''.join(map(comp, seq[::-1]))


def calc_ORFs(seq):
    ORFs = []

    for offset in [0, 1, 2]:
        stop_codone = -1
        for i in range(len(seq)-3-offset, -1, -3):

                triplet = seq[i:i+3]
                
                if triplet in START_CODONES and stop_codone != -1:
                    ORFs.append((i+1, stop_codone+3))
                    
                if triplet in STOP_CODONES:
                    stop_codone = i
    return ORFs


with open(sys.argv[1], 'r') as f:
    lines = f.read().split('\n')
chrom = lines[0].split()[0][1:]
seq = ''.join(lines[1:])

res = ''
for ORF in calc_ORFs(seq):
    res += '{} {} {}\n'.format(chrom, ORF[0], ORF[1])

seq = reverse_complimentary(seq)
for ORF in calc_ORFs(seq):
    begin = len(seq)+1 - ORF[0]
    end   = len(seq)+1 - ORF[1]
    res += '{} {} {}\n'.format(chrom, begin, end)


with open(sys.argv[2], 'w') as f:
    f.write(res)



