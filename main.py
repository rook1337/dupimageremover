from DuplicateRemover import DuplicateRemover
import sys

dirname = str.strip(sys.argv[1])
# Remove Duplicates
dr = DuplicateRemover(dirname)
dr.find_duplicates()

# Find Similar Images
#dr.find_similar("test.png",70)