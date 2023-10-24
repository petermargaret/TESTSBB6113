# importing the "tarfile" module 
import tarfile 

# open file 
genome_file = tarfile.open('SRR26442322.fastq.gz') 

# extracting file 
genome_file.extractall('./sequences') 

genome_file.close() 
