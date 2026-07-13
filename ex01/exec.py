import sys

arguments_list=sys.argv[1:]
merged_list=" ".join(arguments_list)


print(merged_list[::-1].swapcase())