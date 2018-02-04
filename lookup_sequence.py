#!/usr/bin/env python3

# Read in file
FASTA_file = open('e_coli_k12_dh10b.faa', 'r')

# Dict to track unique sequences
sequences = {}
# Tracks amount of genes
gene_count = 0
# Tracks if the gene was found
gene_found = False


for line in FASTA_file:
	# Sets each unique sequence into the sequence dict
	if line.startswith('>'):
		name = line[1:].rstrip('\n')
		sequences[name] = ''
		gene_count += 1

	elif(gene_count > 0):
		sequences[name] += line.rstrip('\n')

# User input for accessin number
acc_num = raw_input('Enter an accession number to search for: ')

# Searchs sequences for the accession number
for gene in sequences:
	# Splits the string to find the accession number
	acc = gene.split('|')
	if(acc_num == acc[3]):
		print(gene)
		print(sequences[gene])
		gene_found = True

# If the gene was not in the FASTA file
if(not gene_found):
	print("Accession number not found")