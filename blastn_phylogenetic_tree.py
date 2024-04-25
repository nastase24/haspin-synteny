from Bio.Blast import NCBIWWW
from Bio.Blast import NCBIXML
from Bio import AlignIO
from Bio.Align.Applications import ClustalwCommandline
from Bio import Phylo
import matplotlib.pyplot as plt

# Author: Alex Nastase

# Taken from Tammy's labs, converts a fasta file to a sequence or 
# returns -1 if the file is not in fasta format
def convertFileToSequence(filename):
    clean = -1
    with open(filename, 'r') as file:
        # read in first line
        header = file.readline()
        if (header[0] == '>'):
            print("in FASTA format")
            clean = 1
            # read rest of file
            sequence = file.read()
            # remove all return and newline characters
            sequence = sequence.replace("\r", "")
            sequence = sequence.replace("\n", "")
        else:
            print("invalid format")
    if(clean == -1): return -1  # so other functions can check
    return sequence

#Prompt user input for the filename and the title of the figure
sequence = convertFileToSequence(input("Enter the filename of a Fasta file: "))
title = input("Enter descriptive title for the figure being created: ")

# Perform BLAST search. You can use blastn by using the commented out line below instead 
#result_handle = NCBIWWW.qblast("blastn", "nt", sequence,hitlist_size=10)
result_handle = NCBIWWW.qblast("blastp", "nr", sequence, hitlist_size=15)
blast_records = NCBIXML.parse(result_handle)

# Save the sequences from the BLAST results, including species names in sequence names
with open("blast_results.fasta", "w") as out_handle:
    written_seq = set()
    for blast_record in blast_records:
        for alignment in blast_record.alignments:
            for hsp in alignment.hsps:
                # Extract species name from sequence title
                start = alignment.title.find('[')
                end = alignment.title.find(']')
                if start != -1 and end != -1:
                    species_name = alignment.title[start+1:end].replace(' ', '_')
                    print(species_name)
                else:
                    species_name = 'unknown'
                # annotate label with species name and score    
                unique_id = ">%s_%d\n" % (species_name,hsp.score)
                if unique_id not in written_seq:    
                # Append unique identifier and species name to each sequence name
                    out_handle.write(">%s_%d\n%s\n" % (species_name,hsp.score,hsp.sbjct))
                    written_seq.add(unique_id)

# Perform multiple sequence alignment using ClustalW
clustalw_cline = ClustalwCommandline("clustalw2", infile="blast_results.fasta")
stdout, stderr = clustalw_cline()

# Read the alignment results
align = AlignIO.read("blast_results.aln", "clustal")

# Construct a phylogenetic tree
tree = Phylo.read("blast_results.dnd", "newick")
fig,ax = plt.subplots(figsize=(10,10))
plt.title(title)
plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1)

# Print the phylogenetic tree
Phylo.draw(tree,axes=ax)
