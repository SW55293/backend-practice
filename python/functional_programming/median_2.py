'''
ASSIGNMENT
In the world of document conversion, you'll sometimes need to handle fonts and font sizes. 
Complete the get_median_font_size function.

Given a list of numbers representing font sizes, return the median font size. If the list is empty, 
return None. If the list has an even number of elements, return the average of the two middle elements.

'''

# My try
from statistics import median
def get_median_font_size(font_sizes):
    if len(font_sizes) == 0: return None

    return median(font_sizes)

# Functional Programming way
def get_median_font_size(font_sizes):
    if len(font_sizes) == 0:
        return None
    sorted_sizes = sorted(font_sizes)
    n = len(sorted_sizes)
    if n % 2 == 0:
        return (sorted_sizes[n // 2 - 1] + sorted_sizes[n // 2]) / 2
    else:
        return sorted_sizes[n // 2]