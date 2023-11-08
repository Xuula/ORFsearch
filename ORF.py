START_CODONES = ['ATG']
STOP_CODONES  = ['TAA', 'TAG', 'TGA']

def reverse_complimentary(seq):
    comp = lambda n: {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}[n]
    return list(map(comp, seq[::-1]))


def calc_ORFs(seq):
    ORFs = []

    for offset in [0, 1, 2]:
        stop_codone = -1
        for i in range(len(seq)-3-offset, -1, -3):

                triplet = seq[i:i+3]
                
                if triplet in START_CODONES and stop_codone != -1:
                    ORFs.append((i, stop_codone+2))
                    
                if triplet in STOP_CODONES:
                    stop_codone = i
    return ORFs


seq = input()

print('Открытые рамки считывания:')
for ORF in calc_ORFs(seq):
    print(f'({ORF[0]}:{ORF[1]})')

print('Повторный запуск на обратно комплиментарной последовательности...')

seq = reverse_complimentary(seq)
for ORF in calc_ORFs(seq):
    print(f'({ORF[0]}:{ORF[1]})')


