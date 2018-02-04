#!/usr/local/bin/python3

import jinja2
import re

# This line tells the template loader where to search for template files
templateLoader = jinja2.FileSystemLoader( searchpath="./templates" )

# This creates your environment and loads a specific template
env = jinja2.Environment(loader=templateLoader)
template = env.get_template('unit04.html')

# Read in file
FASTA_file = open('e_coli_k12_dh10b.faa', 'r')

# Dict to track unique sequences
sequences = {}
gene_count = 0

# List to keep track of FASTA description elements
id_portion = []
seq_length = []
rest_of_header = []

# List to track how many rows to show in the html file
row_count = []

for line in FASTA_file:
	# Sets each unique sequence into the sequence dict
	if line.startswith('>'):
		name = line[1:].rstrip('\n')
		sequences[name] = ''
		gene_count += 1

	elif(gene_count > 0):
		sequences[name] += line.rstrip('\n')

# Parses the correct description elements
for seq in sequences:
	header = seq.split(' ')
	id_portion.append(header[0])
	seq_length.append(len(sequences[seq]))
	temp = ' '.join(header[1:])
	rest_of_header.append(temp)

# Appends 20 rows
for i in range(20):
	row_count.append(i)
    
print("Content-Type: text/html\n\n")
print(template.render(ids=id_portion, length=seq_length, ends=rest_of_header, rows=row_count))
