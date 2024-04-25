README for blastn_phylogenetic_tree.py
This script performs a BLAST search, 
constructs a multiple sequence alignment, 
and generates a phylogenetic tree from the results.

Expected Input:
- genetic data in FASTA format. Ex "myGene.fasta"
- user input to select the file, and label output

Expected Output:
- blast alignment results file: "blast_results.fasta"
- clustal multiple sequence alignment files: "blast_results.aln", "blast_results.dnd"
- Phylogenetic tree figure, able to be saved as file.
WARNING: if you want to save any of these files, move/rename them or
they will be overwritten next time you run it


PSEUDOCODE:
1. Define the sequence to be used for the BLAST search.
2. Perform a BLAST search using the defined sequence:
   - Use the "blastp" program and the "nr" database.
   - Limit the number of hits to 15.
3. Parse the BLAST results.
4. Open a file for writing.
5. For each record in the BLAST results:
   - For each alignment in the record:
     - For each high-scoring pair (HSP) in the alignment:
       - Extract the species name from the alignment title.
       - If the species name is not found, set it to 'unknown'.
       - Write the unique identifier and the sequence to the file.
6. Close the file.
7. Perform a multiple sequence alignment on the sequences in the file using ClustalW.
8. Construct phylogenetic tree from the results.


Requirements:
Python 3
Biopython ('pip install biopython')
ClustalW (install on your computer, and add the directory path to your $PATH environment variable, restart computer)
matplotlib ('pip install matplotlib')

Usage: 

"python3 blastn_phylogenetic_tree.py" 
-put your fasta file in the same directory as the python script
-follow command line instrutions to input fasta filename, and figure descriptive title
- it may take a while to compute

Please note that you may need to adjust the parameters of the BLAST search and the multiple sequence alignment to suit your specific needs.