#!/usr/bin/env python3

import operator

# This program takes in a file containing all of the polypeptide
# sequences in the E. coli K12 genome in FASTA format. The program
# then returns to its output the 5 most frequently used amino acids 
# and add their percentage use

# Read in file
FASTA_file = open('e_coli_k12_dh10b.faa', 'r')

# Dicts to track unique sequences and counts of amino acids
sequences = {}
counts = {}
total = 0

for line in FASTA_file:
	# Sets each unique sequence into the sequence dict
	if line.startswith('>'):
		name = line[1:].rstrip('\n')
		sequences[name] = ''
	else:
		sequences[name] += line.rstrip('\n')
		# Caluculates how many aa type is in each unique sequence
		for aa in sequences[name]:
			if aa in counts:
				counts[aa] = counts[aa] + 1
			else:
				counts[aa] = 1

# Creates now dict of top 5 ammino acids
top_aa = dict(sorted(counts.iteritems(), key=operator.itemgetter(1), reverse=True)[:5])

# Calculate total amino acids
for value in counts.values():
	total = total + value

for key, value in top_aa.items():
	print('%s: %d (%.1f%s)') % (key, value, ((value * 1.0)/(total * 1.0) * 100), '%')


