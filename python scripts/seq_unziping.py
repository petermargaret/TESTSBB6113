#unzipping the Mycobacterium WGS FILE

import gzip 

print("unzipping Genome File...")
seq = b'SRR26442322.fastq.gz'
seq = gzip.compress(seq) 
  
# using gzip.decompress(seq) method 
out_file = gzip.decompress(seq) 
print(out_file) 