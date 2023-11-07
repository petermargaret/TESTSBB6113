import gzip
from Bio import SeqIO

i = 0
for l in gzip.open("SRR26442322.fastq.gz","rt"):
    i += 1
print("Total Genome Reads: ",i)