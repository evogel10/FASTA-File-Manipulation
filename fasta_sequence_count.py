#!/usr/bin/env python3

# Opens the file to read
fasta_file = open("e_coli_k12_dh10b.faa")

# This function takes in a FASTA file and counts the number of sequence entries
def fasta_sequence_count(file):

	fasta_count = 0

	# For loop iterates through file line by line searching for '<'
	for line in file:
		# If '<' is found the entry is added to the count
		if line.startswith(">"):
			fasta_count += 1
	return fasta_count

print ("There are {0} sequences within the file.".format(fasta_sequence_count(fasta_file)))

# Closes file
fasta_file.close()