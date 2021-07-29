from data import *
from array_sorting import *
from main_array_sorting import *


i=0
while i < len(array):
    bubble_sort(array[i])
    middle_value(array[i])
    i += 1
main_bubble_sort(middle_array, array)
print (array)
