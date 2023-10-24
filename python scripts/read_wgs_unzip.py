
from Bio import SeqIO
import tarfile
import gzip

file = gzip.open("SRR26442322.fastq.gz","rt")
fq = SeqIO.parse(file, "fastq")
for read in fq:
        print(read)
file.close()