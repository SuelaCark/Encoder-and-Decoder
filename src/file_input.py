# This file manages the file input file and handles it to the respective cipher for encryption
# of the file contents

# The input/output files can be managed and structure in 2 ways:
# 1. Each cipher can hold try clauses (bad direct implementation)
# 2. The main Cipher class can manage the file input and output, while the children classes access
#    and/or override these methods (better code optimization)
# 3. There can be a separate input and output file for file management before and after encryption
