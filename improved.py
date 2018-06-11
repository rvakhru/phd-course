import argparse
import re

def main():
    opts = parse_arguments()
    filename = opts.f
    file = open(filename)
    print_header(file)
    print_filtered_lines(file)

def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('f', help='input file') #better help needed
    return parser.parse_args()

def print_header(file):
    header = file.readline().split()
    print(*header, sep='\t')

def print_filtered_lines(file):
    #insert comment about filtering procedure
    for line in file:
        type, sequence, p_value, gene_ids = line.split()
        if significant_test(p_value) \
        and positive_p_value(p_value) \
        and not has_invalid_symbols(type, sequence) \
        and has_genes_with_valid_ensemble_ids(gene_ids):
            print("DNA", transform_to_dna(sequence), p_value, gene_ids, sep = "\t") #maybe better print

def positive_p_value(p_value):
    return float(p_value) >= 0

def significant_test(p_value, significance_threshold = 0.05):
    return float(p_value) < significance_threshold

# maybe remove magic numbers / strings from below (although they are very self-explanatory)
def has_invalid_symbols(type, sequence):
    if type == "DNA":
        return has_invalid_dna_symbols(sequence)
    else:
        return has_invalid_rna_symbols(sequence)

def has_invalid_dna_symbols(sequence):
    return [symbol for symbol in sequence if symbol not in "ACGT"]

def has_invalid_rna_symbols(sequence):
    return [symbol for symbol in sequence if symbol not in "ACGU"]

def transform_to_dna(sequence):
    return sequence.replace("U", "T")

def has_genes_with_valid_ensemble_ids(genes):
    return [gene for gene in genes.split(",") if is_valid_ensembl_id(gene)]

def is_valid_ensembl_id(gene_id):
    #comment about how a ensembl id looks like
    ensembl_gene_regex = r'ENSG[0-9]+'
    return re.match(ensembl_gene_regex, gene_id) is not None

if __name__ == '__main__':
    main()
