################################################################################
# Question 2: Given an array of integers, write some code to find all the 
# integers that appear more than once in the array, sorted by which appears 
# most often to least often (once) 
#
# Solution Approach : Used Counter function of the collection class 
# This class is ideal for maintaining < key, freq > pairs for hashable objects.
# 
#
#################################################################################

# Importing Counter function from collection class

from collections import Counter
import sys


# Function to calculate the frequency of elements and print them in sorted order 

def calculate_frequency_of_elements(array):
 frequency_of_elements = Counter ()			   

 for element in array:
  if isinstance(element,int):
   frequency_of_elements[element] +=1
  else:
   print "The array contains non-integer values, please check your input"
   sys.exit()									
     
 print "The list of elements in descending order of frequency :", frequency_of_elements
 
 
 
# Main function to take input and validate it
def main():
  
 input_array_of_integers= []
 try:
   input_array_of_integers = input("Please enter an array of integers in [x,y,z] format :")
   
   if isinstance(input_array_of_integers,list) and len(input_array_of_integers)!= 0:
       calculate_frequency_of_elements(input_array_of_integers)
   else:
	    print "Your input doesn't seem to be an array. Are you sure you entered it correctly? eg input: [2,2,2,3,4]"
		
 except :
   print "Sorry ! Your input doesn't seem to be valid. Please enter only integers. eg input: [2,2,2,3,4] "
   
# Main function called
if __name__ == "__main__":
    main()
