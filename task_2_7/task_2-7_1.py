data="01_02_08"
files = ["seq1", "seq2", "seq3", "seq4"]
for name in files:
   new_name = name +data+ ".fasta"
   print(f"{new_name}")