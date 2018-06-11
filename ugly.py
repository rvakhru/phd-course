import argparse
import re


def main():
    p = argparse.ArgumentParser()
    p.add_argument('f', help='input file')
    args = p.parse_args()
    with open(args.f) as infile:
        header = infile.readline().split()
        print(*header, sep='\t')
        for line in infile:
            toks = line.split()
            # remove insignificant tests
            if float(toks[2]) > 0.05:
                continue
            # check whether the sequence is invalid
            valid_seq, dna_seq = is_valid(toks[1], toks[0])
            if not valid_seq:
                continue
            gene_ids = toks[3].split(',')
            n_valid_genes = count_valid_genes(gene_ids)
            if not n_valid_genes:
                continue
            # print results
            print_line('DNA', dna_seq, float(toks[2]), gene_ids)


def print_line(nuc_type, sequence, p_value, gene_ids):
    # p-values smaller than 0 are not possible
    if p_value < 0:
        return
    print(nuc_type, sequence, p_value, ','.join(gene_ids), sep='\t')


def is_valid(seq, type):
    valid = True
    if type == 'RNA':
        for s in seq:
            if s not in 'ACGU':
                valid = False
                break
        # RNA uses Uracil (U), which corresponds to Thymine (T) in DNA
        seq = seq.replace('U', 'T')
    else:
        for s in seq:
            if s not in 'ACGT':
                valid = False
                break
    return valid, seq


def count_valid_genes(genes):
    """counts the number of valid genes
    """
    n_count = 0
    current = 0
    remaining = len(genes)
    while remaining > 0:
        if is_valid_ensembl_id(genes[current]):
            n_count += 1
            current += 1
            remaining -= 1
        else:
            remaining -= 1
            # remove invalid gene id
            del genes[current]
    return n_count


def is_valid_ensembl_id(gene_id):
    ensembl_gene_regex = r'ENSG[0-9]+'
    return re.match(ensembl_gene_regex, gene_id) is not None


if __name__ == '__main__':
    main()
