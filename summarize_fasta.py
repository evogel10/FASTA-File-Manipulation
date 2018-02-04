#!/usr/bin/env python3

# Read in file
FASTA_file = open('e_coli_k12_dh10b.faa', 'r')

# Dict to track unique sequences
sequences = {}
# Tracks amount of genes
gene_count = 0
minimum = 999999999999
maximum = 0
# Counts all the amino acids in FASTA file
total_aa = 0
hypothetical = 0

for line in FASTA_file:
	# Sets each unique sequence into the sequence dict
	if line.startswith('>'):
		name = line[1:].rstrip('\n')
		sequences[name] = ''
		gene_count += 1
		# Finds descriptions with hypothetical
		if('hypothetical' in line):
			hypothetical += 1
	elif(gene_count > 0):
		sequences[name] += line.rstrip('\n')

# Finds the max and min sequence lengths
for gene in sequences:
	length = len(sequences[gene])
	if (length > maximum):
		maximum = length
	elif(length < minimum):
		minimum = length
	# Tracks the total amount of amino acids in FASTA file
	total_aa = total_aa + length

print("The FASTA contains %d genes") % (gene_count)
print("The minimum protein length is %d amino acids") % (minimum)
print("The maximum protein length is %d amino acids") % (maximum)
print("The average protein length is %d amino acids") % (total_aa / gene_count)
print("%d number of genes have 'hypothetical' in their descriptions") % (hypothetical)

